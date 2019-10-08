from Choices import *
import time
import copy
import itertools
from GNode import *
from NodeRepository import nodeRepository
from Settings import settings
from Edges import *
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

        # 去除重复
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
# 查找节点的
# def getAncestor(node):
#     ancestors = {}
#     ancestors[str(node.getId())] = ""
#     parentsId = node.getParentsId()
#     while len(parentsId) > 0:
#         newParentsId = {}
#         for id in parentsId:
#             if str(id) not in ancestors:
#                 ancestors[str(id)] = ""
#             newnode = nodeRepository.getnode(int(id))
#             newnodeParentsId = newnode.getParentsId()
#             for parentId in newnodeParentsId:
#                 if str(parentId) not in newParentsId:
#                     newParentsId[str(parentId)] = ""
#         parentsId = newParentsId
#     return ancestors
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
def getParentId(parentsId,Dict,player):
    newparentsId = copy.deepcopy(parentsId)
    newparentsId.pop(0)
    for pId in newparentsId:
        # print("当前节点的Id: ",pId)
        parent = nodeRepository.getnode(pId)
        nodeChoicesA = []
        nodeChoicesB = []
        for ce in parent.getOutEdges():
            choiceA, choiceB = ce.getAllChoices()
            if choiceA.isEmpty() == False:
                nodeChoicesA.append(choiceA)
            if choiceB.isEmpty() == False:
                nodeChoicesB.append(choiceB)
        if player == "A":
            if len(nodeChoicesA) > 0:
                if str(pId) in Dict:

                    return pId
        elif player == "B":
            if len(nodeChoicesB) > 0:

                if str(pId) in Dict:
                    return  pId
