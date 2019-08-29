from Commitment import Commitment
import copy
import itertools
from Edges import *
# DGA节点的类结构
#各个成员变量的含义和例子
    # id Gnode 的id 具有唯一性 0 ,1 ,2 ,3 ,...
    # CMTs Commitment的列表 存储该节点所有的Commitment [cmt1,cmt2,...]
    #OutEdges Edge的列表 存储该节点所有的出边 [Edge1,Edge2,Edge3,...]
    #childrenId id的列表 存储该节点的所有的孩子节点的id [id1,id2,id3,...]
    #parentsId id的列表 存储该节点的所有的父亲节点的id [id1,id2,id3,...]
class GNode:
    Id = 0
    def __init__(self):
        GNode.Id = GNode.Id +1
        self._id = GNode.Id
        self._CMTs = []
        self._OutEdges = []
        self._childrenId = []
        self._parentsId = []
        self._type="GNode"
    # 初始化根节点
    # 输入commitment的数据json数组
        [{"time": "", "res": "", "person": "B TO A", "premise": ""},
         {"time": "", "res": "", "person": "B TO A", "premise": ""},...]
    # 改为静态方法
    def generateInitNode(self,jsondata):
        cmtNum = len(jsondata)         #查看Commitment的数量
        for i in range(cmtNum):        #依次生成Commitment
            id = "Term" + str(i+1)           #初始化Commitment的id
            # TODO Term id 前段传入
            tmp = jsondata[i]['person'].split(" ")  #查找Commitment的player
            player = tmp[0]
            resultAction = jsondata[i]['res']  #查找Commitment的结果动作
            premise = jsondata[i]['premise']   #查找Commitment的前提
            cmt = Commitment(id,player,resultAction)    #生成Commitment
            cmt.buildCommitment(premise,player)   #构建Commitment前提表达式,并且初始化Commitment
            self._CMTs.append(cmt) #将Commitment入队
    #判断该节点是否是接受状态
    #也就是叶子节点节点包含的Commitment的状态都是接受态则返回True,否则返回False
    def isLeafNode(self):
        flag = True      #设置标记
        for cmt in self._CMTs:
            if cmt.getStatus() <= 2: # 如果不是终态,则将flag置为False
                flag = False
        return flag
    def setCmts(self,ctms):       #设置节点的承诺列表
        self._CMTs = copy.deepcopy(ctms)
    def getCmt(self,cmtId): #根据commitment的id 返回指定的commitment
        for cmt in self._CMTs:
            if cmtId == cmt.getId():
                return cmt
    def getCmts(self):
        return self._CMTs
    def setCmtsFromDB(self,cmts):
        self._CMTs=cmts

    def getType(self):
        return self._type
    def setType(self,type):
        self._type=type

    def addOutEdge(self, edge): #添加节点的出边
        self._OutEdges.append(edge)
    def getOutEdge(self,childId):
        for ce in self._OutEdges:
            if childId == ce.getChildId():
                return  ce
    def removeOutEdge(self,childId):
        for ce in self._OutEdges:
            if childId == ce.getChildId():
                self._OutEdges.remove(ce)
                return
    def getOutEdges(self):   #获得该节点的所有出边
        return self._OutEdges
    def setOutEdges(self,edges):
        self._OutEdges=edges

    def addChildId(self, id): #TODO 去重
        if id not in self._childrenId:
            self._childrenId.append(id)
    def getChildrenId(self): #获取孩子节点的id
        return self._childrenId
    def setChildrenId(self,ids):
        self._childrenId=ids

    def addParentId(self,id):   #TODO
        if id not in self._parentsId:
            self._parentsId.append(id)
    def getParentsId(self):
        #print(self._parentsId)
        return self._parentsId
    def setParentsId(self,ids):
        self._parentsId=ids

    def getId(self):
        return self._id
    def setId(self,id):
        self._id=id

    def getStates(self):       #得到该节点所有的commitment的状态值
        states = []
        for cmt in self._CMTs:
            status = cmt.getStatus()
            states.append(status)
        return states
    def getStateSet(self):
        return [self.getStates()]

    def updateParentId(self,oldId,newId):    #更改父亲节点的id
        for i in range(len(self._parentsId)):
            if oldId == self._parentsId[i]:
                self._parentsId[i] = newId
    def updateChildId(self,oldId,newId):     #更改孩子节点id
        for i in range(len(self._childrenId)):
            if oldId == self._childrenId[i]:
                self._childrenId[i] = newId
    def getAllChanges(self):   #得到该节点所有的状态变化
        changeCmtId = []       #初始化可以变化的commitment的id
        nextStatus = []        #可以变化下一个状态
        for cmt in self._CMTs:
            tmp = []
            if cmt.getStatus() == 2:      #如果当前状态为2 则可以直接变
                tmp.append(3)
                if cmt.getContractFlag() == False:  #如果动作人不是Contract 则还可以变为5
                    #print("当操作人不是player",True)
                    tmp.append(5)
            if cmt.getStatus() == 1:

                if cmt.getPremise().containsAction() == False: #如果commitment的前提中不含有judge或action
                    if cmt.getPremise().isContradiction():  #如果前提为矛盾式 则直接变为4
                        tmp.append(4)

                    elif cmt.getPremise().isTautology():    #如果前提为永真式 则直接变为2
                        tmp.append(2)
                else:

                    if cmt.getPremise().isContradiction():  #如果前提为矛盾式 则直接变为4
                        tmp.append(4)


                    elif cmt.getPremise().isTautology():    #如果前提为永真式 则直接变为2
                        tmp.append(2)

                    else:
                        if cmt.getPremise().containsNonStoppedCMT() == False: #如果前提中所有以来的其他Commitment都达到终态

                            tmp.append(2)
                            tmp.append(4)
            if len(tmp) != 0:
                changeCmtId.append(cmt.getId())
                nextStatus.append(tmp)
        chaneList = self.combination(changeCmtId,nextStatus)
        return chaneList
    #步骤
        #1 产生孩子节点
        #2 生成相应的边
        #3 对孩子节点进行更新
    #Input
        #combinedChange 一组变化组合的字典 {Term1:2,Term2:3}
    #Output
        #child 孩子节点
    def createChild(self,combinedChange): #创建孩子节点
        #====================生孩子节点=====================
        child = GNode()  # 构建孩子节点
        child.setCmts(self._CMTs) #设置一下孩子节点的CMTs
        #====================生成边=====================
        edges = []  # 定义一条空边
        action = "("
        edges.append(Edge())  # 加入条空边
        for cmtId in combinedChange:  # 遍历变化的cmt
            val = combinedChange[cmtId]  # 查看该cmt的变化值
            cmt = child.getCmt(cmtId)  # 取得孩子节点中的cmt
            if val == 2 or val == 4:
                acts = cmt.getPremise().getActions()  # 从cnf返回action  #TODO cnf    (变化后的动作集会不会变化?????)
                if len(acts) > 0:
                    tlist, flist = cmt.getPremise().getAllModels()  # 得到符合的所有的动作的组合

                    models = tlist if val == 2 else flist  # 分两种情况
                    if len(models) > 0:
                        newedges = []
                        Act = ''
                        for edge in edges:
                            for model in models:
                                newedge = copy.deepcopy(edge)
                                for assign in model:
                                    start = assign.find('(') + 1
                                    end = assign.find(',')
                                    player = assign[start:end]

                                    actDesc = assign
                                    index = cmtId+cmtId
                                    Act = Act + player + assign + '|'
                                    event = Event(player,actDesc,index)
                                    newedge.addEvent(event)
                                newedges.append(newedge)
                        action = action + cmt.getId()+ Act+', '
                        edges = copy.deepcopy(newedges)
                        continue
            act = ""
            player = child.getCmt(cmtId).getPlayer()
            eventID = cmtId
            if val == 4 or val == 2:  # val为2或4 但是action为空
                act = act
            else:
                act = cmt.getAct()
                if val == 3:
                    act = "Sat" + act
                else:
                    act = "Vio" + act
            action = action + cmt.getId() + player + act + ', '
            event = Event(player, act, eventID)
            for e in edges:
                e.addEvent(event)
        #print("边集",len(edges))
        #print("combinedChange:",combinedChange)
        for changeId in combinedChange:
            cmt = child.getCmt(changeId)
            cmt.setStatus(combinedChange[changeId])  # 更新该Commitment的
        for cmt in child._CMTs:  # 遍历所有的commitment
            #print("before update:",cmt.toString(),cmt.getPremise().isContradiction(),cmt.getPremise().isTautology())
            cmt.updatePremise(combinedChange)            #TODO 应该只更改前提中包含combinedChange的commitment
            #print("after update:", cmt.toString(), cmt.getPremise().isContradiction(), cmt.getPremise().isTautology())
        outEdge = CompositeEdge(self._id,child.getId())
        for edge in edges:
            outEdge.appendEdge(edge)
        self._OutEdges.append(outEdge)
        self._childrenId.append(child.getId())

        action = action[:-2] + ')'
        return child ,action
    #以下为静态函数 合并复合边
    @staticmethod
    def combination(changeCmtId,nextStatus):

        Change = []
        for cmtId in changeCmtId:
            change = []
            for status in nextStatus[changeCmtId.index(cmtId)]:
                kv = []
                kv.append(cmtId)
                kv.append(status)
                change.append(kv)
            Change.append(change)
        changeList = []
        if len(Change) >= 1:
            for l in itertools.product(*Change):  # 形成笛卡尔积
                combinedChange = {}
                for i in range(len(l)):
                    combinedChange[l[i][0]] = l[i][1]
                changeList.append(combinedChange)
        return changeList
    def getnodeStrategies(self):     #TODO
        return A,B
    def getspecifiedCompositeEdges(self,id):    #
        return                             #得到指定孩子id的复合边

