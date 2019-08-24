import numpy as np
import itertools
from GNode import *
from NodeRepository import nodeRepository
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

class Choice:
    def __init__(self, nodeId):
        self._events = []
        self._nodeId = nodeId
    def addEvent(self, e):
        self._events.append(e)
    def isEmpty(self):
        return len(self._events) == 0
    def getNodeID(self):
        return self._nodeId

    def toString(self):
        rlt = []
        for event in self._events:
            rlt.append([event.getPlayer(),event.getActDesc(),event.getCmtId(),self._nodeId])
        rlt = sorted(rlt, key=lambda e: e[2])
        return str(rlt)
# class Path:
#     def __init__(self):
class PayoffMatrix:
    def __init__(self,m,n):
        self._payoff = np.arange(m,n)
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
            edgeChoicesA,edgeChoicesB = ce.getAllChoices()
            # nodeChoicesA.extend(edgeChoicesA)
            # nodeChoicesB.extend(edgeChoicesB)
            for choiceA in edgeChoicesA:
                nodeChoicesA.append(choiceA.toString())
            for choiceB in edgeChoicesB:
                nodeChoicesB.append(choiceB.toString())
        if len(nodeChoicesA) != 0:
            wholeChoicesA.append(nodeChoicesA)
        if len(nodeChoicesB) != 0:
            wholeChoicesB.append(nodeChoicesB)
        children = nodeRepository.loadNodes(node.getChildrenId())
        for child in children:
            if str(child.getId()) not in mapping:
                mapping[str(child.getId())] = ""
                queue.append(child)
    print("wholeChoicesA: ", len(wholeChoicesA))
    print("wholeChoicesB: ", len(wholeChoicesB))
    straSetA = Strategy.buildStrategies("A", wholeChoicesA)
    straSetB = Strategy.buildStrategies("B", wholeChoicesB)
    print(straSetA,straSetB)
    return straSetA, straSetB