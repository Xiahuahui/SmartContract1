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
    def toString(self):
        sortedList = sorted(self._choices, key=lambda c: c.getNodeID())

        rlt = []
        for choice in self._choices:
            rlt.append(choice.toString())

        return str(rlt)

    @staticmethod
    def buildStrategies(player, choiceGroupList):
        straSet = []
        for l in itertools.product(*(choiceGroupList)):              #形成笛卡尔积
            stra = Strategy(player)
            stra._choices.extend(l)
            straSet.append(stra)
        return straSet


# class Path:
#     def __init__(self):
class PayoffMatrix:
    def __init__(self,m,n):
        self._payoff = np.arange(m,n)

def removeDupChoices(choices):
    myMap = {}
    rlt = []
    for c in choices:
        if c.toString() not in myMap:
            myMap[c.toString()] = ""
            rlt.append(c)
    return rlt

def createStrategies(root):
    print("调用")
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
            edgeChoicesA,edgeChoicesB = ce.getAllChoices(node.getId())
            nodeChoicesA.extend(edgeChoicesA)
            nodeChoicesB.extend(edgeChoicesB)

        # 去除重复
        nodeChoicesA = removeDupChoices(nodeChoicesA)
        nodeChoicesB = removeDupChoices(nodeChoicesB)

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