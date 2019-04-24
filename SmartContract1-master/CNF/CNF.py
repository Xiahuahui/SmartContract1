import CNF.ClausePackage as cp

class CNF:
    def __init__(self):
        self.clauseSet = []

    def build(self, s):
        if s == "":
            return
        clauseStr = s.split("&&")
        if len(clauseStr) == 0:
            return
        for i in range(len(clauseStr)):
            clause = cp.Clause(clauseStr[i])
            self.clauseSet.append(clause)
        
    def isExist(self, literalStr):
        for c in self.clauseSet:
            if c.isExist(literalStr) == True:
                return True
        return False

    def deleteLiteral(self, literalStr):
        for c in self.clauseSet:
            c.deleteLiteral(literalStr)
            if len(c.literalSet) == 0:
                self.clauseSet.remove(c)

    def getValue(self, valueMap):
        res = True
        for c in self.clauseSet:
            res = res and c.getValue(valueMap)
        return res        

    def print(self):
        s = ""
        for c in self.clauseSet:
            s = s+c.print()+" && "
        s=s[:-4]
        print(s)


if __name__ == "__main__":
    Vmap = {"a":True,"b":False,"c":False,"d":False,"e":True}
    print(Vmap)
    # while(True):
    #     expr = input("input cnf:")
    #     cnf = CNF()
    #     cnf.build(expr)
    #     cnf.print()
    #     print("value: ",cnf.getValue(Vmap))
    expr = "a&&b||e&&c||e"
    cnf = CNF()
    cnf.build(expr)
    cnf.print()
    print("value: ", cnf.getValue(Vmap))

    print("delete a")
    cnf.deleteLiteral("a")
    cnf.print()
    print("value: ",cnf.getValue(Vmap))

    print("delete e")
    cnf.deleteLiteral("e")
    cnf.print()
    print("value: ",cnf.getValue(Vmap))

    print("delete b")
    cnf.deleteLiteral("b")
    cnf.print()
    print("value: ",cnf.getValue(Vmap))

    print("delete c")
    cnf.deleteLiteral("c")
    cnf.print()
    print("value: ",cnf.getValue(Vmap))
