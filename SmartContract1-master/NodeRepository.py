#存储节点的仓库类    单例
class NodeRepository:
    def __init__(self):
        self._repository = []     #存储过程中需要的所有节点
        self._nodeId = []         #存储节点的id 便于存取
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
    def printl(self):
        return self._nodeId
    def getnum(self):
        return len(self._repository)
    def loadNodes(self,idList):
        nodes = []
        List = []          #避免重复取到相同的节点
        for id in idList:
            if id not in List:
                List.append(id)
                n = self.getnode(id)
                nodes.append(n)
        return nodes


nodeRepository = NodeRepository()
if __name__ == '__main__':
    GnodeList = NodeRepository()
    node = GNode()
    print(node)
    GnodeList.addnode(node)
    print(GnodeList.getnode(1))
    GnodeList.remove(1)
    print(GnodeList.getnode(1))
