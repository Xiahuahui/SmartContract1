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


# 和博弈树对接定义的接口
# edge格式 - { ( [pid], [ [action_person, action], ... ] ), ...  }
class GNode:
    def __init__(self):
        self.id = 0
        self.data = []
        self.edge = []
        self.children = []

    # 不重复的添加edge
    def addEdge(self, edge):
        for i in range(len(self.edge)):
            if self.edge[i] == edge:
                return
        self.edge.append(edge)

    # 不重复的添加该节点的孩子节点
    def addChild(self, child):
        for i in range(len(self.children)):
            if self.children[i] == child:
                return
        self.children.append(child)

    def getId(self):
        return self.id

    def getchildren(self):
        return self.children


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
        self.condiction = []  # 存储承诺前提里面含有的其他承诺号
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
                print("action:" + clause[t])
                if clause[t] not in self.action:
                    self.action.append(clause[t])
                self.ActionInPre = True
            if "Term" in clause[t]:
                number = clause[t][4]
                if number not in self.condiction:
                    self.condiction.append(number)
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
    print(actionList)
    # =======================Step 1================================
    # initial state - 1*n vector
    initState = np.ones(StateNum)  # .astype(int)
    for i in range(StateNum):
        # no dependence with others
        if jsondata[i]['premise'] == None or jsondata[i]['premise'] == "":
            initState[i] = 2
    print("initial state:", initState)

    # =======================Step 2================================
    # 根据前提构建有向无环图
    graph = BuildGraph(jsondata, StateNum, actperson)
    for k in range(StateNum):
        if initState[k] == 2:
            graph.vertexList[k].flag = True
    print("matrix:")
    print(graph.matrix)
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
    while len(queue):
        # input("按任意键继续")
        st = queue.pop(0)
        # 直接复制，防止浅拷贝错误
        state = st.state.copy()
        graph = copy.deepcopy(st.graph)

        print("####################################################")
        print("current state:")
        print(state)

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
        # 如果该节点中含有1且前提已经满足
        # =======================Step 3.2.1================================
        if concontainsactissat(state, graph, graph.valueMap) == True:
            uclist1 = makeactchange(state, graph, graph.valueMap)  # 得到状态为pre-bas的独立状态
            if len(uclist1) == 0:
                print("[fatal_error] func makeactchange return nil! check logic")
                continue
            print(uclist1)
            # =======================Step 3.3.1================================
            # 生成新的状态
            # class Gnode:
            #     currentState - self.data
            #     edge - { ([pid], [ [person, action], ... ] ), ...  } - self.edge
            #     child - self.children
            # for i in range(len(uclist1)):
            # 必须使用for in循环
            # 在遍历uclist1中会产生新的分支——外部action导致
            for val in uclist1:
                # id = id + 1
                i = uclist1.index(val)
                newState = st.state.copy()
                newGraph = copy.deepcopy(graph)
                action = "(  "
                currentAction = []
                for t in range(len(uclist1[i])):
                    index = uclist1[i][t][0]
                    change = uclist1[i][t][1]
                    newState[index] = change
                    if newGraph.vertexList[index].ActionInPre == False:
                        continue
                    if newGraph.vertexList[index].ActionInPre == True:
                        if newGraph.vertexList[index].iscontradiction == True:
                            continue
                        if newGraph.vertexList[index].istautology == True:
                            continue
                        if newGraph.vertexList[index].iscontradiction == False and newGraph.vertexList[
                            index].istautology == False:
                            if newGraph.vertexList[index].flag == True:
                                if change == 2:
                                    action = action + getDGAEdge(actionList, index, chmap[change]) + ', '
                                    currentAction.append([actperson[index], chmap[change], index])
                                if change == 4:
                                    action = action + getDGAEdge(actionList, index, chmap[change]) + "judge()" + ', '
                                    currentAction.append([actperson[index], chmap[change], index])
                action = action[:-2] + ')'
                newGraph = updateGraph(newGraph, newState)
                # 与gametree对接
                gnodelist, pnode, id = findGnode(gnodelist, state, id)
                gnodelist, cnode, id = findGnode(gnodelist, newState, id)
                pid = pnode.getId()
                edge = [[pid], currentAction]
                pnode.addChild(cnode)
                cnode.addEdge(edge)

                # 生成状态机文件
                newSt = St_node(id, newState, newGraph)
                queue.append(newSt)
                tran = Transfer(state, action, newState)
                transfer.append(tran)
            continue

        # =======================Step 3.2.2================================
        # 得到不相关承诺集合的变化组合
        uclist2 = getUcList(state, graph, graph.valueMap)

        # 严重错误，不应该出现
        if len(uclist2) == 0:
            print("[fatal_error] func getUncorrelated return nil! check logic")
            continue
        print(uclist2)
        # =======================Step 3.3.2================================
        # 生成新的状态
        # class Gnode:
        #     currentState - self.data
        #     edge - { ([pid], [ [person, action], ... ] ), ...  } - self.edge
        #     child - self.children
        # for i in range(len(uclist2)):
        # 必须使用for in循环
        # 在遍历uclist2中会产生新的分支——外部action导致
        for val in uclist2:
            # id = id + 1
            i = uclist2.index(val)
            newState = st.state.copy()
            newGraph = copy.deepcopy(graph)
            action = "("
            currentAction = []
            for t in range(len(uclist2[i])):
                index = uclist2[i][t][0]
                change = uclist2[i][t][1]
                newState[index] = change
                action = action + getDGAEdge(actionList, index, chmap[change]) + ', '
                currentAction.append([actperson[index], chmap[change], index])
            action = action[:-2] + ')'
            newGraph = updateGraph(newGraph, newState)
            # 与gametree对接
            gnodelist, pnode, id = findGnode(gnodelist, state, id)
            gnodelist, cnode, id = findGnode(gnodelist, newState, id)
            pid = pnode.getId()
            edge = [[pid], currentAction]
            pnode.addChild(cnode)
            cnode.addEdge(edge)

            # 生成状态机文件
            newSt = St_node(id, newState, newGraph)
            queue.append(newSt)
            tran = Transfer(state, action, newState)
            transfer.append(tran)

    # 输出传给game tree的状态机
    # 主要观察：
    # 1. 结构是否正确
    # 2. 有无重复
    # for i in range(len(gnodelist)):
    #         print(gnodelist[i], " id: ",gnodelist[i].id, " Gnodestate: ", gnodelist[i].data, " edge:",gnodelist[i].edge, " child:", gnodelist[i].children)
    return (initState, transfer, gnodelist[0])


