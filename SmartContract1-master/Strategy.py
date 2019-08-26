import numpy as np
from Choices import *
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
            print("根节点出边的长度: ",len(node.getOutEdges()))
            choiceA,choiceB = ce.getAllChoices()
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
        for choiceGroup in wholeChoicesA:
            for choice in choiceGroup:
                print(choice.toString())
            print()

        print("wholeChoicesB: ", len(wholeChoicesB))
        for choiceGroup in wholeChoicesB:
            for choice in choiceGroup:
                print(choice.toString())
            print()

    straSetA = Strategy.buildStrategies("A", wholeChoicesA)
    straSetB = Strategy.buildStrategies("B", wholeChoicesB)

    if settings.DEBUG:
        print("strategies of player A:")
        for stra in straSetA:
            print(stra.toString())
        print ("strategies of player B:")
        for stra in straSetB:
            print(stra.toString())

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

