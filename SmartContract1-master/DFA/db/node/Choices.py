import sys
sys.path.append('.')
from .Event import Event
class Choice:
    Id = 0
    def __init__(self, nodeId):
        Choice.Id = Choice.Id + 1
        self._id  = Choice.Id
        self._edgeChoices = []
        self._nodeId = nodeId
        self._outId = {}
    def getOutIdForDict(self):
        return self._outId
    def getId(self):
        return self._id
    def getEdgeChoices(self):
        return self._edgeChoices
    def setOutId(self,outId):
        if str(outId) not in self._outId:
            self._outId[str(outId)] = ""
    def getChoiceId(self):
        return list(self._outId.keys())[0]
    def getOutId(self):
        return list(self._outId.keys())
    def addEdgeChoide(self, c):
        self._edgeChoices.append(c)
    def getNodeID(self):
        return self._nodeId
    def isEmpty(self):
        return len(self._edgeChoices) == 0
    def toString(self):
        rlt = []
        for edgeChoice in self._edgeChoices:
            rlt.append(edgeChoice.toString())
        rlt = sorted(rlt, key=lambda e: e)
        rltStr = ""
        for edgeChoice in rlt:
            rltStr += edgeChoice + "#"
        return rltStr
    def equal(self,choice):
        if  self._nodeId == choice.getNodeID():
            list1 = sorted(self._edgeChoices, key=lambda e: e.toString())
            list2 = sorted(choice._edgeChoices, key=lambda e: e.toString())
            string1 = ""
            string2 = ""
            for e1 in list1:
                string1 = string1 + e1.toString()
            for e2 in list2:
                string2 = string2 + e2.toString()
            if string1 != string2:
                 return False
            return True
        else:
            return False
    @staticmethod
    def removeDupChoices(choices):
        myMap = {}
        rlt = []
        for c in choices:
            if c.toString() not in myMap:
                myMap[c.toString()] = c
                rlt.append(c)
            else:
                nodeChoice = myMap[c.toString()]
                nodeChoice.setOutId(int(c.getChoiceId()))
        return rlt
    @staticmethod
    def getNodeChoicesIds(nodeChoices):
        nodeChoicesIds = []
        for choice in nodeChoices:
            nodeChoicesIds.append(choice.getId())
        return nodeChoicesIds
    @staticmethod
    def removeDupChoices2(choices):
        myMap = {}
        rlt = []
        for c in choices:
            if c.toString() not in myMap:
                myMap[c.toString()] = ""
                rlt.append(c)
        return rlt
class EdgeChoice:
    def __init__(self):
        self._events = []
    def addEvent(self, e):
        self._events.append(e)
    def isEmpty(self):
        return len(self._events) == 0

    def getEvents(self):
        return self._events
    def toString(self):
        rlt = []
        for event in self._events:
            rlt.append([event.getPlayer(),event.getActDesc(),event.getCmtId()])
        rlt = sorted(rlt, key=lambda e: e[0] + "," + e[2])
        return str(rlt)
if __name__ == '__main__':
    choice = Choice(1)
    choice1 = Choice(1)
    event1 = Event("A","二额","0")
    event2 = Event("A","san","1")
    event4 = Event("A","二额","0")
    event3 = Event("A","san","1")
    choice.addEvent(event1)
    choice.addEvent(event2)
    choice1.addEvent(event3)
    choice1.addEvent(event4)
    print(choice.toString())
    print(choice1.toString())
    print(choice.equal(choice1))