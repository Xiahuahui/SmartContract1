## python 3.6.1
# TODO List
# 1. CNF包的扩展，现阶段只支持合取范式
# 2. 自动化测试工具，用以检测传给game tree的状态机是否正缺
# 3. 外部action的处理只是临时方案，存在隐患
# 4. 合同的输入极度严格其缺乏完备的错误提示
import json
import numpy as np
import operator
import generateGo
import generateSol
from CNF.CNF import *
import copy
import re
import time
import pickle as pickle


# 和博弈树对接定义的接口
# edge格式 - { ( [pid], [ [action_person, action], ... ] ), ...  }
class GNode:
    def __init__(self):
        self.id = 0
        self.data = []
        self.edge = []
        self.children = []

    def getedge(self):  # 得到该节点的入边
        return self.edge

    # 不重复的添加edge
    def addEdge(self, edge):

        self.edge = edge

    # 不重复的添加该节点的孩子节点
    def addChild(self, child):
        for i in range(len(self.children)):
            if self.children[i] == child:
                return
        self.children.append(child)

    def getedges(self):  # 得到该节点的所有出边
        Edge = []
        for child in self.children:
            edge = child.getedge()
            for e in edge:
                Edge.append(e)
        return Edge

    def getId(self):
        return self.id

    def getchildren(self):
        return self.children

    def getplayer(self):  # 得到该节点的动作人 player
        player = []
        for child in self.children:
            edges = child.getedge()
            for edge in edges:
                length = len(edge)
                Player = []
                for l in range(length):
                    Player.append(edge[l][0] + str(edge[l][2]))
                player.extend(Player)
        player = set(player)
        player = list(player)
        return player

    def getaction(self):  # 得到该节点的所有动作
        action = []
        Edges = self.getedges()
        for e in Edges:
            for act in e:
                action.append(act)
        removal = []  # 列表去重
        for i in action:
            if i not in removal:
                removal.append(i)
        action = list(removal)
        return action


# 存储BFS辅助信息
# state - 状态机的一个状态
# graph - 依赖图结构
class St_node:  # 定义了状态机中一个合理状态节点
    def __init__(self, Id, state, graph):
        self.Id = Id
        self.state = state
        self.graph = graph

    def print_content(self):
        print(self.Id)
        print(self.state)


# 状态机存储结构，与前端对应
# current --action--> newS
class Transfer:
    def __init__(self, current, action, newS):
        self.current = current
        self.action = action
        self.newS = newS

    def print_content(self):
        print("==========Transfer==========")
        print(self.current)
        print(self.action)
        print(self.newS)


# 依赖图中的一个节点,一个节点与一个条款一一对应
class GraphNode:
    # premise是CNF包下的结构体
    # title则是该节点的名称，格式：Term+从0开始的int数字
    # 特殊信息
    # ActionInPre - 前提中是否包含外部action的标志位，true则表明前提中有
    # ContractFlag - 条款的动作人是否为contract的标志位，true则表示前提的动作人为contract
    def __init__(self, title):
        self.premise = CNF()  # 逻辑表达式
        self.title = title  # 条款的序号
        self.flag = False  # 前提中的承诺是否全部到达终态
        self.ActionInPre = False  # 前提中是否有judge()
        self.ContractFlag = False  # 动作人是否是Contract
        self.action = []  # 前提中的judge()的总数
        self.judgeplayer = []
        self.condition = []  # 存储承诺前提里面含有的其他承诺号
        self.iscontradiction = False  # 是不是矛盾式
        self.istautology = False  # 判断是不是重言式

    # 根据条款的前提构建CNF
    def buildPremise(self, premise):
        # 如果前提中包含外部action，修改标志位
        clause = re.split('[||&&]', premise)
        for t in range(len(clause)):
            if clause[t] == ' ' or clause[t] == '\n' or clause[t] == '':
                continue
            if "Term" not in clause[t]:
                # print("action:" + clause[t])
                if clause[t] not in self.action:
                    self.action.append(clause[t])
                    tmp = clause[t].split("(")
                    # print("judge动作人",tmp[1][0])
                    self.judgeplayer.append(tmp[1][0])
                self.ActionInPre = True
            if "Term" in clause[t]:
                idx = clause[t].find(".")
                number = clause[t][4:idx]
                if number not in self.condition:
                    self.condition.append(number)
        self.premise.build(premise)


