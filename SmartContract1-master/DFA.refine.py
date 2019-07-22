#关于
#CNF
#cmt 和 action 统称 contractLiteral， 每个contractLiteral 有唯一的ID。字符串，可以是目前的Term1 或 judge(A, pay），未来考虑换为整数

#对外接口，一律采用 contractLiteral ID
#内部实现，每个Literal 是整数，内外之间须有 map 保存映射关系
#CNF
def getClauseSet()
    # TODO 改为 iterator 形式更合理

    def build(premise)
        jsonPremise = formatToJson(premise)
        # 先将 raw string 形式 premise 转换为 JSON格式
        #  json 格式  , 比如 Term3: Term1.SAT||judge(A,pay)&&Term2.Vio||not judge(A,pay)  应转换为下面的格式
        # 注意，我估计judge 可能取非，比如  not judge(A,pay)  ，若不能取非，也不影响使用
        # {"Term3": [ { "Term1":"3" , "judge(A,pay):"1" }, { "Term2":"5" , "judge(A,pay)":"0" }]}
        # 说明，采用上面的格式，是保证CNF解析的contractLiteral ID与外部程序一致
        # 每个 {} 是一个 子句（clause），里面每一项 的 key 是 contractLiteral ID， value 为  3-5 （commitment）或 0/1 （judge ）
        # 最前面的 Term3 是本承诺的ID

    def setCMTStatus(cmtID, status)

    # 设置commitment的状态， status 取值 1-5，目前情况下调用此函数时status为3-5
    # 设置某commitment状态之后，该commitment对应的literal将从CNF中移除

    def isContradiction()  # 可通过eval来得到结果
    def isTautology()  # 可通过eval来得到结果
    def eval()  # return 1, 0, or 2(undecided)
    def getAllModels()  # 返回的结果形式待确定
    def getAllTFModels():
       # 返回所有使得CNF满足（T）或不满足（F）的model
       # 注意，调用此函数时，默认CNF中所有的commitment已进入终态
       # 返回结果形式，两个list，第一个list为T，第二个list为F
       # 形如T= [[judge(A,pay), !judge(B,mail)],[!judge(A,pay),judge(B,mail)]
    def containsAction():
    def getActions(): #返回cnf中存在所有action的id
        return
# DGA结构
class GNode:
    def __init__(self):
        self._id = 0
        self._CMTs = []  # 该节点对应的所有承诺，此列表内均为 Commitment 对象
        self._InEdges = []  # 该节点所有入边,此列表内均为 Edge 对象
        self._children = []  # 该节点所有的子节点，此列表内均为 GNode 对象
        self._state = []     #该节点的状态
        # 私有
    def getOutEdges(self):  # 得到该节点的出边

    def getInEdges(self):  # 得到该节点的所有入边

    def addInEdge(self, edge): #添加节点的入边

    def addChild(self, child): #添加孩子节点

    def getId(self):      #得到该节点的id

    def getChildren(self):  #得到所有的孩子节点

    def getPlayer(self):  # 得到该节点的动作人 player

    def getAction(self):  # 得到该节点的所有动作

    def getState(self):   #得到节点的状态 [1,1,2,2,1]

    def createChild(self,combinedChange): #创建孩子节点

    def getCmt(self,cmtId):  #得到指定承诺
    def getAllChanges(self):   #得到该节点所有的状态变化  TODO
        return []
    # 替代之前的嵌套列表
class Edge:
    def __init__(self):
        self._events = []  # 每个event包含 动作人，动作，序号 ，即 [actperson,act,index]
    def addEvent(self,event):     #往边里面添加事件
    def getLabel(self):          #得到该边上的label
    def setLabel(self,jsonLabel): #设置边上的lable
    def getSize(self)            # 得到Edge包含的events 数量
class Event:
    def __init__(self,player,actDesc,cmtId): # 初始化Events
class Commitment:
    def __init__(self):
        self._premise = CNF()  # 逻辑表达式
        self._id = title  # 条款的id
        self._status      #条款的状态值
        self._flag = False  # 前提中的承诺是否全部到达终态
        self._contractFlag = False  # 动作人是否是Contract
        self._action = []  # 前提中的judge()的总数
        self._judgeplayer = []
        self._condition = []  # 存储承诺前提里面含有的其他承诺号
        self._iscontradiction = False  # 是不是矛盾式
        self._istautology = False  # 判断是不是重言式

    def getContractFlag(self):

        return True
    def setStatus(self,status):   #设置状态
    def getPlayer(self):          #得到Commitment动作人
    def updatePremise(self,combineChange): # 更新前提 Input [[Term1：2], [Term2：3]]
    def getAct(self):            #得到Commitment的动作
    def buildPremise(self, premise):
        self.premise.build(premise)
        clauses = self.premise.getClauseSet()
        for cla in clauses:
            literals = cla.getLiterals()
            for lit in literals:
                if lit.isCMT():
                    if lit.getConLiteralID() not in self.condition:
                        self.condition.append(
                            lit.getConLiteralID())  # 注意condition 里面现在存入的是 Term1。 提醒：杜绝采用序号的方式，统一使用 contractLiteral ID
                else:
                    if lit.getConliteralID() not in self.action:
                        self.action.append(lit.getConLiteralID())  # 注意 action 里面现在存入的是  judge(A, pay)
                        self.judgeplayer.append(lit.getPlayer())
