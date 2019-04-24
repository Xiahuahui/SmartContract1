import CNF.LiteralPackage as lp

class Clause:
    def __init__(self, s):
        self.literalSet = []
        LiteralStr = s.split("||")
        if len(LiteralStr) == 0:
            return
        for i in range(len(LiteralStr)):
            literal = lp.Literal(LiteralStr[i])
            self.literalSet.append(literal)
        
    def isExist(self, literalStr):
        for l in self.literalSet:
            if literalStr == l.content:
                return True
        return False

    def deleteLiteral(self, literalStr):
        for l in self.literalSet:
            if literalStr == l.content:
                self.literalSet.remove(l)

    def getValue(self, valueMap):
        if len(self.literalSet) == 0:
            return True
        for l in self.literalSet:
            if valueMap[l.content] == True:
                return True
        return False
    
    def print(self):
        s = "("
        for l in self.literalSet:
            s = s+l.content+" || "
        s = s[:-4]
        s += ")"
        return s