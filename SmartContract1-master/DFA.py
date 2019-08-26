from GNode import *
from NodeRepository import nodeRepository
from ReduceGNode import ReducedGnode
import json
import generateGo
import generateSol
import pickle as pickle
import time
from Edges import *
from Strategy import createStrategies
from Payoff import *
import random
from Settings import *
#DGA的类结构
#各个成员变量的含义
#root DGA的根节点 GNode
class DGA:
    #构造函数 构建DGA
    def __init__(self):
        self._root = GNode()    #初始化一个根节点
        self._LeafIdList = []
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
                self._LeafIdList.append(node.getId())
                nodeRepository.addnode(node)
                continue

            changeList = node.getAllChanges()  # 计算所有独立的变化   序号变id  {[[Term1,2],[Term2,3]],...}
            #print(changeList)
            for combinedChange in changeList:  # 每个变化的组合对应一条边
                chd,action = node.createChild(combinedChange)  # 根据父节点和复合边，生成子节点。生成过程中，更新子节点各承诺的premise
                chd.addParentId(node.getId())  #将其父亲节点加入
                queue.append(chd)
                action = ""
                trans = [node.getStates(),action,chd.getStates()]
                transfer.append(trans)
            nodeRepository.addnode(node)
        nodeRepository.saveLeafIdList(self.getLeafList(),GNode.Id)
        #print(transfer)
        return (self._root.getStates(),transfer,self._root)
    def getLeafList(self):
        return self._LeafIdList
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
    def mergeleaf(self, keyCmts):
        newLeaves = []
        upperNodesIdList = []      #叶子节点的上层节点的id的列表
        mergeMap = {}       #节点的收益与id的映射
        for leafId in self._LeafIdList:
            leaf = nodeRepository.getnode(leafId)
            parentsIdList = leaf.getParentsId()
            for parentId in parentsIdList:
                if parentId not in upperNodesIdList:
                    upperNodesIdList.append(parentId)
            keyStates = []
            for i in keyCmts:
                keyStates.append(leaf.getStates()[i-1])
            # print("keyStates:",keyStates)
            if str(keyStates) in mergeMap:
                mergeMap[str(keyStates)].append(leaf.getId())
                # print(mergeMap)
            else:
                mergeMap[str(keyStates)]=[leaf.getId()]
                # print(mergeMap)
        for key in mergeMap:
            newnode = ReducedGnode()
            newLeaves.append(newnode)
            for id in mergeMap[key]:
                node = nodeRepository.getnode(id)
                newnode.addState(node.getStates())
                parents = nodeRepository.loadNodes(node.getParentsId())
                for parent in parents:
                    edge = parent.getOutEdge(id)
                    edge.updateChildId(newnode.getId())
                    parent.updateChildId(id,newnode.getId())
                    nodeRepository.updateNode(parent)
                    newnode.addParentId(parent.getId())
                nodeRepository.remove(id)           # 从仓库中删除该合并过的节点,并更新映射集合
            nodeRepository.addnode(newnode)
        # for node in self._LeafList:
        #     print("当前节点的状态",node.getStates(),node.getId())
        # print(mergeMap)
        if settings.DFA == True:
            print(upperNodesIdList)
        return upperNodesIdList, newLeaves
    def mergeBranchNode(self,NodeIdList):
        upperNodesIdList = []             #初始化上层节点列表
        mergeMap = {}              #初始化映射字典 存储孩子节点的key
        for id in NodeIdList:      #扫描上层节点
            node = nodeRepository.getnode(id)
            parentsIdList = node.getParentsId()                 #得到双亲节点
            for parentId in parentsIdList:                       #如果不在upperNode中则入队
                if parentId not in upperNodesIdList:
                    upperNodesIdList.append(parentId)

            Children = nodeRepository.loadNodes(node.getChildrenId())  # 得到该节点的孩子节点
            if len(Children) == 1:  # 如果只有一个孩子节点
                child = Children[0]
                key = str(child.getId())
                if key in mergeMap:  # 如果当前键在字典中
                    mergeMap[key].append(node.getId())
                else:  # 如果当前键不在字典中
                    mergeMap[key] = [node.getId()]
            else:  # 如果不只有一个孩子节点

                OutEdges = node.getOutEdges()
                IdList = node.getChildrenId()
                key = self.encode(OutEdges, IdList)
                if key in mergeMap:  # 如果当前键在字典中
                    mergeMap[key].append(node.getId())
                else:  # 如果当前键不在字典中
                    mergeMap[key] = [node.getId()]

        # for node in NodeList:
        #     print("当前节点的状态",node.getStates(),node.getId())
        # print(mergeMap)

        for key in mergeMap:
            root = self.merge(key, mergeMap[key],upperNodesIdList)

        return upperNodesIdList,root
    #合并节点的孩子节点怎样处理
    def merge(self,key,value,upperNodesIdList):
        newnode = ReducedGnode()
        if "#" in key:     #当含有#时,说明有多条边
            node = nodeRepository.getnode(value[0])
            for edge in node.getOutEdges() :
                edge.updateParentId(newnode.getId())     #TODO   实现
                newnode.addOutEdge(edge)        #TODO 是否用深copy
            for cid in node.getChildrenId():
                newnode.addChildId(cid)
            nodeRepository.updateNode(node)
        else:
            cid = 0
            dict = {}
            for id in value:
                node = nodeRepository.getnode(id)
                OutEdges = node.getOutEdges()
                for edge in OutEdges:
                    if edge.toString() not in dict:  #多个节点可能有重复的边
                        dict[edge.toString()] = edge
                #nodeRepository.updateNode(node)
                cid = node.getChildrenId()[0]
            newnode.addChildId(cid)    #此种情况下所有待合并节点均只有一个相同的孩子
            outEdge = CompositeEdge(newnode.getId(),cid)
            for h in dict:
                outEdge.mergeEdge(dict[h])
            newnode.addOutEdge(outEdge)

        for id in value:
            node = nodeRepository.getnode(id)
            newnode.addState(node.getStates())
            ids = node.getParentsId()
            parents = nodeRepository.loadNodes(ids)
            for parent in parents:
                edge = parent.getOutEdge(id)
                edge.updateChildId(newnode.getId())
                parent.updateChildId(id,newnode.getId())
                nodeRepository.updateNode(parent)                            #TODO
                newnode.addParentId(parent.getId())
            children = nodeRepository.loadNodes(node.getChildrenId())
            for child in children:
                child.updateParentId(id,newnode.getId())
                nodeRepository.updateNode(child)
            if id in upperNodesIdList:
                # newid = newnode.getId()#Mapping[str(id)]
                # changenode = nodeRepository.getnode(newid)
                index = upperNodesIdList.index(id)
                upperNodesIdList[index] = newnode.getId()
            nodeRepository.remove(id)
        nodeRepository.addnode(newnode)
            #print(id," has been removed")
        #print("ChildrenId: ",newnode.getChildrenId())
        root = newnode
        return root

    @staticmethod
    #edges [e1,e2]
    #idList [id1,id2]
    #Output e1*id1#e2*id2
    def encode(edges,idList):
        compositeList = []
        for i in range(len(edges)):
            compositeList.append([edges[i].toString(),idList[i]])
        # print(compositeList)
        l1 = sorted(compositeList, key=lambda ei: ei[1])
        rlt = ""
        for ei in l1:
            rlt += ei[0]+"*"+str(ei[1])+"#"
        rlt = rlt[:-1]
        return rlt
    #化简DGA
    #Input
           #keyCmts  关键条款id的列表
           #Leaf  叶子节点的集合
    def reduceDFA(self,keyCmts):
        #print("调用")
        upperNodes, newLeaves = self.mergeleaf(keyCmts)   #合并叶子节点
        leavesUtil = []
        for leaf in newLeaves:
            ua = random.randint(1, 50)
            ub = random.randint(1, 50)
            item = [leaf, ua, ub]
            leavesUtil.append(item)
        root = ''
        #print("upperNodes ",upperNodes)
        while True:#当上层节点不为空 即没到根节点
            newUpperNodes,root= self.mergeBranchNode(upperNodes)
            #print("newUpperNodes:",newUpperNodes)
            if len(newUpperNodes) == 0:
                break

            else:
                upperNodes = newUpperNodes

        # if settings.DEBUG:
        #     print(root,root.getId())
        #TODO 从根遍历生成Transfer
        trans = getTransfer(root)
        return (root.getStates(), trans, root, leavesUtil)
    def search(self):
        queue = []
        queue.append(self._root)
        while len(queue) != 0:
            node = queue.pop(0)
            print(node.getId())
            print(node.getStates())
            children = nodeRepository.loadNodes(node.getChildrenId())
            for child in children:
                queue.append(child)


