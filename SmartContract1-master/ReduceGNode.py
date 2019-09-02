# 化简相应的状态机
from  GNode import GNode
#合并后的节点,GNode的子类
class ReducedGnode(GNode):
    def __init__(self):
        GNode.__init__(self)
        self._type="ReducedGnode"
        self._stateSet = []
    def addState(self,st):
        self._stateSet.append(st)
    def getStates(self):    #TODO  返回第一个state 应该修改
        return self._stateSet[0]
    def getStateSet(self):
        return self._stateSet
    def setStateSet(self,stateSet):
        self._stateSet=stateSet
    def getType(self):
        return self._type
    def copy(self,node):
        self._id = node.getId()
        self._OutEdges = node.getOutEdges()
        self.setChildrenId(node.getChildrenId())
        self.setParentsId(node.getParentsId())
        self._stateSet.append(node.getStates())

if __name__ == '__main__':
    node = ReducedGnode()
    node1 = GNode()
    print(node.getId())
    print(node1.getId())












