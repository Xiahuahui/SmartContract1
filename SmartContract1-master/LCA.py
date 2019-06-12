import numpy as np
import payoff1
import time
#strategy=[[action],[action],[action]]
def getTreepos(strategy,rootId,GTnodeList):
	print(strategy);
	deep=0
	curNode = GTnodeList[rootId]
	while len(curNode.children) == 0:      #叶子节点
		i=0
		while i < len(curNode.children):
			childNode = curNode.children[i]
			j=0
			#检查边的所有动作是否都在策略中，不在的话就不是这个子节点，都在就是这个子节点
			isChild = True
			while j < len(childNode.edge):
				action = childNode.edge[j]
				if strategy.count(action)==0:
					isChild = False
					break
				else:
					j+=1
			if isChild==True:
				curNode=curNode.children
				deep+=1
				break;
			else:
				i+=1
	return [curNode.ID,deep]

def getSameDeep(node,deep,GTnodeList):
	if node[1]==deep:
		return node
	else:
		while node[1]>deep:
			parentId = GTnodeList[node[0]].edge[0][3]
			node[0] = parentId
			node[1]-=1
		return node

def getLCA(node1,node2,GTnodeList):
	node1ParentId = GTnodeList[node1[0]].edge[0][3]
	node2ParentId = GTnodeList[node2[0]].edge[0][3]
	while node2ParentId != node1ParentId:
		node1[0]=node1ParentId
		node1[1]-=1
		node2[0]=node2ParentId
		node2[1]-=1
		node1ParentId = GTnodeList[node1[0]].edge[0][3]
		node2ParentId = GTnodeList[node2[0]].edge[0][3]
	node1[0]=node1ParentId
	node1[1]-=1
	node2[0]=node2ParentId
	node2[1]-=1
	return node1


def getCA(nodes, GTnodeList):
	curNode = nodes[0]
	i=1
	while i<len(nodes):
		if curNode[1]<nodes[i][1]:
			nodes[i]=getSameDeep(nodes[i],curNode[1],GTnodeList)
		else:
			curNode = getSameDeep(curNode,nodes[i][1],GTnodeList)
		curNode = getLCA(curNode,nodes[i],GTnodeList)
		i+=1
	return curNode

def getBug(payoff,bestPos):
	m=bestPos[0]
	n = bestPos[1]

	payoff=np.array(payoff)
	print("转化后的矩阵")
	print(payoff)
	print(type(payoff))
	x = 1/payoff[m][n][1]
	y = 1/payoff[m][n][0]
	reA=[]
	reB=[]
	for i in range(payoff.shape[1]):
		if x*payoff[m][i][1]>1:
			reB.append([m,i])
	for j in range(payoff.shape[0]):
		if payoff[j][n][0]*y>1:
			reA.append([j,n])
	return reA,reB

def test(payoff,strategies,GTnodeList,bestPos):

	print(type(bestPos))
	bestPos = list(bestPos)
	print(type(bestPos))
	print(bestPos)
	m = bestPos[0]
	print(type(m))
	print(m)
	bugA,bugB = getBug(payoff,bestPos);
	print(bugA)
	print(bugB)

	bugATreePoss = []
	bugBTreePoss = []
	allNodes = []
	bestStrategy = strategies[bestPos[0]][bestPos[1]]
	bestTreePos = getTreepos(bestStrategy,0,GTnodeList)    #找到叶子节点
	for A in bugA:
		bugAstrategy = strategies[A[0]][A[1]]
		bugATreePos = getTreepos(bugAstrategy,0,GTnodeList)
		bugATreePoss.append(bugATreePos)
	for B in bugB:
		bugBstrategy = strategies[B[0]][B[1]]
		bugBTreePos = getTreepos(bugBstrategy,0,GTnodeList)
		bugBTreePoss.append(bugBTreePos)
	allNodes = bugATreePoss
	allNodes.extend(bugBTreePoss)
	allNodes.append(bestTreePos)
	print(allNodes)
	print(getCA(allNodes,GTnodeList))
	return getCA(allNodes,GTnodeList)
def check_payoff(contract, contract_id,bestPos):
	(GTnodeList,payoff,strategies)=payoff1.create_payoff(contract, contract_id)
	a = test(payoff,strategies,GTnodeList,bestPos)
	return a

if __name__ == '__main__':
	test(payoff,strategies,GTnodeList,bestPos)