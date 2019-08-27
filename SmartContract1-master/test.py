# def compare(x,y):
#     return x<y
# student_tuples = [
#         ('john', 'A', 10),
#         ('jane', 'B', 12),
#         ('dave', 'B', 10),
# ]
# l1 = sorted(student_tuples,key = lambda student: str(student[2])+","+str(student[1]))
# print(str(l1))
# from NodeRepository import nodeRepository
# from GNode import GNode
# import random
#
# print (random.randint(1, 50))

# nodeRepository.remove(1)
# print(GnodeList.getnode(1))
# node2 = ReducedGnode()
# nodeRepository.addnode(node2)
# print(node2.getId())
import itertools
A = [[1,2],[3,4]]
B = []
# for l in itertools.product(*A):
#     B.extend(l)
for i in range(1,len(A)):
    print(A[i])
print(B)
