import pycosat
from Clause import Clause
from Literal import Literal
import re
import copy
class CNF:
    def __init__(self):
        self._clauseSet = []
        self._alphabet = {}
        # 字母表 alphabet 是一个字典，key 为 contractLiteral ID  ，value 为 整数
        # 注意: 在CNF内部，随机变量的编号始终是从1开始，连续的一系列整数。
        self._SATCore = []
        # 形如 [[1, -5, 4], [-1, 5, 3, 4]] 的 list，可以直接由pycosat求解
        # 在构造 cnf 以及每次更新 cnf 对象之后，均须更新 _SATCore
        self._isZero = False # 仅当clauseSet为空时生效

    def build(self, premise):
        list1 = self._format(premise)
        for item in list1: # 每个item 是一个字典，如 { "Term1":"3" , "judge(A,pay):"1" }
            cls = Clause()
            #print('item:', item) #DEBUG
            for conLitID in item: # item 的每个key 是 contractLiteralID
                #print('conLitID:', conLitID) #DEBUG
                val = item[conLitID]
                lit = self._newLiteral(conLitID, val)
                #print('literal:', lit.getID(), lit.getConLiteralID(), lit.getStatus()) #DEBUG
                cls.addLiteral(lit)
            self._clauseSet.append(cls)
        self._updateSATCore()

    # 查看cnf中的条款是否都到达终态 返回真假
    def containsNonStoppedCMT(self):
        for cls in self._clauseSet:
            if cls.containsNonStoppedCMT():
                return True
        return False

    # 查看cnf中是否包含动作
    def containsAction(self):
        for cls in self._clauseSet:
            if cls.containsAction():
                return True
        return False
    def getActions(self):
        Action = []
        for cls in self._clauseSet:
            print(cls.getAction())
            Action.extend(cls.getAction())
        return Action

    # 更新前提
    # Input [[Term1：2], [Term2：3]] 字典
    # Output 无返回值
    def updateCnf(self,combineChange):
        # 先扫描每个 clause，将受影响的literal置为0 或 1，并更新clause
        # 若clause 在更新之后为空，将其从clauseSet 去掉
        #同时建立 剩余 literal字典，形如 {1:1, 4:4, 6:6}； 并且记录 maxID
        IDMappings = {}
        maxID =  0
        newClauseSet = []
        for cls in self._clauseSet:
            for conLitID in combineChange:
                if combineChange[conLitID] >= 3:
                    cls.assignLiteral(conLitID, combineChange[conLitID])
            if not cls.isEmpty():
                newClauseSet.append(cls)
                for lit in cls.enumLiterals():
                    IDMappings[lit.getID()] = lit.getID()
                    if lit.getID() > maxID:
                        maxID = lit.getID()
            else:
                # 当clause被清空,如果clause为矛盾式,则需要清空 clauseSet, 将isZero置为 False
                if cls.isContradiction():
                    self._clauseSet.clear()
                    self._isZero = True
                    break

        #TODO  可以加一个逻辑来单独处理 clauseSet为空的情况; 不过目前似乎也能正常工作

        #更新 ClauseSet，去掉空的clause
        self._clauseSet.clear()
        self._clauseSet.extend(newClauseSet)

        #更新IDMappings，将旧的ID映射为新的ID，例如 {4:1, 6:2}
        updatedID = 0
        newID = 1
        while updatedID < maxID:
            # 在 IDMappings  中找到一个 最小的，且大于前一个已更新ID 的 originID
            min = 1000000000
            for id in IDMappings:
                if updatedID < id < min:
                    min = id
            IDMappings[min] = newID # 将选中的ID 更新
            newID += 1
            updatedID = min

        # 再次扫描 clause，按照 字典中的信息，更新 literal ID，并更新 alphabet中信息
        self._alphabet.clear()
        for originID in range(1, maxID + 1):
            if originID in IDMappings:
                for cls in self._clauseSet:
                    for lit in cls.enumLiterals():
                        if lit.getID() == originID:
                            lit.setID(IDMappings[originID])
                            self._alphabet[lit.getConLiteralID() + '-' + str(lit.getStatus())] = lit
        #self._printAlphabet()
        self._updateSATCore()   # 更新 pycosat core

    #TODO 下面两个函数都需要调用eval，应予以优化
    #判断该cnf是否是矛盾式 返回True/False
    def isContradiction(self):
        if len(self._clauseSet) == 0:
            return self._isZero
        else:
            rlt = self._eval()
            return (rlt == 0)

    #判断该cnf是否是永真 返回True/False
    def isTautology(self):
        if len(self._clauseSet)==0:
            return not self._isZero
        else:
            rlt = self._eval()
            return (rlt == 1)

    # 返回所有使得CNF满足（T）或不满足（F）的model
    # 注意，调用此函数时，默认CNF中所有的commitment已进入终态
    # 返回结果形式，两个list，第一个list为T，第二个list为F
    # 形如T= [[judge(A,pay), !judge(B,mail)],[!judge(A,pay),judge(B,mail)]
    # 注意，需要特别处理 CNF中的 !judge literal
    def getAllModels(self):
        # 调用 pycosat 获取所有model，并构造一个字典
        # 字典的key 为 1*-2*3*-4
        models = {}
        for m in pycosat.itersolve(self._SATCore):
            # m is a list like [1, -2, -3, 4, 5]
            key = self._transAssignToKey(m)
            #print('model key:', key)
            models[key] = ''

        # 构建 2^len(alphabet) 个组合. 注意，我们假定一个前提中的judge数量很少
        # 构造这个组合的key，检查其是否在字典中
        # 根据检查结果，添加到 TList 或 FList中
        TList = []
        FList = []
        num = self._getNumDistinctLiterals()
        for idx in range(pow(2, num)):
            binstr = DEC2Bin(idx) # like 101
            if len(binstr)>num:
                binstr = binstr[1:] # 去掉最前面多余的0 TODO 这个很丑陋
            #有可能需要在前面补足 0
            while len(binstr) < num:
                binstr = '0' + binstr
            #print('binstr for idx(', idx, '):', binstr)
            key = self._transBinToKey(binstr)
            #print('key of binstr:', key)
            if (len(key)==0):
                print('ERROR with binstr, idx:', binstr, idx)
            if key in models:
                TList.append(self._transKeyToConAssignment(key))
            else:
                FList.append(self._transKeyToConAssignment(key))
        return TList, FList

    def enumClauseSet(self):
        return iter(self._clauseSet)

    #output  形如 Term1.Sat||judge()&&Term1.Vio||!judge()
    def toString(self):
        rlt = ''
        for cls in self._clauseSet:
            if len(rlt)>0:
                rlt += '&&'
            rlt += cls.toString()
        return rlt

    #根据_clauseSet 和 _alphabet 的内容, 更新 _SATCore
    def _updateSATCore(self):
        self._SATCore = []
        for cls in self._clauseSet:
            vars = []
            for lit in cls.enumLiterals():
                x = lit.getID()
                if lit.isNegative():
                    x = -x;
                vars.append(x)
            self._SATCore.append(vars)


    # 尝试在 alphabet 中加入一个 contractLiterlID, 若已经存在，返回已存在的literal
    # 否则，在alphabet中新增一个记录，返回新的literal
    # 注意：Term1.Sat 和 Term1.Vio 是两个literal，但是 它们的 contractLiteral ID 相同
    # 但是 judge(A,pay)和 !judge(A,pay) 是同一个literal id，也是同一个 contractLiteralID
    def _newLiteral(self, conLitID, val):
        # 先判断 alphabet中是否存在 conLitID + "-" + str(val)，若存在，返回相应literal
        # 否则，若 literal 为 judge，
        #     还需要判断 alphabet中是否存在 conLitID + "-" + str(!val) 若存在，须创建opposite
        key = conLitID + '-' + str(val)
        if key in self._alphabet:
            return self._alphabet[key]
        else:
            if not conLitID.startswith('Term'):
                if val == 1:
                    oppokey = conLitID + '-0'
                else:
                    oppokey = conLitID + '-1'
                #print ('val, oppokey, isKeyExists:', val, oppokey, (oppokey in self._alphabet))
                if oppokey in self._alphabet:
                    lit = self._alphabet[oppokey]
                    oppoLit = lit.createOpposite()
                    self._alphabet[conLitID + '-' + str(val)] = oppoLit
                    return oppoLit

        # 不管是literal还是 opposite literal都没出现过
        id = self._getNumDistinctLiterals() + 1
        newlit = Literal(id, conLitID)
        self._alphabet[key] = newlit
        newlit.setStatus(val)

        return newlit

    #input Term3: Term1.SAT||judge(A,pay)&&Term2.Vio||!judge(A,pay)  应转换为下面的list
    #  [ { "Term1":"3" , "judge(A,pay):"1" }, { "Term2":"5" , "judge(A,pay)":"0" }]
    def _format(self, premise):
        rlt = []
        for clsStr in re.split('[&&]', premise):
            group = {}
            if len(clsStr) == 0:
                continue
            else:
                for unit in re.split('[||]', clsStr):
                    unit = unit.lstrip().rstrip()
                    if len(unit) == 0:
                        continue
                    else:
                        if unit.startswith('Term'):
                            left,c,right = unit.partition('.')
                            left = left.lstrip().rstrip() # 去掉后面的空格
                            right = right.lstrip().rstrip() #去掉前后空格
                            val = 0
                            #print('unit:', unit)  #DEBUG
                            #print('left, c, right:', left, c, right) #DEBUG
                            if right.lower() == 'sat':
                                val = 3
                            elif right.lower() == 'exp':
                                val = 4
                            else:
                                val = 5
                            #print('left, val:', left, val) #DEBUG
                            group[left] = val
                            #print('group:', group) #DEBUG
                        else:
                            act = unit.lstrip().rstrip()
                            val = 1
                            if unit.startswith('!'):
                                act = act[1:]
                                val = 0
                            group[act] = val
            rlt.append(group)
        #print('result of _format():', rlt) #DEBUG
        return rlt

    # 调用 pycosat 来计算
    # 若为永真式，返回 1； 若为矛盾式，返回 0； 否则，返回 2
    def _eval(self):
        if len(self._clauseSet) == 0 or len(self._alphabet) == 0 :
            return 1 # 没有任何变量，必然永真式
        else:
            rlt = pycosat.solve(self._SATCore)
            if rlt == 'UNSAT':
                return 0
            else:
                rlt = len(list(pycosat.itersolve(self._SATCore)))
                if rlt >= pow(2, self._getNumDistinctLiterals())-0.00001: # TODO 这里的逻辑是否正确，需要测试
                    return 1
                else:
                    return 2

    # 获取 alphabet 中独立的（具有不同的 ID)的literal 数量
    def _getNumDistinctLiterals(self):
        dic = {}
        num = 0
        for k in self._alphabet:
            litID = self._alphabet[k].getID()
            if litID not in dic:
                num += 1
                dic[litID] = 1
        return num

    #input [1,-2,3]
    #output 1*-2*3
    def _transAssignToKey(self, assign):
        key = ''
        for i in range(len(assign)):
            key += str(assign[i])
            if i < len(assign)-1:
                key += '*'
        return key

    #input 01011
    #output -1*2*-3*4*5
    def _transBinToKey(self, binStr):
        rlt = ''
        for idx in range(len(binStr)):
            x = binStr[idx]
            if int(x) > 0:
                rlt += str(idx + 1)
            else:
                rlt += '-' + str(idx + 1)
            if idx < len(binStr) - 1:
                rlt += '*'
        return rlt

    def _printAlphabet(self):
        for key in self._alphabet:
            lit = self._alphabet[key]
            print(key, ':', lit.toString())
    # 注意 将 整数ID 换为相应的 contractLiteralID，并增加相应的 !
    #input 1*-2*3
    #output  [judge1(),!judge2(),judge3()]
    def _transKeyToConAssignment(self, key):
        dicStatus = {3:'Sat', 4:'Exp', 5:'Vio'}
        rlt = []
        for ch in re.split('[*]', key):
            x = int(ch)
            for litKey in self._alphabet:
                lit = self._alphabet[litKey]
                conLitID = litKey.partition('-')[0] # obtain Term1 or judge()

                if lit.getID() == x:
                    rlt.append(conLitID)
                elif lit.getID() == -x:
                    rlt.append('!' + conLitID)

                if lit.isCMT():
                    rlt.append( '.' + dicStatus[lit.getStatus()])

        #print('result for trans key(', key , '):', rlt)
        return rlt


