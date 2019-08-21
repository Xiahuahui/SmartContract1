# 化简相应的状态机
from GNode import GNode
#合并后的节点,GNode的子类
class Reduced_Gnode(GNode):
    def __init__(self):
        GNode.__init__(self)

if __name__ == '__main__':
    node = Reduced_Gnode()
    node1 = GNode()
    print(node.getId())
    print(node1.getId())












