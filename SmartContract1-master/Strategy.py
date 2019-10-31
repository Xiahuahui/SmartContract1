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
#定义其中一种策略的组合:
class ChoiceCombination:
    childNodesMapping = ""
    ancestorMapping = ""
    def __init__(self):
        self._choicesIds=[]
        self._choicesNodeIds = {}
    def addChoice(self,choice):
        self._choicesIds.append(choice.getId())
        if str(choice.getNodeID()) not in self._choicesNodeIds:
            self._choicesNodeIds[str(choice.getNodeID())] = choice.getId()
        else:
            print("已经出错")
    #判断当前策略是否该与这个策略组合做笛卡尔积
       # 在策略组合中若存在一个不需要笛卡尔积的情况,则不需要做
    def needChoice(self,nodeChoice,ExistPath ,Iskeyancestor):
        choiceSourcenode = nodeRepository.getnode(nodeChoice.getNodeID())    #该选择的父亲节点
        choiceDestinationIds = nodeChoice.getOutId()   #该选择的孩子节点的ids
        for c in nodeRepository.loadChoices(self._choicesIds):
            cSourcenode = nodeRepository.getnode(c.getNodeID())
            flag0 = False
            for cDestinationId in c.getOutId():
                cDestinationnode = nodeRepository.getnode(int(cDestinationId))
                flag1 = True
                key1 = str(c.getNodeID())+"#"+str(nodeChoice.getNodeID())
                key2 = str(cDestinationId)+"*"+str(nodeChoice.getNodeID())
                if key1 in Iskeyancestor:
                    T1 = Iskeyancestor[key1]
                else:

                    Iskeyancestor[key1] = iskeyancestor(cSourcenode, choiceSourcenode)
                    T1 = Iskeyancestor[key1]
                if key2 in ExistPath:
                    T2 = ExistPath[key2]
                else:

                    ExistPath[key2] = (existPath(cDestinationnode, choiceSourcenode) == False)
                    T2 = ExistPath[key2]
                if T1 and T2 :
                    flag1 = False
                flag0 = flag0 or flag1
            if flag0 == False:
                return False,Iskeyancestor,ExistPath

            flag2 = False
            for choiceDestinationId in choiceDestinationIds:
                choiceDestinationnode = nodeRepository.getnode(int(choiceDestinationId))
                flag3 = True
                key1 = str(nodeChoice.getNodeID()) + "#" + str(c.getNodeID())
                key2 = str(choiceDestinationId) + "*" + str(c.getNodeID())
                if key1 in Iskeyancestor:
                    T1 = Iskeyancestor[key1]
                else:
                    Iskeyancestor[key1] = iskeyancestor(choiceSourcenode,cSourcenode)
                    T1 = Iskeyancestor[key1]
                if key2 in ExistPath:
                    T2 = ExistPath[key2]
                else:
                    ExistPath[key2] = (existPath(choiceDestinationnode,cSourcenode) == False)
                    T2 = ExistPath[key2]
                if T1 and T2:
                    flag3 = False
                flag2 = flag2 or flag3
            if flag2 == False:
                return False,Iskeyancestor,ExistPath
        return True ,Iskeyancestor,ExistPath
    def getChoices(self):
        return nodeRepository.loadChoices(self._choicesIds)
    def toString(self):
        rlt = ""
        sortedList = sorted(nodeRepository.loadChoices(self._choicesIds), key=lambda c: c.getNodeID())
        for choice in sortedList:
            rlt = rlt + choice.toString()
        return rlt
    def getChoicesNodeIds(self):
        return self._choicesNodeIds
    def getNextNodeId(self,stra,nowNodeId):
        if (str(nowNodeId) in self._choicesNodeIds) and (str(nowNodeId) in stra.getChoicesNodeIds()):
            # print("调用1")
            choiceA = nodeRepository.getChoice(self._choicesNodeIds[str(nowNodeId)])
            choiceB = nodeRepository.getChoice(stra.getChoicesNodeIds()[str(nowNodeId)])
            outIdsA = choiceA.getOutId()
            outIdsB = choiceB.getOutId()
            commonId = ""
            for id in outIdsA:
                if id in outIdsB:
                    commonId = id
                    return str(commonId)
        elif (str(nowNodeId) in self._choicesNodeIds) and (str(nowNodeId) not in stra.getChoicesNodeIds()):
            # print("调用2")
            choice = nodeRepository.getChoice(self._choicesNodeIds[str(nowNodeId)])
            outId = choice.getChoiceId()
            return str(outId)

        elif (str(nowNodeId) not in self._choicesNodeIds) and (str(nowNodeId)  in stra.getChoicesNodeIds()):
            # print("调用3")
            choice = nodeRepository.getChoice(stra.getChoicesNodeIds()[str(nowNodeId)])
            outId = choice.getChoiceId()
            return str(outId)
        else:
            # print("调用4")
            node = nodeRepository.getnode(nowNodeId)
            print(node.getChildrenId())
            return node.getChildrenId()[0]

    def findUtility(self, stra, leavesUtil):
        print("当前的策略组合分别是:  ",self.toString(),stra.toString())
        nextNodeId = self.getNextNodeId(stra, 1)
        nextNode = nodeRepository.getnode(int(nextNodeId))
        print("下一个节点id",nextNodeId,nextNode.getStates())
        while  (nextNode.isLeafNode() == False):
            nextNodeId= self.getNextNodeId(stra,nextNodeId)
            nextNode = nodeRepository.getnode(int(nextNodeId))
            print("下一个节点id", nextNodeId, nextNode.getStates())
        print(self.getUtility(nextNode, leavesUtil))
        return self.getUtility(nextNode,leavesUtil)
    @staticmethod
    def getUtility(node, leavesUtil):
        print("叶节点的状态: ",node.getStates())
        flag = 0
        for item in leavesUtil:
            leaf = item[0]
            if node.getId() == leaf.getId():
                flag = 1
                return [item[1], item[2]]
        if flag == 0:
            return [-1,-1]
