from Event import *
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