#定义其中一种策略的组合:
class ChoiceCombination:
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

    # def needNode(self,node):                   #判断是否需要与当前的策略组合做笛卡尔积
    #     ancestors = getAncestor(node)
    #     for ancestor in ancestors:
    #         if str(ancestor) in self._Id:
    #             flag = False
    #             for childId in self._Id[ancestor]:
    #                 if childId  in ancestors:
    #                     flag = flag or True
    #             if flag == False:
    #                 return False
    #     return  True
    def needNode(self,node,player):                   #判断是否需要与当前的策略组合做笛卡尔积
        ancestors = getAncestor(node,[node.getId()])
        flag0 = False
        flag3 = True
        for ancestor in ancestors:
            # print("调用修改后的函数")
            # print("当前的祖先节点: ",ancestor)
            # print("当前的策略,",self._Id)
            flag1 = False
            flag4 = False
            for ancestorId in ancestor:
                if str(ancestorId) in self._Id:
                    flag4 = flag4 or True
                    # print(str(ancestorId))
                    flag2 = False
                    for childId in self._Id[str(ancestorId)]:
                        # print("childId:  ",childId)
                        # print("ancestor",ancestor)
                        if int(childId)  in ancestor:
                            # print("在")
                            # print(ancestorId,getParentId(ancestor,self._Id,player))
                            # print("自家最近的策略: ",getParentId(ancestor,self._Id,player))
                            if ancestorId == getParentId(ancestor,self._Id ,player):
                                flag2 = flag2 or True
                                # print("需要做笛卡尔积:   ")
                    flag1 = flag1 or flag2
            flag3 = flag3 and flag4
            flag0 = flag0 or flag1
        if flag3 == False:
            return  True
        if flag0 == False:
            return False
        return  True
    # def copy(self):                       #当前策略组合的一种复制
    #     newcComb = ChoiceCombination()
    #     newcComb._choices = self._choices
    #     newcComb._Id = self._Id
    #     return newcComb
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
def reduceStrategies(root):
    queue = []
    mapping = {}
    queue.append(root)
    mapping[str(root.getId())] = ""
    ChoicesA = []            #初始化的player A 策略组合
    ChoicesAFlag = {}
    ChoicesB = []            #初始化的player B 策略组合
    ChoicesBFlag = {}
    TT = 0
    starttime = time.time()
    while len(queue) > 0:
        flagA = False
        flagB = False
        if len(ChoicesA) == 0:      #判断是不是第一次出现
            flagA = True
        if len(ChoicesB) == 0:
            flagB = True
        node = queue.pop()
        TT = TT +1
        print("处理过的节点个数: ",TT)
        endtime = time.time()
        print("处理这些叶结点耗时:", endtime - starttime)
        starttime = endtime

        # print("当前节点的状态:",node.getStates())
        # print("当前节点的祖先:",getAncestor(node,[node.getId()]))
        newChoiceA = []
        newChoiceB = []
        nodeChoicesA = []
        nodeChoicesB = []
        for ce in node.getOutEdges():
            choiceA, choiceB = ce.getAllChoices()
            if choiceA.isEmpty() == False:
                nodeChoice = NodeChoice(choiceA)
                nodeChoice.setOutId(ce.getChildId())
                nodeChoicesA.append(nodeChoice)
            if choiceB.isEmpty() == False:
                nodeChoice = NodeChoice(choiceB)
                nodeChoice.setOutId(ce.getChildId())
                nodeChoicesB.append(nodeChoice)
        nodeChoicesA = NodeChoice.removeDupChoices(nodeChoicesA)
        nodeChoicesB = NodeChoice.removeDupChoices(nodeChoicesB)
        if flagA:
            for nodeChoice in nodeChoicesA:
                cComb = ChoiceCombination()
                cComb.addChoice(nodeChoice.getChoice(), node.getId(),nodeChoice.getOutId())
                newChoiceA.append(cComb)
        else:
            T = 0
            for cCombation in ChoicesA:
                if cCombation.needNode(node,"A"):
                    if str(T) in ChoicesAFlag:
                        del ChoicesAFlag[str(T)]
                    for nodeChoice in nodeChoicesA:
                        newcComb = copy.deepcopy(cCombation)
                        newcComb.addChoice(nodeChoice.getChoice(), node.getId(), nodeChoice.getOutId())
                        newChoiceA.append(newcComb)
                    T = T + 1
        if flagB:
            for nodeChoice in nodeChoicesB:
                cComb = ChoiceCombination()
                cComb.addChoice(nodeChoice.getChoice(), node.getId(), nodeChoice.getOutId())
                newChoiceB.append(cComb)
        else:
            T = 0
            for cComb in ChoicesB:
                if cComb.needNode(node,"B"):
                    if str(T) in ChoicesBFlag:
                        del ChoicesBFlag[str(T)]
                    for nodeChoice in nodeChoicesB:
                        newcComb = copy.deepcopy(cComb)
                        newcComb.addChoice(nodeChoice.getChoice(), node.getId(), nodeChoice.getOutId())
                        newChoiceB.append(newcComb)
                    T = T+1
        if len(newChoiceA) != 0:
            tmp = []
            for key in ChoicesAFlag:
                tmp.append(ChoicesA[int(key)])
            tmp.extend(newChoiceA)
            ChoicesA = list(tmp)
            ChoicesAFlag = {}
            for i in range(len(ChoicesA)):
                ChoicesAFlag[str(i)] = ""
        if len(newChoiceB) != 0:
            # print("B当前的策略组合: ")
            for cComb in ChoicesB:
                print(cComb.toString())
            tmp = []
            for key in ChoicesBFlag:
                tmp.append(ChoicesB[int(key)])
            tmp.extend(newChoiceB)
            ChoicesB = list(tmp)
            ChoicesBFlag = {}
            for i in range(len(ChoicesB)):
                ChoicesBFlag[str(i)] = ""
        # print("A当前的策略组合: ")
        # for cComb in ChoicesA:
        #     print(cComb.toString())
        # print("B当前的策略组合: ")
        # for cComb in ChoicesB:
        #     print(cComb.toString())
        print("ChoicesA的长度",len(ChoicesA))
        # print(ChoicesAFlag)
        print("ChoicesB的长度", len(ChoicesB))
        # print(ChoicesBFlag)
        children = nodeRepository.loadNodes(node.getChildrenId())
        for child in children:
            if str(child.getId()) not in mapping:
                mapping[str(child.getId())] = ""
                queue.append(child)
    straSetA = Strategy.buildreducedStrategies("A", ChoicesA)
    straSetB = Strategy.buildreducedStrategies("B", ChoicesB)
    return straSetA, straSetB
if __name__ == '__main__':
    print("策略:   单元测试")
    choice = Choice(1)
    choice1 = Choice(2)
    choice2 = Choice(1)
    choice3 = Choice(2)
    event1 = Event("A","二额","0")
    event2 = Event("A","san","1")
    event4 = Event("A","二额","0")
    event3 = Event("A","san","1")
    choice.addEvent(event1)
    choice.addEvent(event2)
    choice1.addEvent(event3)
    choice1.addEvent(event4)
    choice2.addEvent(event1)
    choice2.addEvent(event2)
    choice3.addEvent(event3)
    choice3.addEvent(event4)
    strategy = Strategy('A')
    strategy.addChoice(choice)
    strategy.addChoice(choice1)
    print(strategy.toString())
    print(strategy.contain([choice2,choice3]))

