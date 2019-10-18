import pickle
from Choices import *
import time
import copy
import itertools
from GNode import *
from NodeRepository import nodeRepository
from Settings import settings
from Edges import *
from Payoff import *
class Strategy:
    def __init__(self,player):
        self._player = player
        self._choices = []
    def addChoice(self,choice):
        self._choices.append(choice)
    def toString(self):
        rlt = ""
        sortedList = sorted(self._choices, key=lambda c: c.getNodeID())
        for choice in sortedList:
            rlt = rlt + choice.toString()
        return rlt
    def contain(self,choiceSet):
        flag1 = True
        for outChoice in choiceSet:
            flag2 = False
            for inChoice in self._choices:
                if inChoice.equal(outChoice) :
                    flag2 = True
                    break
            flag1 = flag1 and flag2
        return flag1

    @staticmethod
    def buildStrategies(player, choiceGroupList):
        straSet = []
        for l in itertools.product(*(choiceGroupList)):              #形成笛卡尔积
            stra = Strategy(player)
            stra._choices.extend(l)
            straSet.append(stra)
        return straSet

    @staticmethod
    def buildreducedStrategies(player, choiceCombinationList):
        straSet = []
        for cComb in  choiceCombinationList:
            stra = Strategy(player)
            stra._choices.extend(cComb.getChoices())
            straSet.append(stra)
        return straSet
def createStrategies(root):
    queue = []
    mapping = {}
    queue.append(root)
    mapping[str(root.getId())] = ""
    wholeChoicesA = []
    wholeChoicesB = []
    while len(queue) > 0:
        node = queue.pop()
        nodeChoicesA = []
        nodeChoicesB = []
        for ce in node.getOutEdges():
            choiceA,choiceB = ce.getAllChoices()
            if settings.DEBUG:
                print("ChoiceA.toString():  ",choiceA.toString())
                print("ChoiceB.toString():   ",choiceB.toString())
            if choiceA.isEmpty() == False:
                nodeChoicesA.append(choiceA)
            if choiceB.isEmpty() == False:
                nodeChoicesB.append(choiceB)

        nodeChoicesA = Choice.removeDupChoices(nodeChoicesA)
        nodeChoicesB = Choice.removeDupChoices(nodeChoicesB)

        if len(nodeChoicesA) != 0:
            wholeChoicesA.append(nodeChoicesA)
        if len(nodeChoicesB) != 0:
            wholeChoicesB.append(nodeChoicesB)

        children = nodeRepository.loadNodes(node.getChildrenId())
        for child in children:
            if str(child.getId()) not in mapping:
                mapping[str(child.getId())] = ""
                queue.append(child)
    if settings.DEBUG:
        print("wholeChoicesA: ", len(wholeChoicesA))
        I = 1
        for choiceGroup in wholeChoicesA:
            print("当前节点参与人B的策略数:  ",len(choiceGroup))
            I = I * len(choiceGroup)
        print("参与人A的策略数:  ",I)
        J = 1
        print("wholeChoicesB: ", len(wholeChoicesB))
        for choiceGroup in wholeChoicesB:
            print("当前节点参与人B的策略数:  ",len(choiceGroup))
            J = J * len(choiceGroup)
        print("参与人B的策略数:  ",J)
    # straSetA = []
    # straSetB = []
    straSetA = Strategy.buildStrategies("A", wholeChoicesA)
    print("完毕")
    straSetB = Strategy.buildStrategies("B", wholeChoicesB)

    if settings.DEBUG:
        print("strategies of player A:")
        for stra in straSetA:
            print(stra.toString())
        print ("strategies of player B:")
        for stra in straSetB:
            print(stra.toString())
    if settings.DEBUG:
        print("A的策略数: ",len(straSetA))
        print("B的策略数: ",len(straSetB))

    return straSetA, straSetB
# 判断有向图中两个节点之间是否存在路径(广度优先)
    #startNode   起始节点
    #endNode     结束节点
# 返回一个布尔值   若存在则返回True
                #若不存在则返回False
