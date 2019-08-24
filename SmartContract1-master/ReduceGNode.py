# 化简相应的状态机
from  GNode import GNode
#合并后的节点,GNode的子类
class ReducedGnode(GNode):
    def __init__(self):
        GNode.__init__(self)
        self._stateSet = []
    def addState(self,st):
        self._stateSet.append(st)
    def getStates(self):    #TODO  返回第一个state 应该修改
        return self._stateSet[0]

if __name__ == '__main__':
    node = ReducedGnode()
    node1 = GNode()
    print(node.getId())
    print(node1.getId())












