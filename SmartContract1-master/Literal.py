import copy

# 注意：Term1.Sat 和 Term1.Vio 是两个literal，但是 它们的 contractLiteral ID 相同
# 但是！！！ judge(A,pay) 和 !judge(A,pay) 却是相同的literal id, 也是相同的 contractLiteralID
# judge(A,pay) 的 polarity 为 1， 而  !judge(A,pay) 的 polarity 为 0
# TODO 实际 Term1.Sat 和 Term1.Vio 也应该采用相同的Literal, 但是这就必须引入其他clause来描述同一Term 的Sat，Vio，Exp关系
# TODO 而且，在我们目前的实现中，当CNF中存在 Term时，都不会判断其 永真，永假，因此这样处理应该不会有问题
# 使用 status 来保存 Sat, Vio, Exp, 例如， Term1.Sat 对应 Literal.status = 3
class Literal:
    # 初始化 literal 对象时，会根据 输入的信息判断是否 CMT
    def __init__(self, litID, conLitID):
        self._ID = litID
        self._conLitID = conLitID
        self._status = 1
        if conLitID[0:4] == 'Term':
            self._type = 1 # 是CMT
        else:
            self._type = 0

    def toString(self):
        dicStatus = {3:'Sat', 4:'Exp', 5:'Vio'} # TODO 应存储在类似 globalSettings 的地方
        rlt = ''
        if self.isCMT():
            rlt += self._conLitID + '.'
            rlt += dicStatus[self._status]
        else:
            if self.isNegative():
                rlt += '!'
            rlt+= self._conLitID
        return rlt

    def getID(self):
        return self._ID;

    def setID(self, val):
        self._ID = val

    def getName(self):  #name =  CMTID.Status or, name = judge()
        return ""

    def getConLiteralID(self):  #string e.g. Term1
        return self._conLitID

    def setStatus(self, val):
        self._status = val
    def getStatus(self):  #int
        return self._status

    def isCMT(self): # 该literal对应的是否为commitment
        return (self._type == 1)

    #当literal为judge时，返回player
    #例如， judge(A,pay) 返回 A
    def getPlayer(self):
        if self.isCMT():
            return ''
        else:
            start = self._conLitID.find('(') + 1
            end = self._conLitID.find(',')
            return self._conLitID[start:end]


    #下面函数仅对 judge 类型的literal有意义
    def isNegative(self):
        return self._status == 0

    # 创建一个与当前Literal 极性相反的Literal，二者ID相同
    def createOpposite(self):
        lit = copy.copy(self)
        if self._status == 1:
            lit._status = 0
        else:
            lit._status = 1
        return lit


if __name__ == '__main__':
    lit = Literal(1, 'judge(A,pay)')
    lit.setStatus(0)
    print(lit.toString())
    print('player:', lit.getPlayer())

    lit = Literal(2, 'Term1')
    lit.setStatus(3)
    print(lit.toString())
    print(lit.getPlayer())


