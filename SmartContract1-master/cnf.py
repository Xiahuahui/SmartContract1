class CNF:
    #构造函数 返回一个cnf类
    def __init__(self):

    # 构建cnf(初始化cnf)
    #Input premise   commitment中的premise  Term1.Sat||judge(A,pay)&&Term2.Vio||not judge(A,pay)
    def buildPremise(self, premise):
    # 分解CNF  得到clause类的列表 [clause,clause,clause,...]
    def getClauseSet(self):
        return [Clause(),Clause(),Clause(),...]
    # 查看cnf中的条款是否都到达终态 返回真假
    def getFlag(self):
        return True
    # 更新前提
    # Input [[Term1：2], [Term2：3]] 字典
    # Output 无返回值
    def updateCnf(self,combineChange):

    #判断该cnf是否是矛盾式 返回True/False
    def isContradiction(self):
        return True
    #判断该cnf是否是永真是 返回True/False
    def isTautology(self):
        return False
    #返回所有的judge组合   [ [judge(A,pay), -judge(B,mail)], [-judge(A,pay), judge(B,mail)],...]
    # 返回所有使得CNF满足（T）或不满足（F）的model
    # 注意，调用此函数时，默认CNF中所有的commitment已进入终态
    # 返回结果形式，两个list，第一个list为T，第二个list为F
    # 形如T= [[judge(A,pay), !judge(B,mail)],[!judge(A,pay),judge(B,mail)]
    def getAllModels(self):
        return []
# Clause类
class Clause:
    def __init__(self):
    # 得到Clause中的Literal类的列表   [literal,literal,literal,...]
    def getLiterals(self):
        return[Literal(),Literal()]
# Literal类
class Literal:
    def __init__(self):
    #得到literal的id  Term1
    def getConLiteralID(self):
        return Term1
    #得到literal是不是Term    True/False
    def isCMT(self):
        return True
    #当literal是judeg(A,1),得到  A
    def getPlayer(self):
        return 'A'