def getAncestor(node,ancestor):
    parents = nodeRepository.loadNodes(node.getParentsId())  # 直接取得是策略
    ancestors = []
    if len(parents) == 0:  # 如果是叶子节点,则直接返回 @path
        ancestors.append(ancestor)
        return ancestors
    else:
        for parent in parents:  # 如果不是叶子节点   则在原来的策略上加上一条边
            newancestor = copy.deepcopy(ancestor)
            parentId = parent.getId()
            newancestor.append(parentId)
            ancestors.extend(getAncestor(parent, newancestor))
        return ancestors
def getAllnodeAncestor(root):
    queue = []
    mapping = {}
    queue.append(root)
    mapping[str(root.getId())] = ""
    ancestorMapping = {}
    starttime = time.time()
    T = 0
    while len(queue) > 0:
        node = queue.pop(0)
        T = T + 1
        if T % 10 == 0:
            endtime = time.time()
            print("遍历10个的时间: ", endtime - starttime)
            starttime = endtime
        ancestorMapping[str(node.getId())] = getAncestor(node ,[node.getId()])
        for child in nodeRepository.loadNodes(node.getChildrenId()):
            if str(child.getId()) not in mapping:
                mapping[str(child.getId())] = ""
                queue.append(child)
    return ancestorMapping
def iskeyancestor(startNode,endNode):
    ancestors = ChoiceCombination.ancestorMapping[str(endNode.getId())]
    for a in ancestors:
        if str(startNode.getId()) not in a:
            return False
    return True
def childNodesMapping(root):
    Queue = []
    mapping = {}
    Queue.append(root)
    mapping[str(root.getId())] = ""
    childNodesMapping = {}
    starttime = time.time()
    T = 0
    while len(Queue) > 0:
        node = Queue.pop(0)
        T = T + 1
        if T % 10 == 0:
            endtime = time.time()
            print("遍历10个的时间: " ,endtime - starttime)
            starttime = endtime
        childNodesMapping[str(node.getId())] = childNodes(node)
        for child in nodeRepository.loadNodes(node.getChildrenId()):
            if str(child.getId()) not in mapping:
                mapping[str(child.getId())] = ""
                Queue.append(child)
    return childNodesMapping
def childNodes(startNode):
    queue = []
    mapping = {}
    queue.append(startNode)
    mapping[str(startNode.getId())] = ""
    while len(queue) > 0:
        node = queue.pop(0)
        for child in nodeRepository.loadNodes(node.getChildrenId()):
            if str(child.getId()) not in mapping:
                mapping[str(child.getId())] = ""
                queue.append(child)
    return mapping
def existPath(startNode,endNode):
    if str(endNode.getId()) in ChoiceCombination.childNodesMapping[str(startNode.getId())]:
        return True
    else:
        return False

#定义其中一种策略的组合:
class ChoiceCombination:
    childNodesMapping = ""
    ancestorMapping = ""
    def __init__(self):
        self._choices=[]
        self._Id = {}
    def addChoice(self,choice,inId,outId):
        self._choices.append(choice)
        if str(inId) not in self._Id:
            self._Id[str(inId)] = list(outId)
        else:
            print("已经出错")
            self._Id[str(inId)].extend(outId)
    #判断当前策略是否该与这个策略组合做笛卡尔积
       # 在策略组合中若存在一个不需要笛卡尔积的情况,则不需要做
    def needChoice(self,nodeChoice,ExistPath ,Iskeyancestor):
        choiceParentnode = nodeRepository.getnode(nodeChoice.getChoice().getNodeID())    #该选择的父亲节点
        choiceChildIds = nodeChoice.getOutId()   #该选择的孩子节点的ids
        for c in self._choices:
            cParentnode = nodeRepository.getnode(c.getNodeID())
            flag0 = False
            for cChildId in self._Id[str(c.getNodeID())]:
                cChildnode = nodeRepository.getnode(int(cChildId))
                flag1 = True
                key1 = str(c.getNodeID())+"#"+str(nodeChoice.getChoice().getNodeID())
                key2 = str(cChildId)+"*"+str(nodeChoice.getChoice().getNodeID())
                if key1 in Iskeyancestor:
                    T1 = Iskeyancestor[key1]
                else:

                    Iskeyancestor[key1] = iskeyancestor(cParentnode, choiceParentnode)
                    T1 = Iskeyancestor[key1]
                if key2 in ExistPath:
                    T2 = ExistPath[key2]
                else:

                    ExistPath[key2] = (existPath(cChildnode, choiceParentnode) == False)
                    T2 = ExistPath[key2]
                if T1 and T2 :
                    flag1 = False
                flag0 = flag0 or flag1
            if flag0 == False:
                return False,Iskeyancestor,ExistPath

            flag2 = False
            for choiceChildId in choiceChildIds:
                choiceChildnode = nodeRepository.getnode(int(choiceChildId))
                flag3 = True
                key1 = str(nodeChoice.getChoice().getNodeID()) + "#" + str(c.getNodeID())
                key2 = str(choiceChildId) + "*" + str(c.getNodeID())
                if key1 in Iskeyancestor:
                    T1 = Iskeyancestor[key1]
                else:
                    Iskeyancestor[key1] = iskeyancestor(choiceParentnode,cParentnode)
                    T1 = Iskeyancestor[key1]
                if key2 in ExistPath:
                    T2 = ExistPath[key2]
                else:
                    ExistPath[key2] = (existPath(choiceChildnode,cParentnode) == False)
                    T2 = ExistPath[key2]
                if T1 and T2:
                    flag3 = False
                flag2 = flag2 or flag3
            if flag2 == False:
                return False,Iskeyancestor,ExistPath
        return True ,Iskeyancestor,ExistPath
    def getChoices(self):
        return self._choices
    def toString(self):
        rlt = ""
        sortedList = sorted(self._choices, key=lambda c: c.getNodeID())
        for choice in sortedList:
            rlt = rlt + choice.toString()
        return rlt