if __name__ == '__main__':
    comEdge1 = CompositeEdge()
    comEdge2 = CompositeEdge()
    event1 = Event('A',"二二","10")
    event2 = Event("B","C","11")
    event3 = Event('A',"二二","10")
    event4 = Event("B","C","11")
    event5 = Event('A',"二二","5")
    event6 = Event("B","C","11")
    event7 = Event('A',"二二","10")
    event8 = Event("B","C","11")
    edge1 = Edge()
    edge2 = Edge()
    edge3 = Edge()
    edge4 = Edge()
    edge2.addEvent(event1)
    edge2.addEvent(event2)
    print("edge2.toString(): ",edge2.toString())
    edge1.addEvent(event4)
    edge1.addEvent(event3)
    print("edge1.toString(): ",edge1.toString())
    edge3.addEvent(event5)
    edge3.addEvent(event6)
    print("edge3.toString(): ",edge3.toString())
    edge4.addEvent(event7)
    edge4.addEvent(event8)
    comEdge1.appendEdge(edge1)
    comEdge1.appendEdge(edge2)
    comEdge2.appendEdge(edge3)
    comEdge2.appendEdge(edge4)
    print("edge4.toString(): ",edge4.toString())
    print("comEdge1.toString(): ",comEdge1.toString())
    print("comEdge2.toString(): ", comEdge2.toString())
    comEdge1.mergeEdge(comEdge2)
    print("comEdge1.toString(): ",comEdge1.toString())