# 依赖图结构
class Graph:
    def __init__(self, n):
        # 图采用邻接矩阵来保存，
        # 矩阵matrix的元素是edge结构体的list
        # matrix[i][t]表示vertex[i]到vertex[t]的边
        # vertexList和matrix的顺序一一对应
        # valueMap - Boolean类型的Map，CNF包求值所必需的结构，构成：
        # 一个条款会产生3个key，分别是title.Sat  title.Exp  title.Vio
        # 当条款处于Sat、Exp、Vio中任一状态时，就将对应的key赋值为true，三个key至多有一个为true
        self.matrix = [[[] * n for i in range(n)] for _ in range(n)]
        self.vertexList = []
        self.valueMap = {}

    # 不重复的添加依赖图节点，同时更新valuemap
    def addNode(self, graphNode):
        self.vertexList.append(graphNode)
        postfix = [".Sat", ".Exp", ".Vio"]
        for i in range(len(postfix)):
            key = graphNode.title + postfix[i]
            self.valueMap[key] = False
        for j in range(len(graphNode.action)):
            key = graphNode.action[j]
            self.valueMap[key] = False


# 根据json中条款的顺序返回两个list
# actperson - 第一个list的每一个元素则是条款的动作人
# actionlist - 第二个list的每一个元素则是该条款的动作
def getPersonAction(jsondata):
    actperson = []
    actionlist = []
    stateNum = len(jsondata)
    for i in range(stateNum):
        tmp = jsondata[i]['person'].split(" ")
        actperson.append(tmp[0])
        actionlist.append(jsondata[i]['res'])
    return (actperson, actionlist)


# 核心函数
# 状态机生成算法，BFS
def generate(inputdate):
    jsondata = json2python(inputdate)
    # state num
    StateNum = len(jsondata)
    # 获取动作人和动作列表
    actperson, actionList = getPersonAction(jsondata)
    # print(actionList)
    # =======================Step 1================================
    # 初始化根节点的状态
    initState = np.ones(StateNum)  # .astype(int)
    for i in range(StateNum):
        # no dependence with others
        if jsondata[i]['premise'] == None or jsondata[i]['premise'] == "":
            initState[i] = 2
    # print("initial state:", initState)

    # =======================Step 2================================
    # 根据前提构建有向无环图
    graph = BuildGraph(jsondata, StateNum, actperson)
    for k in range(StateNum):
        if initState[k] == 2:
            graph.vertexList[k].flag = True
    # print("matrix:")
    # print(graph.matrix)
    # =======================Step 3================================
    # 广度优先搜索（队列辅助实现），寻找所有合理的状态机节点
    id = 0
    chmap = {2: 'Bas', 3: 'Sat', 4: 'Exp', 5: 'Vio'}
    st = St_node(0, initState, graph)
    queue = []
    transfer = []
    queue.append(st)
    gnodelist = []
    # BFS
    ii = 0
    while len(queue):
        # input("按任意键继续")
        st = queue.pop(0)
        ii = ii + 1
        print(ii)
        # 直接复制，防止浅拷贝错误
        state = st.state.copy()
        graph = copy.deepcopy(st.graph)

        # print("####################################################")
        # print("current state:")
        # print(state)

        # =======================Step 3.1================================
        # 更新图和边
        graph = updateGraph(graph, state)
        done = 0
        for i in range(StateNum):
            if state[i] >= 3:
                done += 1
        # 迭代边界-所有承诺状态处于终态(3,4,5)
        if done == StateNum:
            continue
        # 如果不是(接受状态)终态 则查找所有的独立条款及其组合
        # =======================Step 3.2================================
        uclist = getUcList(state, graph)  # 查找所有独立的条款及变化
        print("uclist")
        print(uclist)
        print(len(uclist))
        for changecombine in uclist:  # 每个变化的组合对应一条边
            preState = st.state.copy()  # 得到父亲节点的状态
            preGraph = copy.deepcopy(graph)  # 复制父亲节点的依赖图
            edge, action, newState, newGraph = getDGAEdge(changecombine, preState, preGraph, actperson, actionList)
            gnodelist, pnode, id = findGnode(gnodelist, state, id)  # 从队列里面得到父亲节点
            gnodelist, cnode, id = findGnode(gnodelist, newState, id)  # 从队列里面得到孩子节点
            pnode.addChild(cnode)  # 将孩子节点连接到父亲节点上
            cnode.addEdge(edge)  # 将边加到孩子节点
            # 生成状态机文件
            newSt = St_node(id, newState, newGraph)  # 初始化新节点

            queue.append(newSt)  # 将节点加入队列
            tran = Transfer(state, action, newState)  # 构造变化
            transfer.append(tran)  # 将变化入队
    # 输出态机
    # 主要观察：
    # 1. 结构是否正确
    # 2. 有无重复

    return (initState, transfer, gnodelist[0])