# TODO：在生成DGA时，每次生成一个子节点，都要根据状态的变化更改子节点中每个条款的premise
# TODO: 此函数应为 Node 的成员函数
# TODO  GNode 中应包含一组 commitment ， 每个 commitment 的内容应相应更新
# TODO  不需要 Graph 以及 GraphNode， GraphNode 实际就是 commitment
# 得到pre-bas的独立条款
def getAllChanges(self):
    for cmt in self.CMTs:
        tmp = []
        if cmt.status == 2:
            tmp.append(3)
            # 如果动作人是contract，则取出Vio的变化
            if cmt.getContractFlag() == False:
                 tmp.append(5)
        if cmt.status == 1:
            if cmt.containsAction() == False:
                if cmt.premise.isContradiction():    # TODO 需要判断CNF的真假
                    tmp.append(4)
                elif:
                    cmt.premise.isTautology():      #TODO 需要判断CNF的真假
                    tmp.append(2)
            else:
                # 当前提中存在action, 应先检查前提中所有的 commitment
                # 只有所有commitment均进入终态，该条款才进入post-act
                # 调用 cmt.premise.getAllModels(), 得到所有可以使premise为真的 组合，比如
                # [ [judge(A,pay), -judge(B,mail), judge(A,receive)], [-judge(A,pay), judge(B,mail),-judge(A,receive)]
                # 这里，每一项里面的 judge(A,pay)为 contractLiteral ID
                models = cmt.premise.getAllModels()
                maxNum = power(2, len(cmt.action)）
                if len(models) == 0:
                    temp.append(4)  # 若 modles 数量 == 0， 下一个状态只能为 4
                elsif
                len(models) < maxNum
                temp.append(2)  # 若 0< models 数量 < 2^ len(cmt.action), 下一个状态可以为2或4
                temp.append(4)
                else
                temp.append(2)  # 若 models 数量 == 2^ len(cmt.action), 下一个状态只能为 2
        if len(tmp) != 0:
            rlt.append(cmt.getID())
        nextStates.append(tmp)
return rlt, nextStates


# Node 的成员函数
# input  一组变化，形如 [[Term1：2], [Term2：3]]，注意采用承诺的 ID 而不是序号
# 注意一组变化可能产生多条复合边 Edge。且从当前节点出发，每条边均到达相同的子节点
# output 子节点
# 更新commitment 生成子节点 生成边
def createChild(self, combinedChange):
    child = GNode()      #构建孩子节点
    child._CMTs = self._CMTs.deep_copy() #拷贝父亲节点的CMTs
    # 生成边
    edges = []   #定义一条空边
    edges.append(Edge())     #加入条空边
    for cmtId in combinedChange:    #遍历变化的cmt
        val = combinedChange[cmtId] #查看该cmt的变化值
        cmt = child.getCmt(cmtId) # 取得孩子节点中的cmt
        if val == 2 or val == 4:
            acts = cmt.premise.getActions()#从Cnf返回action
            if len(acts) > 0:
                tlist, flist = cmt.premise.getAllTFModels()  #得到符合的所有的动作的组合
                models = tlist if val == 2 else flist      #分两种情况
                if len(models)>0:
                   newedges = []
                   for edge in edges:
                       for model in models:
                           newedge = edge.deep_copy()
                            for assign in model:
                                event = []    #TODO   assign[judge(A,1),!judge(B,2),...]
                                newedge.add(event)
                        newedges.append(newedge)
                edges = newedges.deep_copy()
                continue
        #处理不拆分边的情况
        act = ""
        player = cmt.getPlayer()
        eventID = cmtId
        if val == 4 or val == 2:     #val为2或4 但是action为空
            act = ""
        else:
            act = cmt.getAct()
            if val == 3:
                act = "Sat" + act
            else:
                act = "Vio" + act

        event = Event(player,act,cmtId)
        for e in edges:
            e.addEvent(event)
    # 将edges写入到child 中
    child._InEdges.extend(edges)
    for cmt in child._CMTs:  # 遍历所有的commitment
        if cmt.getID() in combinedChange:  # 如果Commitment发生了变化
            cmt.setStatus(combinedChange[cmt.getID()])  # 更新该Commitment的
        cmt.updatePremise(combinedChange)
    return child


# 核心函数
# 状态机生成算法，BFS
def generate(inputdata):
    jsondata = json2python(inputdata)
    # 初始化根节点
    n0 = generateInitNode(jsondata)
    # 广度优先搜索（队列辅助实现），寻找所有合理的状态机节点
    queue = []
    queue.append(n0)
# BFS
    while len(queue) > 0:
        node = queue.pop(0)
        # 直接复制，防止浅拷贝错误
        state = node.getState()
        #函数内部的函数
        if isFinalState(state):
            continue
        # 如果不是终态 则查找所有的独立条款及其组合
        changeList = node.getAllChanges()  # 计算所有独立的变化   序号变id  {[[Term1,2],[Term2,3]],...}
        for combinedChange in changeList:  # 每个变化的组合对应一条边
            chd = node.createChild(combinedChange)  # 根据父节点和复合边，生成子节点。生成过程中，更新子节点各承诺的premise
            node.addChild(chd)
            queue.append(chd)
    return n0