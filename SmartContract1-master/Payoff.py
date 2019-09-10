import numpy as np
from Edges import *
import copy
from NodeRepository import nodeRepository
from Settings import settings
from Choices import *
from Strategy import *
class Path:
     def __init__(self):
         self._compEdges = []
         self._ua = -1
         self._ub = -1
     def setUtility(self,values):
         self._ua = values[0]
         self._ub = values[1]
     def getUtility(self):
         return [self._ua,self._ub]
     def appendEdge(self,ce):
         self._compEdges.append(ce)
     def getPathChoices(self):
         pathChoiceA = []
         pathChoiceB = []

         for ce in self._compEdges:
             ChoiceA, ChoiceB = ce.getAllChoices()  # TODO we need to add nodeID into CompositeEdge
             if ChoiceA.isEmpty() == False:
                pathChoiceA.append(ChoiceA)
             if ChoiceB.isEmpty() == False:
                pathChoiceB.append(ChoiceB)
         pathChoiceA = Choice.removeDupChoices(pathChoiceA)
         pathChoiceB = Choice.removeDupChoices(pathChoiceB)

         return pathChoiceA,pathChoiceB

     # 如果匹配,则返回 utility 的值 ua1, ub1 (>=0)
     # 否则, 返回 -1, -1   注意, 假设 utility值均为非负
     def findUtility(self, straA, straB):
         # path的所有
         if settings.DEBUG:
            print("StraA:  ",straA.toString())
            print("StraB:   ",straB.toString())

         pathChoicesA, pathChoicesB = self.getPathChoices()

         if settings.DEBUG:
            print("pathChoicesA: ")
            printChoicesSet(pathChoicesA)
            print("pathChoicesB: ")
            printChoicesSet(pathChoicesB)

         if straA.contain(pathChoicesA) and straB.contain(pathChoicesB):
             return self.getUtility()
         else:
             if settings.DEBUG:
                print("不能匹配")
             return [-1, -1]
     def toString(self):
         rlt = ""
         for ce in self._compEdges:
             rlt += ce.toString()+"//"
         return rlt
def printChoicesSet(choicesSet):
    for choice in choicesSet:
        print (choice.toString())
# @leavesUtil 所有叶节点的utility值, [[leafNode1, ua1, ub1],...]
def getUtility(node, leavesUtil):
    for item in leavesUtil:
        leaf = item[0]
        if node.getId() == leaf.getId():
            return [item[1], item[2]]
# @subtreeRoot : 子树的根节点
# @path : 从根到 subtreeRoot 的路径
# @output 从subtreeRoot 展开的到叶节点的所有路径的集合
def getAllPaths(subtreeRoot, path,leavesUtil):
    children = nodeRepository.loadNodes(subtreeRoot.getChildrenId())  # 直接取得是策略
    rlt = []
    if len(children) == 0:  # 如果是叶子节点,则直接返回 @path
        utils = getUtility(subtreeRoot, leavesUtil)
        path.setUtility(utils)
        path.toString()
        rlt.append(path)
        return rlt
    else:
        for child in children:  # 如果不是叶子节点   则在原来的策略上加上一条边
            # outEdges = subtreeRoot.getOutEdges()
            # for ce in outEdges:
            #     print(ce.getChildId())
            # print()
            # print(child.getId())
            outEdge = subtreeRoot.getOutEdge(child.getId())
            newPath = copy.deepcopy(path)
            newPath.appendEdge(outEdge)
            rlt.extend(getAllPaths(child, newPath, leavesUtil))
        return rlt


#@straSetA, @straSetB  两个player的策略集
#@leavesUtil 所有叶节点的utility值, [[leafNode1, ua1, ub1],...]

def createPayoffMatrix(straSetA, straSetB,root,leavesUtil):
    print("调用")
    initPath = Path()
    paths = getAllPaths(root, initPath, leavesUtil)    #得到所有的路径
    if settings.DEBUG:
        print("num of paths:", len(paths))
    length1 = len(straSetA)
    length2 = len(straSetB)
    matrixA = np.zeros((length1,length2))
    matrixB = np.zeros((length1, length2))
    for i in range(length1):
        for j in range(length2):
            for p in paths:
                ua1, ub1 =  p.findUtility(straSetA[i],straSetB[j])
                if ua1 >= 0:
                    matrixA[i][j] = ua1
                    matrixB[i][j] = ub1
                    break
    if settings.DEBUG:
        print("收益矩阵A")
        print(matrixA)
        print("收益矩阵B")
        print(matrixB)
if __name__ == '__main__':
    print()