# 得到所有变化的组合
# Input
# state, 所有承诺的当前状态 [3,1,2,2]
# graph, 当前节点的依赖图  即各个条款的真值 {Term0.Sat : True ,Term0.Vio : Flase,Term0.Exp: Flase,Term1.Sat : Flase ,Term1.Vio : Flase,Term1.Exp: Flase......}
# Output
# res   所有变化的组合 {[[1,2],[2,3],[3,5]],[1,2],[2,3],[3,3]]...}
def getUcList(state, graph):
    zeroslist1, nextStates1 = getPostactChanges(state, graph)  # 得到所有Postact

    zeroslist2, nextStates2 = getBasChange(state, graph)  # 得到所有act

    zeroslist1.extend(zeroslist2)
    for i in range(len(zeroslist2)):
        nextStates1[zeroslist2[i]] = nextStates2[zeroslist2[i]]
    zeroslist = list(zeroslist1)
    nextStates = list(nextStates1)

    currentChange = []
    for index in zeroslist:
        currentChange.append(nextStates[index])
    # combination
    res = []
    tmp = []
    res = combination(res, 0, tmp, currentChange, zeroslist)
    return res


# 得到父节点到子节点之间的复合边 并生成新的节点的状态,并将依赖图进行更新
# Input
# changecombine   [[1,2],[2,3],[3,5]]  #一条复合边的变化
# preState [3,1,2,2]   #当前节点的状态
# preGraph # 当前节点的依赖图{Term0.Sat : True ,Term0.Vio : Flase,Term0.Exp: Flase,Term1.Sat : Flase ,Term1.Vio : Flase,Term1.Exp: Flase......}
# actorList ,['A','B','A','A'] 所有条款的动作人列表
# actList  [act1,act2,act3,..] 所有条款的动作列表
# Output
# edge {[[actperson,act,index],[actperson,act,index],[actperson,act,index]]...}   子节点到父节点的一条复合边 action 用于在前端的显示
# action 用于前端显示
# newState 新节点的状态
# newGraph 新节点的依赖图
def getDGAEdge(changecombine, preState, preGraph, actorList, actList):
    edge = [[]]  # 初始化边
    action = "("  # 初始化动作
    for change in changecombine:  # 对于每个条款的变化
        index = change[0]  # 哪个条款的变
        Change = change[1]  # 变化的条款变化的终态
        if preState[index] == 2:  # 对于变化之前是2的承诺
            ap = actorList[index]  # 动作人
            act = actList[index]  # 执行的动作
            if Change == 3:  # 当变化为3时
                act = "sat" + act
            else:  # 当变化为5时
                act = "vio" + act
            element = [ap, act, index]
            action = action + 'Term' + str(index + 1) + ap + act + ', '  # 将act加入action
            for hh in range(len(edge)):
                edge[hh].append(element)
        else:  # 对于变化之前是1的承诺
            if (preGraph.vertexList[index].iscontradiction == True) or (
                    preGraph.vertexList[index].istautology == True):  # 如果前提是矛盾式
                ap = 'C'
                act = ''
                element = [ap, act, index]
                action = action + 'Term' + str(index + 1) + ap + act + ', '
                for hh in range(len(edge)):
                    edge[hh].append(element)
            else:  # 当1可变为2或4 时
                isChangedToBase = (Change == 2)  # 当变化为2时为True 否则为False
                element, act = getJudgeSat(index, preGraph, actorList, isChangedToBase)  # 获得满足的所有的judge组合
                Action = []
                for h in range(len(element)):
                    for hhh in range(len(edge)):
                        for hhhh in range(len(element[h])):
                            edge[hhh].append(element[h][hhhh])
                        Action.append(list(edge[hhh]))
                        for hhhh in range(len(element[h])):
                            edge[hhh].pop()
                action = action + act
                edge = list(Action)
        preState[index] = Change
    action = action[:-2] + ')'
    newState = preState
    newGraph = updateGraph(preGraph, newState)
    return (edge, action, newState, newGraph)