def getTransfer(root):
    trans = []
    queue = []
    Mapping = {}
    queue.append(root)
    Mapping[str(root.getId())] = ""
    while len(queue) != 0:
        node = queue.pop(0)
        trans.extend(buildNodeTransfer(node))
        children = nodeRepository.loadNodes(node.getChildrenId())
        for child in children:
            if str(child.getId()) not in Mapping:
                queue.append(child)
                Mapping[str(child.getId())] = ""
    return trans

def buildNodeTransfer(node):
    trans = []
    children = nodeRepository.loadNodes(node.getChildrenId())
    for child in children:
        trans.append([node.getStates(), "", child.getStates()])
    return trans

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
def save_transfer1(initState, transfers, contract_id):
    transfer_file = {'InitStatus': str(initState), "FsmArray": []}

    for i in range(0, len(transfers)):
        current_status = transfers[i][0]
        new_status =transfers[i][2]
        action = transfers[i][1]
        t = {'CurrentStatus': str(current_status), 'Action': action, 'NewStatus': str(new_status)}
        # print(transfers)
        transfer_file['FsmArray'].append(t)
    with open('./fsm1/' + contract_id, 'w') as fs:
        fs.write(json.dumps(transfer_file, indent=2))

# 对外接口
def create_fsm(contract, contract_id):
    root = DGA()
    root.setRoot(contract)
    initState, transfer, DFA = root.generateDGA()
    #print("叶子节点:    ",root.getLeafList())
    print("前",nodeRepository.getnum())
    initState1, transfer1, DFA1,A = root.reduceDFA([3])
    A,B = createStrategies(DFA1)
    print("A")
    print("B")
    print("后",nodeRepository.getnum())
    write_file = open('./MyWorkPlace/' + contract_id + '.pkl', 'wb')
    pickle.dump(DFA, write_file)
    write_file.close()
    save_transfer(initState, transfer, contract_id)
    save_transfer1(initState1, transfer1, contract_id)
