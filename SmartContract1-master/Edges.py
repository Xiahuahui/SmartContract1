from Strategy import *
class CompositeEdge:
    def __init__(self):
        self._edges = []
    def appendEdge(self,edge):
        self._edges.append(edge)
    def toString(self):   #TODO
        rlt = []
        for edge in self._edges:
            rlt.append(edge.toString())
        rlt = sorted(rlt, key=lambda e: e[0])
        return str(rlt)
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
        choicesA = []
        choicesB = []
        for edge in self._edges:
            choiceA = Choice("A")
            choiceB = Choice("B")
            for e in edge._events:
                #TODO  if player == Contract, we just ignore it
                if e.getPlayer() == "A":
                    choiceA.addEvent(e)
                elif e.getPlayer() == "B":
                    choiceB.addEvent(e)
            if choiceA.isEmpty() == False:
                choicesA.append(choiceA)
            if choiceB.isEmpty() == False:
                choicesB.append(choiceB)

        return choicesA,choicesB
    def getAction(self):
        action
        for edge in self._edges:
            act = ""
            for event in edge:
                act = act + event.getPlayer()+event.getActDesc()
            action = action + act + ","


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
# Event 类结构
#各个成员变量的含义
    #player #该事件的动作人
    #actDesc #对动作的描述
    #cmtId #对应Commitment的id
class Event:
    def __init__(self,player,actDesc,cmtId): # 初始化Events
        self._player = player #该事件的动作人
        self._actDesc = actDesc #actDesc #对动作的描述
        self._cmtId = cmtId #cmtId #对应Commitment的id
    def getPlayer(self): # Player must be either A or B !!!
        return self._player
    def getCmtId(self):
        return self._cmtId
    def getActDesc(self):
        return self._actDesc
    def toString(self):
        return str([self._player,self._actDesc,self._cmtId])
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
    print(comEdge1.getAllChoices())