# 辅助函数
# 状态机边生成，生成包含动作的边
def getDGAEdge(ActionList, index, edge):
    if edge == "Sat":
        return "Term" + str(index) + ": execute " + ActionList[index] + ' '
    if edge == "Vio":
        return "Term" + str(index) + ": Violate " + ActionList[index] + ' '
    if edge == "Exp":
        return "Term" + str(index) + ": timeout "
    if edge == "Bas":
        return "Term" + str(index) + ": execute judge()"


# 辅助函数
# 朴素算法判断两个list是否相同
def isequle(list1, list2):
    n = len(list1)
    for i in range(n):
        if list1[i] != list2[i]:
            return False
    return True


# 遍历一个列表中，寻找state_np的节点
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
        for k in range(len(graph.vertexList[j].condiction)):
            flag2 = False
            for t in range(len(postfix)):
                key = "Term" + str(graph.vertexList[j].condiction[k]) + postfix[t]
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
        print("commitment premise: ", premise)
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
    return res


def recursion2(cnf, valueMap, TermFlag, index):
    print("序号2", index)
    if index == len(TermFlag):
        print(cnf.getValue(valueMap))
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
    return res


# 核心函数
# 暴力求解一个条款的前提，在某个valuemap下是否为矛盾式
# 其背后的意义为：前提已经不可能满足，该条款只能进入Exp或者Vio
# 返回true则说明该逻辑表达式是矛盾式
def isContradiction(cnf, valueMap, stateNum):
    postfix = [".Sat", ".Exp", ".Vio"]
    cnf_tmp = copy.deepcopy(cnf)
    isTrue = [False] * stateNum

    for i in range(stateNum):
        flag = False
        for t in range(len(postfix)):
            key = "Term" + str(i + 1) + postfix[t]
            flag = flag or valueMap[key]
        isTrue[i] = flag
    return not recursion(cnf_tmp, valueMap, isTrue, 0)


# 判断是不是永真式
def tautology(cnf, valueMap, stateNum):
    postfix = [".Sat", ".Exp", ".Vio"]
    cnf_tmp = copy.deepcopy(cnf)
    isTrue = [False] * stateNum

    for i in range(stateNum):
        flag = False
        for t in range(len(postfix)):
            key = "Term" + str(i + 1) + postfix[t]
            flag = flag or valueMap[key]
        isTrue[i] = flag
    return recursion2(cnf_tmp, valueMap, isTrue, 0)


