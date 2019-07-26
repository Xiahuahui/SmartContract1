
from Literal import Literal
class Clause:
    def __init__(self):
        self._literals = []
        self._isZero = True # 仅当clause为空时生效,该值为True时表明clause为矛盾式,否则为永真式

    def addLiteral(self, lit):
        self._literals.append(lit)

    def isEmpty(self):
        return len(self._literals) == 0

    # 设置 conLiteralID 对应的 literal 的状态
    # 若存在这样的literal， if lit.status = status, 则该 lit 被置为 1； 否则 置为0
    # 对 clause 做相应更新
    def assignLiteral(self, conLiteralID, status):
        for lit in self._literals:
            if lit.getConLiteralID() == conLiteralID:
                if lit.getStatus() == status:
                    self._literals.clear() # 有一项为1，clause 取值为1
                    self._isZero = False # 永真式
                    break
                else:
                    self._literals.remove(lit)
                break

    def isTautology(self):
        if len(self._literals)==0:
            # literals 已清空, 根据 isZero判断
            return not self._isZero
        else:
            return False;

    def isContradiction(self):
        if len(self._literals)==0:
            # literals 已清空, 根据 isZero判断
            return self._isZero
        else:
            return False;


    def enumLiterals(self):
        return iter(self._literals)

    def containsNonStoppedCMT(self):
        for lit in self._literals:
            if lit.isCMT():
                return True
        return False

    def containsAction(self):
        for lit in self._literals:
            if not lit.isCMT():
                return True
        return False
    def getAction(self):
        Action = []
        for lit in self._literals:
            if not lit.isCMT():
                print(lit.toString())
                Action.append(lit.toString())
        return Action


    def toString(self):
        rlt = ''
        for lit in self._literals:
            rlt += lit.toString()
            rlt += '||'
        rlt = rlt[0:len(rlt)-2] # 去掉末尾多余的 ||
        return  rlt

if __name__ == '__main__':
    cls = Clause()
    # Term1.Sat, judge()  &&  Term1.Vio, !judge(）
    lit = Literal(1, 'Term1')
    lit.setStatus(3)
    cls.addLiteral(lit)
    lit = Literal(2,'judge(A,pay)')
    lit.setStatus(1)

    cls.addLiteral(lit)

    print(cls.toString())
    cls.assignLiteral('Term1',4 )
    print(cls.toString())

