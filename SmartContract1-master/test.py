# def compare(x,y):
#     return x<y
# student_tuples = [
#         ('john', 'A', 10),
#         ('jane', 'B', 12),
#         ('dave', 'B', 10),
# ]
# l1 = sorted(student_tuples,key = lambda student: str(student[2])+","+str(student[1]))
# print(str(l1))
from NodeRepository import nodeRepository
from GNode import GNode

node = GNode()
node1 = GNode()
l = []
l2 = []
l = [node,node1,node]
for i in l:
    if i not in l2:
        l2.append(i)
print(l2)
# nodeRepository.remove(1)
# print(GnodeList.getnode(1))
# node2 = ReducedGnode()
# nodeRepository.addnode(node2)
# print(node2.getId())