# 得到满足状态的judg组合
# Input
# index,  变化条款的编号
# newGraph, {Term0.Sat : True ,Term0.Vio : False,Term0.Exp: False,Term1.Sat : False ,Term1.Vio : False,Term1.Exp: False.....}
# actperson ,['A','B','A','A'] 所有条款的动作人列表
# isChangedToBase    True||False  当变为2时为True 当变为4时为False
# Output
# Cat [[["B",judge(),"00"],["B",!judge(2),"00"]],[["B",!judge(),"00"],["B",!judge(2),"00"]]]
def getJudgeSat(index, preGraph, actperson, isChangedToBase):
    length = len(preGraph.vertexList[index].action)  # 对应条款中的judge个数
    length1 = 2 ** length  # 对于judge赋值
    Cact = []
    action = ""
    # 将真值转化为二进制数
    for j1 in range(length1):
        ll = ['0'] * length
        for t1 in range(len(list(DEC2Bin(j1)))):
            ll.pop()
        ll.extend(list(DEC2Bin(j1)))
        act = ''
        cact = []
        for k in range(length):
            preGraph.valueMap[preGraph.vertexList[index].action[k]] = int(ll[k])  # 对于各个judge赋值
            if int(ll[k]) == 0:
                act = act + actperson[index] + '!' + preGraph.vertexList[index].action[k] + '|'
                cact.append(
                    [preGraph.vertexList[index].judgeplayer[
                         k], '!' + preGraph.vertexList[index].action[
                         k], str(k) + str(k)])
            if int(ll[k]) == 1:
                act = act + actperson[index] + preGraph.vertexList[index].action[k] + '|'
                cact.append(
                    [preGraph.vertexList[index].judgeplayer[
                         k], preGraph.vertexList[index].action[
                         k], str(k) + str(k)])
        if preGraph.vertexList[index].premise.getValue(preGraph.valueMap) == isChangedToBase:
            act = act[:-1]
            action = action + 'Term' + str(index + 1) + act + ', '
            Cact.append(cact)
    return (Cact, action)


# 辅助函数
# 朴素算法判断两个list是否相同
def isequle(list1, list2):
    n = len(list1)
    for i in range(n):
        if list1[i] != list2[i]:
            return False
    return True


# 如果有则返回该节点
# 如果没有则建立新的节点，然后返回
def findGnode(NodeList, state_np, id):
    state = state_np.astype(int).tolist()
    for i in range(len(NodeList)):
        if isequle(NodeList[i].data, state) == True:
            return (NodeList, NodeList[i], id)

    # 查找不存在，新建节点
    node = GNode()
    node.data = state
    node.edge = []
    node.id = id
    NodeList.append(node)
    # 注意更新id
    return (NodeList, node, id + 1)


# 更新依赖图，主要是valuemap的更新
def updateGraph(graph, state):
    chmap = {2: 'Bas', 3: 'Sat', 4: 'Exp', 5: 'Vio'}
    postfix = [".Sat", ".Exp", ".Vio"]
    stateNum = len(state)
    for i in range(stateNum):
        if state[i] >= 3:
            key = "Term" + str(i + 1) + "." + chmap[state[i]]
            graph.valueMap[key] = True
    for j in range(len(graph.vertexList)):
        flag1 = True
        for k in range(len(graph.vertexList[j].condition)):
            flag2 = False
            for t in range(len(postfix)):
                key = "Term" + str(graph.vertexList[j].condition[k]) + postfix[t]
                flag2 = flag2 or graph.valueMap[key]
            flag1 = flag1 and flag2
        if flag1 == True:
            graph.vertexList[j].flag = True

    return graph


# 根据json数据构建依赖图
def BuildGraph(jsondata, StateNum, actperson):
    # 条款状态的映射，详见论文条款定义
    chmap = {'Sat': 3, "Exp": 4, "Vio": 5}

    graph = Graph(StateNum)
    # 生成GraphNode
    for i in range(StateNum):
        title = "Term" + str(i + 1)
        node = GraphNode(title)
        premise = jsondata[i]['premise']
        if premise == None:
            premise = ""
        # 根据前提构建CNF表达式
        node.buildPremise(premise)
        # 将当前节点加入graph中
        graph.addNode(node)

        # ！！！！注意，约定大写C代表contract
        if actperson[i] == 'C':
            node.ContractFlag = True

    # 根据各个条款的前提，生成依赖图的邻接矩阵
    for i in range(StateNum):
        premise = jsondata[i]['premise']
        # 前提为空，统一处理为空字符串
        if premise == None:
            premise = ""

        # 以||和&&为分隔符分割
        clause = re.split('[||&&]', premise)
        for t in range(len(clause)):
            if "Term" not in clause[t]:
                continue
            tmp = clause[t].split('.')
            index = int(tmp[0][4:]) - 1
            state = chmap[tmp[1]]
            graph.matrix[i][index].append(state)
    return graph


