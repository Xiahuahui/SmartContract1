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