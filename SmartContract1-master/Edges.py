from Choices import *
from Event import *
class CompositeEdge:
    def __init__(self,parentId,childId):
        self._edges = []
        self._parentId =  parentId
        self._childId = childId
    def appendEdge(self,edge):
        self._edges.append(edge)
    def toString(self):
        rlt = []
        for edge in self._edges:
            rlt.append([edge.toString()])
        rlt = sorted(rlt, key=lambda e: e[0])
        return str(rlt)
    def getParentId(self):
        return self._parentId
    def getChildId(self):
        return self._childId
    def updateChildId(self,id):
        self._childId = id
    def updateParentId(self,id):
        self._parentId = id
    def mergeEdge(self,comEdge):
        Mapping = {}
        for edge in self._edges:
            Mapping[edge.toString()] = ""
        for edge in comEdge._edges:
            if edge.toString() not in Mapping:
                Mapping[edge.toString()] = ""
                self._edges.append(edge)

    # return choices of both players at this CompositeEdge, like  [choice1,choice2,...],[choice1,choice2,...]
    def getAllChoices(self):
        choiceA = Choice(self._parentId)
        choiceB = Choice(self._parentId)
        for edge in self._edges:
            edgeChoiceA = EdgeChoice()
            edgechoiceB = EdgeChoice()
            for e in edge._events:
                #TODO  if player == Contract, we just ignore it
                if e.getPlayer() == "A":
                    edgeChoiceA.addEvent(e)
                elif e.getPlayer() == "B":
                    edgechoiceB.addEvent(e)
            if edgeChoiceA.isEmpty() == False:
                choiceA.addEdgeChoide(edgeChoiceA)
            if edgechoiceB.isEmpty() == False:
                choiceB.addEdgeChoide(edgechoiceB)
        return choiceA,choiceB



#边集类结构
#各个成员变量的含义
    #events   Event的列表 [Event,Event,Event,]
class Edge:
    def __init__(self):
        self._events = []  # 每个event包含 动作人，动作，序号 ，即 [actperson,act,index]
    def addEvent(self,event):     #往边里面添加事件
        self._events.append(event)
    def toString(self):
        rlt = []
        for event in self._events:
            rlt.append([event.getPlayer(),event.getActDesc(),event.getCmtId()])
        rlt = sorted(rlt, key=lambda e: e[0] + "," + e[2])
        return str(rlt)

if __name__ == '__main__':
    print("边集: Edges")
    event1 = Event('A',"judge()","1")
    event2 = Event("B","pay","2")
    event3 = Event('A',"judge()","1")
    event4 = Event("B","pay","2")
    edge1 = Edge()
    edge2 = Edge()
    edge1.addEvent(event1)
    edge1.addEvent(event2)
    edge2.addEvent(event4)
    edge2.addEvent(event3)
    print(edge1.toString())
    compositeEdge1 = CompositeEdge(1,2)
    compositeEdge1.appendEdge(edge1)
    compositeEdge2 = CompositeEdge(1,2)
    compositeEdge2.appendEdge(edge2)
    print(compositeEdge1.toString())
    print(compositeEdge2.toString())
    compositeEdge1.mergeEdge(compositeEdge2)
    print(compositeEdge1.toString())
    print("检测choice:")
    choice1,choice2 = compositeEdge1.getAllChoices()
    print(len(choice1),len(choice2))
    choice3, choice4 = compositeEdge2.getAllChoices()
    print(len(choice3),len(choice4))