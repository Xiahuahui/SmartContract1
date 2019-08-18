# 化简相应的状态机
import DFA
# 实现每层节点的引用
# L1,L2,L3,...,Lk 引用每层的节点
class Reduced_Gnode:
    Id = 0
    def __init__(self):
        Reduced_Gnode.Id = Reduced_Gnode.Id + 1
        self._id = str(Reduced_Gnode.Id) + "r"  # Gnode 的id 具有唯一性
#合并叶子节点
Input : keyCmts [3,5,6,...] #关键性条款的序号
　　　　　Leaf [Gnode,Gnode,] #叶子节点的列表
def mergeleaf(keyCmts,Leaf):
    group = []
    groupby = []
    for leaf in Leaf:
        keyStates = []
        for i in keyCmts:
            keyStates.append(leaf.getStates()[i-1])
        if keyStates in group:
            index = group.index(keyStates)
            groupby[index].append(leaf.getId())
        if keyStates not in group:
            group.append(keyStates)
            groupby.append([leaf.getId()])
    for g in groupby:
        rnode = Reduced_Gnode()
        for id in g:
            parent = Gnode.getParent(id)
            parent.changeChild(id,rnode)
#Input:
        # DFA DFA的初始化节点
        # L 每层节点的引用
def mergeBranchNode(DFA,L):
    mergeMap = {}
    H = DFA.getheight
    for h in range(H-1,-1,-1):
        for node in L[h]:
            edges = node.getOutedges[]
            childrenId = node.getOuteNodeId[]
            for i in range (len(edges)):
                key = edges[i] + str(childrenId[i])
                if key in mergeMap:
                    mergeMap[key].append(node.getId())
                if key not in mergeMap:
                    mergeMap[key] = [node.getId()]
        for k in mergeMap:
            if len(mergeMap[k]) > 0:
                merge(k,mergeMap[k])
#Input :
    # key   #要合并的节点的边集
    # value #要合并节点的Id
def merge(key , value):
    newnode = Gnode()
    parse(key)
    for id in value:
        parent = Gnode.getParent(id)
        parent.changeChild(id)
        parent.changeedge(id,edge)
def parse(key):











