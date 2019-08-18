from  GNode import GNode
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
    def setRoot(self,inputdata): #设置根节点
        jsondata = self.json2python(inputdata)
        self._root.generateInitNode(jsondata)  # 设置根节点
    #构造整棵树
    def generateDGA(self):
        counter = 0
        transfer = []
        queue = []  # 建立节点队列
        queue.append(self._root)  # 根节点入队
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
                continue
            changeList = node.getAllChanges()  # 计算所有独立的变化   序号变id  {[[Term1,2],[Term2,3]],...}
            #print(changeList)
            for combinedChange in changeList:  # 每个变化的组合对应一条边
                chd,action = node.createChild(combinedChange)  # 根据父节点和复合边，生成子节点。生成过程中，更新子节点各承诺的premise
                node.addChild(chd)
                queue.append(chd)
                action = ""
                trans = [node.getStates(),action,chd.getStates()]
                transfer.append(trans)
        #print(transfer)
        return (self._root.getStates(),transfer,self._root)
    def getDGARoot(self):     #获得初始节点
        return self._root
    @staticmethod
    def json2python(inputdata):
        data = json.loads(inputdata)
        return data
    def Search(self):
        queue = []  # 建立节点队列
        level = []  #用来存储节点的高度
        L = []  #存储节点的引用
        Leaf = []
        queue.append(self._root)  # 根节点入队
        level.append(self._root.getLevel())
        if self._root.isLeafNode == True:
            Leaf.append(child)
        L.append([self._root])
        while len(queue) > 0:
            node = queue.pop(0)
            Children = node.getChildren()
            for child in Children:
                if child.isLeafNode() == True:
                    Leaf.append(child)
                if child.getLevel() in level:
                    L[child.getLevel()].append(child)
                if child.getLevel() not in level:
                    level.append(child.getLevel())
                    L.append([child])
                queue.append(child)
        return L , Leaf
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
    L , Leaf= root.Search()
    write_file = open('./MyWorkPlace/' + contract_id + '.pkl', 'wb')
    pickle.dump(DFA, write_file)
    write_file.close()
    save_transfer(initState, transfer, contract_id)

if __name__ == '__main__':
    data = input("jsonData")
    root = DGA()
    root.setRoot(data)
    root.generateDGA()