class NodeChoice:
    def __init__(self,choice):
        self._choice = choice
        self._outId = {}
    def setOutId(self,outId):
        if str(outId) not in self._outId:
            self._outId[str(outId)] = ""
    def getChoice(self):
        return self._choice
    def getChoiceId(self):
        return list(self._outId.keys())[0]
    def getOutId(self):
        return list(self._outId.keys())
    def toString(self):
        return self._choice.toString()
    @staticmethod
    def removeDupChoices(choices):
        myMap = {}
        rlt = []
        for c in choices:
            if c.getChoice().toString() not in myMap:
                myMap[c.getChoice().toString()] = c
                rlt.append(c)
            else:
                nodeChoice = myMap[c.getChoice().toString()]
                nodeChoice.setOutId(int(c.getChoiceId()))
        return rlt
def updatenewChoices(newChoices,choices,nodeChoices,node,ChoicesFlag,ExistPath ,Iskeyancestor):
    if len(choices) == 0:
        for nodeChoice in nodeChoices:
            cComb = ChoiceCombination()
            cComb.addChoice(nodeChoice.getChoice(), node.getId(), nodeChoice.getOutId())
            newChoices.append(cComb)
    else:
        T = 0
        for cCombation in choices:
            for nodeChoice in nodeChoices:
                flag,Iskeyancestor,ExistPath= cCombation.needChoice(nodeChoice,  ExistPath, Iskeyancestor)
                if flag:
                    if str(T) in ChoicesFlag:
                        del ChoicesFlag[str(T)]
                    newcComb = copy.deepcopy(cCombation)
                    newcComb.addChoice(nodeChoice.getChoice(), node.getId(), nodeChoice.getOutId())
                    newChoices.append(newcComb)
            T = T + 1
    return newChoices,Iskeyancestor,ExistPath
def updateChoices(choices,newChoices,ChoicesFlag):
    if len(newChoices) != 0:
        tmp = []
        for key in ChoicesFlag:
            tmp.append(choices[int(key)])
        tmp.extend(newChoices)
        choices = list(tmp)
        ChoicesFlag = {}
        for i in range(len(choices)):
            ChoicesFlag[str(i)] = ""
    return  choices , ChoicesFlag