def DEC2Bin(dec):  # 将十进制转化为二进制
    result = ""
    if dec:
        result = DEC2Bin(dec // 2)
        return result + str(dec % 2)
    else:
        return result


# 核心函数
# 得到当前状态机下的极大独立条款集合
def getUcList(state, graph, valueMap):
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
    currentChange = []
    for index in zeroslist:
        currentChange.append(nextStates[index])
    # combination
    res = []
    tmp = []
    res = combination(res, 0, tmp, currentChange, zeroslist)
    return res


# 当前状态之中是否存在prebas的状态
def concontainsactissat(state, graph, valueMap):
    stateNum = len(state)
    zeroslist = []
    flag5 = False  # 判断当下状态有没有pre-bas 若有则返回为真   否则返回为假
    for i in range(stateNum):
        tmp = []
        if state[i] == 1:
            if graph.vertexList[i].ActionInPre == False:
                if isContradiction(graph.vertexList[i].premise, valueMap, stateNum) == True:
                    tmp.append(4)
                if tautology(graph.vertexList[i].premise, valueMap, stateNum) == True:
                    tmp.append(2)
            if graph.vertexList[i].ActionInPre == True:
                length = len(graph.vertexList[i].action)
                length1 = 2 ** length
                flag3 = True
                flag4 = True
                for j in range(length1):
                    ll = ['0'] * length
                    for t in range(len(list(DEC2Bin(j)))):
                        ll.pop()
                    ll.extend(list(DEC2Bin(j)))
                    for k in range(length):
                        graph.valueMap[graph.vertexList[i].action[k]] = int(ll[k])
                        flag3 = flag3 and isContradiction(graph.vertexList[i].premise, valueMap, stateNum)
                        flag4 = flag4 and tautology(graph.vertexList[i].premise, valueMap, stateNum)
                if flag3 == True:  # 如果在有前提的情况下已经为矛盾式
                    graph.vertexList[i].iscontradiction = True
                    tmp.append(4)
                if flag4 == True:  # 如果在有前提的情况下以为永真式
                    graph.vertexList[i].istautology = True
                    tmp.append(2)
                elif flag3 == False and flag4 == False:
                    if graph.vertexList[i].flag == True:
                        tmp.append(2)
                        tmp.append(4)
        if len(tmp) != 0:
            zeroslist.append(i)
    if len(zeroslist) != 0:
        flag5 = True
    return flag5


# 得到pre-bas的独立条款
def makeactchange(state, graph, valueMap):
    stateNum = len(state)
    zeroslist = []
    nextStates = []
    for i in range(stateNum):
        tmp = []
        if state[i] == 1:
            if graph.vertexList[i].ActionInPre == False:  # 当前提中不存在judge();
                if isContradiction(graph.vertexList[i].premise, valueMap, stateNum) == True:  # 如果这个前提是矛盾式
                    tmp.append(4)
                if tautology(graph.vertexList[i].premise, valueMap, stateNum) == True:  # 如果这个前提式永真式
                    print("序号", i)
                    tmp.append(2)
            if graph.vertexList[i].ActionInPre == True:  # 当前提中存在judge
                length = len(graph.vertexList[i].action)
                length1 = 2 ** length
                flag3 = True
                flag4 = True
                for j in range(length1):
                    ll = ['0'] * length
                    for t in range(len(list(DEC2Bin(j)))):
                        ll.pop()
                    ll.extend(list(DEC2Bin(j)))
                    for k in range(length):
                        graph.valueMap[graph.vertexList[i].action[k]] = int(ll[k])
                        flag3 = flag3 and isContradiction(graph.vertexList[i].premise, valueMap, stateNum)
                        flag4 = flag4 and tautology(graph.vertexList[i].premise, valueMap, stateNum)
                if flag3 == True:
                    graph.vertexList[i].iscontradiction = True
                    tmp.append(4)
                if flag4 == True:
                    graph.vertexList[i].istautology = True
                    print(state, i)
                    tmp.append(2)
                elif flag3 == False and flag4 == False:
                    if graph.vertexList[i].flag == True:
                        tmp.append(2)
                        tmp.append(4)
        if len(tmp) != 0:
            zeroslist.append(i)
        nextStates.append(tmp)
    currentChange = []
    for index in zeroslist:
        currentChange.append(nextStates[index])
    # combination
    res = []
    tmp = []
    res = combination(res, 0, tmp, currentChange, zeroslist)
    return res

    # 辅助函数


# 将json数据转换为python对象
def json2python(JsonData):
    print("before decoding:")
    print(JsonData)
    data = json.loads(JsonData)

    print("after decoding:")
    print(data)
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
    save_transfer(initState, transfer, contract_id)
    return DFA


if __name__ == '__main__':
    data = input("jsonData")
    initState, transfer, DFA = generate(data)
    save_transfer(initState, transfer, "tmp")
    gametree.check(DFA, Tnode)
    # painting2(DFA)
