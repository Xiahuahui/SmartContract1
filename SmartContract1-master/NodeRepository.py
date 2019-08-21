#存储节点的仓库类
from GNode import GNode
class NodeRepository:
    def __init__(self):
        self._repository = []     #存储过程中需要的所有节点
        self._nodeId = []         #存储节点的id 便于存取
        self._mapping = {}   #存储id 与 index 的映射关系
    #根据节点的id取到相应node
    def getnode(self,id):
        if id in self._nodeId:
            index = self._nodeId.index(id)
            return self._repository[index]
        else:

            return -1
    def remove(self,id):
        if id in self._nodeId:
            index = self._nodeId.index(id)
            del self._repository[index]
            del self._nodeId[index]
        else:
            print("没有该节点")
    def addnode(self,node):
        if node.getId() not in self._nodeId:
            self._repository.append(node)
            self._nodeId.append(node.getId())
if __name__ == '__main__':
    GnodeList = NodeRepository()
    node = GNode()
    print(node)
    GnodeList.addnode(node)
    print(GnodeList.getnode(1))
    GnodeList.remove(1)
    print(GnodeList.getnode(1))