def reduceStrategies(root):
    print("当前含有的节点: ",nodeRepository.printl())
    starttime0 = time.time()
    print("开始")
    childNodeMapping = childNodesMapping(root)
    mydb = open('dbase', 'wb')
    pickle.dump(childNodeMapping, mydb)
    endtime0 = time.time()
    print("结束",endtime0 - starttime0)
    ancestorMapping = getAllnodeAncestor(root)
    mydb2 = open('dbase2', 'wb')
    pickle.dump(ancestorMapping, mydb2)
    endtime1 = time.time()
    print("结束2",endtime1 -endtime0)
    ExistPath = {}
    Iskeyancestor = {}
    mydb = open('dbase', 'rb')
    childNodeMapping = pickle.load(mydb)
    mydb2 = open('dbase2', 'rb')
    ancestorMapping = pickle.load(mydb2)
    print("祖先集合: ",ancestorMapping)
    for key in ancestorMapping:
        T = 0
        for ancestor in ancestorMapping[key]:
            length = len(ancestor)
            a = [str(j) for j in ancestor]
            b = [""]*length
            c = zip(a, b)
            ancestorMapping[key][T] = dict(c)
            T = T + 1
    print("改进的祖先集合: ", ancestorMapping)
    ChoiceCombination.ancestorMapping = ancestorMapping
    ChoiceCombination.childNodesMapping = childNodeMapping
    queue = []
    mapping = {}
    queue.append(root)
    mapping[str(root.getId())] = ""
    ChoicesA = []                  #存储所有已生成的策略的组合
    ChoicesAFlag = {}              #标记字典用于更新ChoicesA
    ChoicesB = []
    ChoicesBFlag = {}
    TT = 0
    starttime = time.time()
    while len(queue) > 0:
        node = queue.pop(0)
        print("当前节点的状态:",node.getStates())
        TT = TT +1
        print("处理过的节点个数: ",TT)
        endtime = time.time()
        print("处理这个结点耗时:", endtime - starttime)
        starttime = endtime
        newChoicesA = []
        newChoicesB = []
        nodeChoicesA = []
        nodeChoicesB = []
        for ce in node.getOutEdges():
            choiceA, choiceB = ce.getAllChoices()
            if choiceA.isEmpty() == False:
                nodeChoiceA = NodeChoice(choiceA)
                nodeChoiceA.setOutId(ce.getChildId())
                nodeChoicesA.append(nodeChoiceA)
            if choiceB.isEmpty() == False:
                nodeChoiceB = NodeChoice(choiceB)
                nodeChoiceB.setOutId(ce.getChildId())
                nodeChoicesB.append(nodeChoiceB)
        nodeChoicesA = NodeChoice.removeDupChoices(nodeChoicesA)
        nodeChoicesB = NodeChoice.removeDupChoices(nodeChoicesB)
        newChoicesA,Iskeyancestor,ExistPath = updatenewChoices(newChoicesA,ChoicesA,nodeChoicesA,node,ChoicesAFlag,ExistPath ,Iskeyancestor)
        newChoicesB,Iskeyancestor,ExistPath = updatenewChoices(newChoicesB,ChoicesB,nodeChoicesB,node,ChoicesBFlag,ExistPath ,Iskeyancestor)
        ChoicesA ,ChoicesAFlag = updateChoices(ChoicesA,newChoicesA,ChoicesAFlag)
        ChoicesB ,ChoicesBFlag = updateChoices(ChoicesB,newChoicesB,ChoicesBFlag)
        if settings.DEBUG :
            print("A当前的策略组合: ")
            for cComb in ChoicesA:
                print(cComb.toString())
            print("B当前的策略组合: ")
            for cComb in ChoicesB:
                print(cComb.toString())
            print("ChoicesA的长度",len(ChoicesA))
            print("ChoicesB的长度", len(ChoicesB))
        children = nodeRepository.loadNodes(node.getChildrenId())
        for child in children:
            if str(child.getId()) not in mapping:
                mapping[str(child.getId())] = ""
                queue.append(child)
    straSetA = Strategy.buildreducedStrategies("A", ChoicesA)
    straSetB = Strategy.buildreducedStrategies("B", ChoicesB)
    return straSetA, straSetB
if __name__ == '__main__':
    mydb3 = open('dbase3', 'rb')
    Nodes = pickle.load(mydb3)
    mydb4 = open('dbase4', 'rb')
    leavesUtil = pickle.load(mydb4)
    for node in Nodes:
        print(node.getId())
    nodeRepository.initRepository(Nodes)
    root = nodeRepository.getnode(1)
    C,D = reduceStrategies(root)
    createPayoffMatrix(C, D, root, leavesUtil)
