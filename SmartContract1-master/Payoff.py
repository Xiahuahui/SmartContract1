import nashpy as nash
import numpy as np
from Edges import *
import copy
from NodeRepository import nodeRepository
from Settings import settings
from Choices import *
from Strategy import *
import time
class Path:
     def __init__(self):
         self._compEdges = []
         self._ua = -1
         self._ub = -1
     def setUtility(self,values):
         print("values",values)
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
         pathChoiceA = Choice.removeDupChoices2(pathChoiceA)
         pathChoiceB = Choice.removeDupChoices2(pathChoiceB)

         return pathChoiceA,pathChoiceB

     # 如果匹配,则返回 utility 的值 ua1, ub1 (>=0)
     # 否则, 返回 -1, -1   注意, 假设 utility值均为非负
     def findUtility(self, straA, straB):
         pathChoicesA, pathChoicesB = self.getPathChoices()
         if straA.contain(pathChoicesA) and straB.contain(pathChoicesB):
             return self.getUtility()
         else:
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
    return [-1,-1]
# @subtreeRoot : 子树的根节点
# @path : 从根到 subtreeRoot 的路径
# @output 从subtreeRoot 展开的到叶节点的所有路径的集合
def getAllPaths(subtreeRoot, path,leavesUtil):
    children = nodeRepository.loadNodes(subtreeRoot.getChildrenId())  # 直接取得是策略
    rlt = []
    if len(children) == 0:  # 如果是叶子节点,则直接返回 @path
        utils = getUtility(subtreeRoot, leavesUtil)
        print("zhuangtai :",subtreeRoot.getStates(),utils)
        path.setUtility(utils)
        path.toString()
        rlt.append(path)
        return rlt
    else:
        for child in children:  # 如果不是叶子节点   则在原来的策略上加上一条边
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
    file = "./path.text"
    with open(file, 'a+') as f:
        f.write(str(len(paths)) + '\n')
    length1 = len(straSetA)
    length2 = len(straSetB)
    matrixA = np.zeros((length1,length2))
    matrixB = np.zeros((length1, length2))
    counter = 0
    # starttime = time.time()
    for i in range(length1):
        for j in range(length2):
            for p in paths:
                print("当前的路径",p.toString())
                ua1, ub1 =  p.findUtility(straSetA[i],straSetB[j])
                counter += 1
                # if counter % 100 == 0:
                #     endtime = time.time()
                #     print("已匹配的个数:", counter)
                #     print("匹配这些路径:", endtime - starttime)
                #     starttime = endtime
                if ua1 >= 0:
                    matrixA[i][j] = ua1
                    matrixB[i][j] = ub1
                    break
    if settings.DEBUG:
        print("收益矩阵A")
        print(matrixA)
        print("收益矩阵B")
        print(matrixB)
        print(matrixA[0][0])
        print(matrixB[0][0])
        print(straSetA[0].toString())
        print(straSetB[0].toString())
    return matrixA,matrixB
def createReducedPayoffMatrix(straSetA, straSetB,leavesUtil):
    length1 = len(straSetA)
    length2 = len(straSetB)
    matrixA = np.zeros((length1,length2))
    matrixB = np.zeros((length1, length2))
    counter = 0
    starttime = time.time()
    for i in range(length1):
        for j in range(length2):
            counter = counter + 1
            if counter % 100 == 0:
                    endtime = time.time()
                    print("已匹配的个数:", counter)
                    print("匹配这些路径:", endtime - starttime)
                    starttime = endtime
            ua1, ub1 = straSetA[i].findUtility(straSetB[j],leavesUtil)
            if ua1 >= 0:
                matrixA[i][j] = ua1
                matrixB[i][j] = ub1
    if settings.DEBUG:
        print("收益矩阵A")
        print(matrixA)
        print("收益矩阵B")
        print(matrixB)
    return matrixA ,matrixB
#求解两个矩阵的纳什均衡
def nash (matrixA,matrixB):    #输入收益矩阵     输出纳什均衡点
    toyple = matrixA.shape
    matrixB = matrixB.T
    print(toyple[0])
    row = toyple[0]
    column = toyple[1]
    Alable = [0]*row        #存储每个节点A的lable ,收益矩阵的行数,即第一个人的纯策略
    Blable = [0]*column        #存储每个节点B的lable ,收益矩阵的列数,即第二个人的纯策略
    for i in range(row):            #找出每个策略的收益,并且找出最大收益
        Max = []
        Alable[i] = []
        for m in range(row):
            if m != i:
                Alable[i].append(m)
        for j in range(column):
            Max.append(matrixB[j][i])
        M = max(Max)
        for q in range(len(Max)):                  #找到最佳即为lable
            if Max[q] == M:
                Alable[i].append(row+q)
    for j in range(column):
        Blable[j]=[]        #初始化y的lable即x分量为0的下标加1
        Max = []
        for m in range(column):
            if m != j:
                Blable[j].append(row+m)

        for i in range(row):
                Max.append(matrixA[i][j])
        M = max(Max)                  #找到最佳即为lable
        for q in range(len(Max)):
            if Max[q] == M:
                Blable[j].append(q)
    for i in range (row):
        print("x"+str(i),Alable[i])
    for j in range(column):
        print("y"+str(j),Blable[j])
    Nash = []                   #寻找纳什均衡点 即lable中包含(1到m +n中的所有数值即为纳什均衡点)
    for i in range (row):
        for j in range(column):
            lable = []
            lable.extend(Alable[i])
            lable.extend(Blable[j])
            flage = 1
            for k in range(row + column):
                if k not in lable:
                    flage = 0
                    break
            if flage == 1:
                nash = [i,j]
                Nash.append(nash)
    print("纳什均衡点: ", Nash)
    return Nash

if __name__ == '__main__':
    print()