# middleware
# 辅助函数
# 递归，把独立条款集合的所有可能的次态组合生成状态机的次态
# tmplist - 存放递归过程的中间结果
# nextSatet - 条款的次态
# index - 独立条款的下标集合
def combination(res, ith, tmplist, nextState, index):
    if ith == len(nextState) and len(tmplist):
        res.append(tmplist)
        return res

    for t in range(len(nextState[ith])):
        # ！必须深拷贝
        tmp = tmplist.copy()
        tmp.append([index[ith], nextState[ith][t]])
        res = combination(res, ith + 1, tmp, nextState, index)
    return res


# 判断矛盾式的辅助函数
# 递归，从0开始，遍历所有可行的valuemap组合
# 3叉树
def recursion(cnf, valueMap, TermFlag, index):
    if index == len(TermFlag):
        return cnf.getValue(valueMap)
    if TermFlag[index] == True:
        return recursion(cnf, valueMap, TermFlag, index + 1)

    res = False
    postfix = [".Sat", ".Exp", ".Vio"]
    for i in range(len(postfix)):
        key = "Term" + str(index + 1) + postfix[i]
        valueMap[key] = True
        res = res or recursion(cnf, valueMap, TermFlag, index + 1)
        valueMap[key] = False
        if res == True:
            break
    return res


def recursion2(cnf, valueMap, TermFlag, index):
    if index == len(TermFlag):
        return cnf.getValue(valueMap)
    if TermFlag[index] == True:
        return recursion2(cnf, valueMap, TermFlag, index + 1)
    res = True
    postfix = [".Sat", ".Exp", ".Vio"]
    for i in range(len(postfix)):
        key = "Term" + str(index + 1) + postfix[i]
        valueMap[key] = True
        res = res and recursion2(cnf, valueMap, TermFlag, index + 1)
        valueMap[key] = False
        if res == False:
            break
    return res


# 核心函数
# 暴力求解一个条款的前提，在某个valuemap下是否为矛盾式
# 其背后的意义为：前提已经不可能满足，该条款只能进入Exp或者Vio
# 返回true则说明该逻辑表达式是矛盾式
def isContradiction(cnf, graph, index):
    postfix = [".Sat", ".Exp", ".Vio"]
    cond = list(graph.vertexList[index].condition)
    actions = list(graph.vertexList[index].action)
    valueMap = {}
    for id in cond:
        for t in range(len(postfix)):
            key = "Term" + id + postfix[t]
            value = graph.valueMap[key]
            valueMap[key] = value
    for act in actions:
        valueMap[act] = graph.valueMap[act]
    print("缩小后的valueMap:", valueMap)

    cnf_tmp = copy.deepcopy(cnf)
    isTrue = [False] * len(cond)

    for id in cond:
        flag = False
        for t in range(len(postfix)):
            key = "Term" + id + postfix[t]
            flag = flag or valueMap[key]
        isTrue[cond.index(id)] = flag
    rlt = not recursion(cnf_tmp, valueMap, isTrue, 0)
    print("reslutofiscontra:", rlt)
    return rlt


# 判断是不是永真式
def tautology(cnf, graph, index):
    postfix = [".Sat", ".Exp", ".Vio"]
    cond = list(graph.vertexList[index].condition)
    actions = list(graph.vertexList[index].action)
    valueMap = {}
    for id in cond:
        for t in range(len(postfix)):
            key = "Term" + id + postfix[t]
            value = graph.valueMap[key]
            valueMap[key] = value
    for act in actions:
        valueMap[act] = graph.valueMap[act]
    print("缩小后的valueMap:", valueMap)

    cnf_tmp = copy.deepcopy(cnf)
    isTrue = [False] * len(cond)

    for id in cond:
        flag = False
        for t in range(len(postfix)):
            key = "Term" + id + postfix[t]
            flag = flag or valueMap[key]
        isTrue[cond.index(id)] = flag
    rlt = not recursion(cnf_tmp, valueMap, isTrue, 0)
    rlt = recursion2(cnf_tmp, valueMap, isTrue, 0)
    print("tautologyresult:", rlt)
    return rlt