class Strategy:
    def __init__(self,player):
        self._player = player
        self._choices = []
    def toString(self):
        rlt = ""
        sortedList = sorted(self._choices, key=lambda c: c.getNodeID())
        for choice in sortedList:
            rlt = rlt + choice.toString()
        return rlt
    def getChoices(self):
        return self._choices
    # 查看choiceSet中的choice 是否全部在 self._choices
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
    #构造一个策略的选择可能
    @staticmethod
    def buildStrategies(player, choiceGroupList):
        straSet = []
        for l in itertools.product(*(choiceGroupList)):              #形成笛卡尔积
            stra = Strategy(player)
            stra._choices.extend(l)
            straSet.append(stra)
        return straSet
    #构造一个策略的选择可能
    @staticmethod
    def buildreducedStrategies(player, choiceCombinationList):
        straSet = []
        for cComb in  choiceCombinationList:
            stra = Strategy(player)
            stra._choices.extend(cComb.getChoices())
            straSet.append(stra)
        return straSet
    @staticmethod
    def toChoicesCombination(straSet):
        Choices = []
        for stra in straSet:
            com = ChoiceCombination()
            for choice in stra.getChoices():
                com.addChoice(choice)
            Choices.append(com)
        return Choices

def createStrategies(root):
    queue = []
    mapping = {}
    queue.append(root)
    mapping[str(root.getId())] = ""
    wholeChoicesA = []
    wholeChoicesB = []
    while len(queue) > 0:
        node = queue.pop(0)
        nodeChoicesA = []
        nodeChoicesB = []
        for ce in node.getOutEdges():
            choiceA,choiceB = ce.getAllChoices()
            nodeRepository.addChoice(choiceA)
            nodeRepository.addChoice(choiceB)
            # if settings.DEBUG:
            #     print("ChoiceA.toString():  ",choiceA.toString())
            #     print("ChoiceB.toString():   ",choiceB.toString())
            if choiceA.isEmpty() == False:
                choiceA.setOutId(ce.getChildId())
                nodeChoicesA.append(choiceA)
            if choiceB.isEmpty() == False:
                choiceB.setOutId(ce.getChildId())
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

    straSetA = Strategy.buildStrategies("A", wholeChoicesA)
    straSetB = Strategy.buildStrategies("B", wholeChoicesB)
    ChoicesA = Strategy.toChoicesCombination(straSetA)
    ChoicesB = Strategy.toChoicesCombination(straSetB)

    # if settings.DEBUG:
    #     print("strategies of player A:")
    #     for stra in straSetA:
    #         print(stra.toString())
    #     print ("strategies of player B:")
    #     for stra in straSetB:
    #         print(stra.toString())
    if settings.DEBUG:
        print("A的策略数: ",len(straSetA))
        print("B的策略数: ",len(straSetB))

    return straSetA, straSetB, ChoicesA, ChoicesB