#input 10
#output 1010
def DEC2Bin(dec):  # 将十进制转化为二进制
    if dec == 0:
        return '0'
    result = ""
    if dec:
        result = DEC2Bin(dec // 2)
        return result + str(dec % 2)
    else:
        return result

if __name__ == '__main__':
    cnf = CNF()
    premise = 'Term1.Sat'
    print('premise:', premise)
    cnf.build(premise)
    print('containsNonStoppedCMT:', cnf.containsNonStoppedCMT())
    print(cnf.getActions())
    print('original CNF:', cnf.toString())
    print('containsNonStoppedCMT:', cnf.containsNonStoppedCMT())
    print('containsAction:', cnf.containsAction())
    #tlist, flist = cnf.getAllModels() # TODO 此处结果有异常，若调用此函数只是在没有CMT情况下，目前代码可用
    print('###############################################')

    combinedChanges = {'Term1':2} #Input [[Term1：2], [Term2：3]] 字典

    cnf.updateCnf(combinedChanges)
    print('setting changes:', combinedChanges)
    print('updated cnf:', cnf.toString())
    print('containsNonStoppedCMT:', cnf.containsNonStoppedCMT())
    print('containsAction:', cnf.containsAction())
    print("isContradiction:",cnf.isContradiction())
    print("isTautology:",cnf.isTautology())

    #tlist, flist = cnf.getAllModels()

    #print('TList:', tlist)
    #print('FList:', flist)