def DEC2Bin(dec):  # 将十进制转化为二进制
    result = ""
    if dec:
        result = DEC2Bin(dec // 2)
        return result + str(dec % 2)
    else:
        return result


# dealjudge  处理当judge出现并起到作用时的函数


# 核心函数
# 得到当前状态机下的的Bas的变化
def getBasChange(state, graph):
    stateNum = len(state)
    nextStates = []
    zeroslist = []
    for i in range(stateNum):
        tmp = []
        if state[i] == 2:
            tmp.append(3)
            # 如果动作人是contract，则取出Vio的变化
            if graph.vertexList[i].ContractFlag == False:
                tmp.append(5)
        if len(tmp) != 0:
            zeroslist.append(i)
        nextStates.append(tmp)
    return zeroslist, nextStates


# 得到pre-bas的独立条款
def getPostactChanges(state, graph):
    stateNum = len(state)
    zeroslist = []
    nextStates = []
    for i in range(stateNum):

        tmp = []
        if state[i] == 1:
            if graph.vertexList[i].ActionInPre == False:  # 当前提中不存在judge();

                if isContradiction(graph.vertexList[i].premise, graph, i) == True:  # 如果这个前提是矛盾式
                    graph.vertexList[i].iscontradiction = True
                    tmp.append(4)
                if tautology(graph.vertexList[i].premise, graph, i) == True:  # 如果这个前提式永真式
                    graph.vertexList[i].istautology = True
                    tmp.append(2)
            if graph.vertexList[i].ActionInPre == True:  # 当前提中存在judge
                length = len(graph.vertexList[i].action)
                length1 = 2 ** length
                flag3 = True
                flag4 = True
                for j in range(length1):
                    flag5 = False
                    flag6 = False
                    ll = ['0'] * length
                    for t in range(len(list(DEC2Bin(j)))):
                        ll.pop()
                    ll.extend(list(DEC2Bin(j)))
                    for k in range(length):
                        graph.valueMap[graph.vertexList[i].action[k]] = int(ll[k])
                    if isContradiction(graph.vertexList[i].premise, graph, i) == True:
                        flag5 = True
                        flag6 = False
                    elif tautology(graph.vertexList[i].premise, graph, i) == True:
                        flag6 = True
                        flag5 = False
                    flag3 = flag3 and flag5
                    flag4 = flag4 and flag6
                if flag3 == True:
                    graph.vertexList[i].iscontradiction = True
                    tmp.append(4)
                if flag4 == True:
                    graph.vertexList[i].istautology = True

                    tmp.append(2)
                elif flag3 == False and flag4 == False:
                    if graph.vertexList[i].flag == True:
                        tmp.append(2)
                        tmp.append(4)
        if len(tmp) != 0:
            zeroslist.append(i)
        nextStates.append(tmp)
    return zeroslist, nextStates


# 将json数据转换为python对象
def json2python(JsonData):
    # print("before decoding:")
    # print(JsonData)
    data = json.loads(JsonData)

    # print("after decoding:")
    # print(data)
    return data


# 将Transfer存放到外部文件中
def save_transfer(initState, transfers, contract_id):
    transfer_file = {'InitStatus': str(initState.astype(int).tolist()), "FsmArray": []}

    for i in range(0, len(transfers)):
        current_status = str(transfers[i].current.astype(int).tolist())
        new_status = str(transfers[i].newS.astype(int).tolist())
        action = str(transfers[i].action)
        t = {'CurrentStatus': str(current_status), 'Action': action, 'NewStatus': str(new_status)}
        # print(transfers)
        transfer_file['FsmArray'].append(t)
    with open('./fsm/' + contract_id, 'w') as fs:
        fs.write(json.dumps(transfer_file, indent=2))

    generateGo.transferGo('./fsm/' + contract_id, './code/' + contract_id)
    generateSol.transferSolidity('./fsm/' + contract_id, './code/' + contract_id)


# 对外接口
def create_fsm(contract, contract_id):
    initState, transfer, DFA = generate(contract)
    write_file = open('./MyWorkPlace/' + contract_id + '.pkl', 'wb')
    pickle.dump(DFA, write_file)
    write_file.close()
    save_transfer(initState, transfer, contract_id)


if __name__ == '__main__':
    data = input("jsonData")
    initState, transfer, DFA = generate(data)
    save_transfer(initState, transfer, "tmp")
    gametree.check(DFA, Tnode)
    # painting2(DFA)

