from  GNode import GNode
from NodeRepository import NodeRepository
import reduce
import json
import numpy as np
import operator
import generateGo
import generateSol
import copy
import re
import time
import pickle as pickle
import time
#DGA的类结构
#各个成员变量的含义
#root DGA的根节点 GNode
class DGA:
    #构造函数 构建DGA
    def __init__(self):
        self._root = GNode()    #初始化一个根节点
        self._Leaf = []
    def setRoot(self,inputdata): #设置根节点
        jsondata = self.json2python(inputdata)
        self._root.generateInitNode(jsondata)  # 设置根节点
    #构造整棵树
    def generateDGA(self):
        counter = 0
        transfer = []
        queue = []  # 建立节点队列
        queue.append(self._root)  # 根节点入队
        GNodeList = NodeRepository()
        GNodeList.addnode(self._root)
        starttime = time.time()
        while len(queue) > 0:  # 当队列不为空时
            counter = counter + 1
            if counter % 1000 == 0:
                endtime = time.time()
                print("已经处理的节点数:",counter)
                print("前一批节点总共耗时:",endtime - starttime)
                starttime = endtime

            trans = []
            node = queue.pop(0)  # 节点出队
            if node.isLeafNode() == True:
                self._Leaf.append(node)
                continue

            changeList = node.getAllChanges()  # 计算所有独立的变化   序号变id  {[[Term1,2],[Term2,3]],...}
            #print(changeList)
            for combinedChange in changeList:  # 每个变化的组合对应一条边
                chd,action = node.createChild(combinedChange)  # 根据父节点和复合边，生成子节点。生成过程中，更新子节点各承诺的premise
                chd.addParent(node.getId())  #将其父亲节点加入
                node.addChild(chd.getId())
                queue.append(chd)
                GNodeList.addnode(chd)
                action = ""
                trans = [node.getStates(),action,chd.getStates()]
                transfer.append(trans)
        #print(transfer)
        return (self._root.getStates(),transfer,self._root)
    def getLeaf(self):
        return self._Leaf
    def getDGARoot(self):     #获得初始节点
        return self._root
    @staticmethod
    def json2python(inputdata):
        data = json.loads(inputdata)
        return data
    # 合并叶子节点
    # Input
        # keyCmts  关键条款的列表
        # Leaf    叶子节点
        # NodeMapping 新旧节点id的映射字典
    #Output
        #upperNode 叶子节点的上层节点
    def mergeleaf(self, keyCmts, Leaf):
        upperNode = []      #叶子节点的上层节点
        mergeMap = {}       #节点的收益与id的映射
        for leaf in Leaf:
            parents = leaf.getParents()
            for parent in parents:
                if parent not in upperNode:
                    upperNode.append(parents)
            keyStates = []
            for i in keyCmts:
                keyStates.append(leaf.getStates()[i - 1])
            if str(keyStates) in mergeMap:
                mergeMap[str(keyStates)].append(leaf.getId())
            if str(keyStates) not in mergeMap:
                mergeMap[str(keyStates)]=[leaf.getId()]
        for key in mergeMap:
            newnode = Reduced_Gnode()
            for id in mergeMap[key]:
                node = getnode(id)
                parents = node.getParents()
                for parent in parents:
                    parent.update()  # TODO 参数还没确定 边集
                    newnode.addParent(parent.getId())
                remove(id)           # 从仓库中删除该合并过的节点,并更新映射集合
            addnode(newnode)
        return upperNode
    def mergeBranchNode(self,NodeList):
        upperNode = []             #初始化上层节点列表
        mergeMap1 = {}              #初始化映射字典 存储一个孩子节点的key
        mergeMap2 = {}              #初始化映射字典 存储交叉多个孩子节点的key
        for node in NodeList:      #扫描上层节点
            parents = node.getParents()                  #得到双亲节点
            for parent in parents:                       #如果不在upperNode中则入队
                if parent not in upperNode:
                    upperNode.append(parent)
                Children = node.getChildren()            #得到该节点的孩子节点
                if len(Children) == 1:                   #如果只有一个孩子节点
                    child = Children[0]
                    key = str(child.getId())
                    if key in mergeMap1:                      #如果当前键在字典中
                        mergeMap1[key].append(node.getId())
                    if key not in mergeMap1:                  #如果当前键不在字典中
                        mergeMap1[key] = [node.getId()]
                elif len(Children)!= 1:                  #如果不只有一个孩子节点
                    OutEdges = node.getOutedges()
                    childId = node.getChildrenId()
                    key = self.encode(OutEdges,childId)
                    if key in mergeMap2:                      #如果当前键在字典中
                        mergeMap2[key].append(node.getId())
                    if key not in mergeMap2:                  #如果当前键不在字典中
                        mergeMap2[key] = [node.getId()]
        for key in mergeMap1:
            self.merge1(key,mergeMap1[key])
        for key in mergeMap2:
            self.merge2(key, mergeMap2[key])
        return upperNode

    def merge1(self,key, value):
        edges = []
        newnode = Reduced_Gnode()
        newnode.addChild(int(key))
        for id in value:
            node.getnode(id)
            edge = node.getOutedges()
            edges.append(edge)
            parents = node.getParents()
            for parent in parents:
                parent.update()  # TODO
                newnode.addParent(parents)
            children = node.getChildren()
            for child in children:
                child.update()
            remove(id)
        newnode.addOutEdges()
        addnode(newnode)
    #合并节点的孩子节点怎样处理
    def merge2(self,key,value):
        newnode = Reduced_Gnode()
        edges,ids = parse(key)
        for edge in edges :
            newnode.addOutEdges(edges)
        for id in ids:
            newnode.addChild(id)
        for id in value:
            node = getnode(id)
            parents = node.getParents()
            for parent in parents:
                parent.update()                            #TODO
                newnode.addParent(parents)
            children = node.getChildren()
            for child in children:
                child.update()
            remove(id)
        addnode(newnode)
    def encode(self,edge,id):

    def parse(self,key):
    #化简DGA
    #Input
           #keyCmts  关键条款id的列表
           #Leaf  叶子节点的集合
    def reduceDFA(self,keyCmts,Leaf):
        upperNode = mergeleaf(keyCmts,Leaf)   #合并叶子节点
        while len(upperNode) != 0:                        #当上层节点不为空 即没到根节点
            upperNode = mergeBranchNode(upperNode)

def save_transfer(initState, transfers, contract_id):
    transfer_file = {'InitStatus': str(initState), "FsmArray": []}

    for i in range(0, len(transfers)):
        current_status = transfers[i][0]
        new_status =transfers[i][2]
        action = transfers[i][1]
        t = {'CurrentStatus': str(current_status), 'Action': action, 'NewStatus': str(new_status)}
        # print(transfers)
        transfer_file['FsmArray'].append(t)
    with open('./fsm/' + contract_id, 'w') as fs:
        fs.write(json.dumps(transfer_file, indent=2))

    generateGo.transferGo('./fsm/' + contract_id, './code/' + contract_id)
    generateSol.transferSolidity('./fsm/' + contract_id, './code/' + contract_id)


# 对外接口
def create_fsm(contract, contract_id):
    root = DGA()
    root.setRoot(contract)
    initState, transfer, DFA = root.generateDGA()
    #L , Leaf,GnodeList= root.Search()
    write_file = open('./MyWorkPlace/' + contract_id + '.pkl', 'wb')
    pickle.dump(DFA, write_file)
    write_file.close()
    save_transfer(initState, transfer, contract_id)

if __name__ == '__main__':
    data = input("jsonData")
    root = DGA()
    root.setRoot(data)
    root.generateDGA()
