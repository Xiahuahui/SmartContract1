import sys
sys.path.append('.')
from .CNF import CNF
#Commitment类结构
#各个成员变量的含义及例子
    # premise Commitment的前提是个CNF表达式
    # id Commitment的id Term1,Term2,Term3,...
    # player Commitment的动作人 A||B||Contract
    # resultAction Commitment中的result的动作
    # status Commitment当前的状态值1-5
    # contractFlag 判断Commitment的动作人是否是Contract 若是则为True 否则为False
class Commitment:
    def __init__(self,id,player,resultAction):
        self._premise = CNF()  # 逻辑表达式
        self._id = id  # Commitment的id
        self._player = player     #Commitment的动作人
        self._resultAction = resultAction  #Commitment中结果的动作
        self._status = 1  # Commitment的状态值 初始化时设置为1
        self._contractFlag = False  # 动作人是否是Contract
    def buildCommitment(self,premise,player):        #初始化Commitment
        self._premise.build(premise) #构建Commitment中的CNF表达式
        if premise == None or premise == "": #如果premise为空 则将status置为2
            self._status = 2 #则将status置为2
        if player == "C":                   #如果动作人为Contract
            self._contractFlag = True #将contractFlag置为 True
    def getContractFlag(self):         #判断Commitment的动作人是否是Contract
        if self._contractFlag == False: #若不是,则返回False
            return False
        if self._contractFlag == True:  #若是 则返回True
            return True
    def getId(self):       #返回commitment的id
        return self._id
    def getPlayer(self):  # 得到Commitment动作人
        return self._player
    def updatePremise(self,combineChange): # 更新前提 Input [[Term1：2], [Term2：3]]
        self._premise.updateCnf(combineChange)
    def getAct(self):            #得到Commitment的动作
        return self._resultAction
    def setStatus(self,status): #设置Commitment的状态值
        self._status = status
    def getStatus(self): #设置Commitment的状态值
        return  self._status
    def getPremise(self):
        return self._premise
    def toString(self):
        rlt = "("
        rlt += self._id+","+self._player +","+self._premise.toString()+")"
        return rlt
if __name__ == '__main__':
    c = CNF()