#得到到根节点的所有路径的祖先节点
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
            # print("遍历10个的时间: ", endtime - starttime)
            starttime = endtime
        ancestorMapping[str(node.getId())] = getAncestor(node ,[node.getId()])
        for child in nodeRepository.loadNodes(node.getChildrenId()):
            if str(child.getId()) not in mapping:
                mapping[str(child.getId())] = ""
                queue.append(child)
    return ancestorMapping
# 判断是否是关键节点
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
            # print("遍历10个的时间: " ,endtime - starttime)
            starttime = endtime
        childNodesMapping[str(node.getId())] = childNodes(node)
        for child in nodeRepository.loadNodes(node.getChildrenId()):
            if str(child.getId()) not in mapping:
                mapping[str(child.getId())] = ""
                Queue.append(child)
    return childNodesMapping
#得到所有节点的孩子节点
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
#生成新的策略组合
def updatenewChoices(newChoices,choices,nodeChoices,ChoicesFlag,ExistPath ,Iskeyancestor):
    if len(choices) == 0:
        for nodeChoice in nodeChoices:
            cComb = ChoiceCombination()
            cComb.addChoice(nodeChoice)
            newChoices.append(cComb)
    else:
        T = 0
        for cCombation in choices:
            for nodeChoice in nodeChoices:
                flag,Iskeyancestor,ExistPath= cCombation.needChoice(nodeChoice, ExistPath, Iskeyancestor)
                if flag:
                    if str(T) in ChoicesFlag:
                        del ChoicesFlag[str(T)]
                    newcComb = copy.deepcopy(cCombation)
                    newcComb.addChoice(nodeChoice)
                    newChoices.append(newcComb)
            T = T + 1
    return newChoices,Iskeyancestor,ExistPath
#更新策略组合
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
#存储以及获取两种数据
#Input
    #root    状态机根节点
#Output
    # childNodeMapping  孩子节点的集合
    # ancestorMapping  祖先节点的集合
def getData(root):
    childNodeMapping = childNodesMapping(root)
    mydb = open('dbase', 'wb')
    pickle.dump(childNodeMapping, mydb)
    ancestorMapping = getAllnodeAncestor(root)
    mydb2 = open('dbase2', 'wb')
    pickle.dump(ancestorMapping, mydb2)
    mydb = open('dbase', 'rb')
    childNodeMapping = pickle.load(mydb)
    mydb2 = open('dbase2', 'rb')
    ancestorMapping = pickle.load(mydb2)
    for key in ancestorMapping:
        T = 0
        for ancestor in ancestorMapping[key]:
            length = len(ancestor)
            a = [str(j) for j in ancestor]
            b = [""]*length
            c = zip(a, b)
            ancestorMapping[key][T] = dict(c)
            T = T + 1
    return childNodeMapping , ancestorMapping
def reduceStrategies(root):
    ExistPath = {}               #存储两个节点之间是否存在路径
    Iskeyancestor = {}           #存储是否是关键祖先节点
    childNodeMapping, ancestorMapping = getData(root)       #得到孩子节点的集合与祖先节点的集合
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
            nodeRepository.addChoice(choiceA)
            nodeRepository.addChoice(choiceB)
            if choiceA.isEmpty() == False:
                choiceA.setOutId(ce.getChildId())
                nodeChoicesA.append(choiceA)
            if choiceB.isEmpty() == False:
                choiceB.setOutId(ce.getChildId())
                nodeChoicesB.append(choiceB)
        nodeChoicesA = Choice.removeDupChoices(nodeChoicesA)
        nodeChoicesB = Choice.removeDupChoices(nodeChoicesB)
        newChoicesA,Iskeyancestor,ExistPath = updatenewChoices(newChoicesA,ChoicesA,nodeChoicesA,ChoicesAFlag,ExistPath ,Iskeyancestor)
        newChoicesB,Iskeyancestor,ExistPath = updatenewChoices(newChoicesB,ChoicesB,nodeChoicesB,ChoicesBFlag,ExistPath ,Iskeyancestor)
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
    return straSetA, straSetB, ChoicesA, ChoicesB
if __name__ == '__main__':
    mydb3 = open('dbase3', 'rb')
    Nodes = pickle.load(mydb3)
    # mydb4 = open('dbase4', 'rb')
    # leavesUtil = pickle.load(mydb4)
    for node in Nodes:
        print(node.getId())
    nodeRepository.initRepository(Nodes)
    node = nodeRepository.getnode(1691118)

    # C,D = reduceStrategies(root)
    # createPayoffMatrix(C, D, root, leavesUtil)