if __name__ == '__main__':
    file = open("../Bigcontract.text",'r')
    data=file.read()
    root = DGA()
    root.setRoot(data)
    root.generateDGA()
    #root.search()
    #root = DGA()
    #root._root = nodeRepository.getnode(1)
    #root._LeafIdList,GNode.Id = nodeRepository.getLeafIdList()
    #print(root._LeafIdList)
    #================单元测试======================
    print("化简前的节点数量", nodeRepository.getnum())
    input("enter:")
    #=================合并叶子节点==================
    # upperNodesIdList1, newLeaves = root.mergeleaf([1])
    # print("upperNodesIdList1:   ",upperNodesIdList1)
    # print(nodeRepository.printl())
    #=================合并分支节点==================
    # upperNodesIdList2 = root.mergeBranchNode(upperNodesIdList1)
    # print("upperNodesIdList2:   ",upperNodesIdList2)
    # print(nodeRepository.printl())
    # upperNodesIdList3 = root.mergeBranchNode(upperNodesIdList2)
    # print("upperNodesIdList3:   ",upperNodesIdList3)
    # print(nodeRepository.printl())
    state, trans, root, leavesUtil = root.reduceDFA([1])
    print("化简后的节点数量", nodeRepository.getnum())
    # # #root.search()
    # # upperNodes = root.mergeleaf([3])
    # # for node in upperNodes:
    # #     print(node.getStates())
    # # upperNodes = root.mergeBranchNode(upperNodes)
    # # print("化简后的节点数量",nodeRepository.getnum())
    # # upperNodes = root.mergeBranchNode(upperNodes)
    # # print("化简后的节点数量",nodeRepository.getnum())
    # # upperNodes = root.mergeBranchNode(upperNodes)
    # # print("化简后的节点数量",nodeRepository.getnum())
    # States,trans,newRoot, leavesUtil = root.reduceDFA([1])
    #
    # print("化简后的节点数量", nodeRepository.getnum())
    # print(States,trans,newRoot)
    nodeIdList = nodeRepository.printl()
    print(nodeIdList)
    for id in nodeIdList:
        node = nodeRepository.getnode(id)
        print(node.getStateSet())
        print(node.getStates())
    #straSetA, straSetB = createStrategies(root)

    #
    #
    #createPayoffMatrix(straSetA, straSetB, root, leavesUtil)




