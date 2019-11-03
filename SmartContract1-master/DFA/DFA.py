import sys
sys.path.append(".")
import random
from Settings import settings,saveResultToFile,readResultFromFile
import pickle as pickle
import time
import json
from .generateCode import transferGo,transferSolidity
from .db import GNode,ReducedGnode,nodeRepository,Edge,CompositeEdge
# DGA的类结构
# 各个成员变量的含义
# root DGA的根节点 GNode
class DGA:
    # 构造函数 构建DGA
    def __init__(self):
        self._root = GNode()  # 初始化一个根节点
        self._LeafIdList = []

    def setRoot(self, inputdata):  # 设置根节点
        jsondata = self.json2python(inputdata)
        self._root.generateInitNode(jsondata)  # 设置根节点

    # 构造整棵树
    def generateDGA(self):
        counter = 0
        # transfer = []
        queue = []
        queue.append(self._root)  # 根节点入队
        starttime = time.time()
        while len(queue) > 0:  # 当队列不为空时
            if settings.DEBUG == True:
                counter = counter + 1
                if counter % 1 == 0:
                    endtime = time.time()
                    print("已经处理的节点数:", counter)
                    print("前一批节点总共耗时:", endtime - starttime)
                    starttime = endtime
            node = queue.pop(0)
            if node.isLeafNode() == True:
                self._LeafIdList.append(node.getId())
                nodeRepository.addnode(node)
                continue

            changeList = node.getAllChanges()  # 计算所有独立的变化   序号变id  {[[Term1,2],[Term2,3]],...}
            # print(changeList)
            for combinedChange in changeList:  # 每个变化的组合对应一条边
                chd, action = node.createChild(combinedChange)  # 根据父节点和复合边，生成子节点。生成过程中，更新子节点各承诺的premise
                chd.addParentId(node.getId())  # 将其父亲节点加入
                queue.append(chd)
                # trans = [node.getStates(), action, chd.getStates()]
                # transfer.append(trans)
            nodeRepository.addnode(node)
        nodeRepository.saveLeafIdList(self.getLeafList(), GNode.Id)  # TODO check
        transfer = getTransfer(self._root)
        # leafIdList, _ = nodeRepository.getLeafIdList()
        # leaves = nodeRepository.loadNodes(leafIdList)
        # leavesUtil = []
        # for leaf in leaves:
        #     ua = random.randint(1, 50)
        #     ub = random.randint(1, 50)
        #     item = [leaf, ua, ub]
        #     leavesUtil.append(item)
        return (self._root.getStates(), transfer)

    def getLeafList(self):
        return self._LeafIdList

    def getDGARoot(self):  # 获得初始节点
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
    # Output
    # upperNode 叶子节点的上层节点
    def mergeleaf(self, keyCmts,classfiy):
        upperNodesMap = {}  # 叶子节点的上层节点的id的字典
        mergeMap = {}  # 节点的收益与id的映射
        for i in range (len(classfiy)):
            mergeMap[str(i+1)] = []
        if settings.DEBUG == True:
            file = "./log.text"
            print("叶节点的个数:   ", len(self._LeafIdList))
            string = "叶节点的个数:   " + str(len(self._LeafIdList))
            with open(file, 'a+') as f:
                f.write(string + '\n')

        counter = 0
        starttime = time.time()
        for leafId in self._LeafIdList:
            if settings.DEBUG == True:
                counter += 1
                if counter % 1000 == 0:
                    endtime = time.time()
                    print("已合并的叶结点个数:", counter)
                    print("合并这些叶结点耗时:", endtime - starttime)
                    starttime = endtime
            print("当前的叶子节点",leafId)
            print("当前数据库的节点:",nodeRepository.printl())
            leaf = nodeRepository.getnode(leafId)
            parentsIdList = leaf.getParentsId()
            for parentId in parentsIdList:
                if parentId not in upperNodesMap:
                    upperNodesMap[str(parentId)] = ""

            keyStates = []
            for i in keyCmts:
                keyStates.append(leaf.getStates()[i - 1])
            for i in range(len(classfiy)):
                if keyStates in classfiy[i]:
                    mergeMap[str(i+1)].append(leafId)
                    break
        mergedNodes = {}
        counter1 = 0
        starttime1 = time.time()
        for key in mergeMap:
            starttime = time.time()
            newNode, counter1, starttime1 = self.mergeLeafNode(mergeMap[key], counter1, starttime1)
            if str(newNode.getId()) not in mergedNodes:
                mergedNodes[str(newNode.getId())] = newNode
            endtime = time.time()
            if settings.DEBUG == True:
                print("待合并的key:", key)
                print("该key对应的结点个数:", len(mergeMap[key]))
                print("合并这些结点耗时:", endtime - starttime)
        for newnode in mergedNodes.values():
            nodeRepository.addnode(newnode)
        if settings.DEBUG == True:
            print("合并后叶结点的个数:   ", len(mergedNodes))
            string1 = "合并后叶结点的个数:   " + str(len(mergedNodes))
            with open(file, 'a+') as f:
                f.write(string1 + '\n')
        return list(upperNodesMap.keys()), list(mergedNodes.values())

    def mergeLeafNode(self, toMergeIds, counter, starttime):
        newnode = ReducedGnode()
        parentEdgeMap = {}
        for id in toMergeIds:
            if settings.DEBUG == True:
                counter = counter + 1
                if counter % 1000 == 0:
                    endtime = time.time()
                    print("已合并的叶子结点个数:", counter)
                    print("合并这些叶子结点耗时:", endtime - starttime)
                    starttime = endtime
            node = nodeRepository.getnode(id)
            newnode.addState(node.getStates())
            for pid in node.getParentsId():
                parent = nodeRepository.getnode(pid)
                nodeRepository.addNodeToBuffer(parent)
                if str(pid) not in parentEdgeMap:
                    parentEdgeMap[str(pid)] = []
                edge = parent.getOutEdge(id)
                parentEdgeMap[str(pid)].append(edge)
                parent.removeOutEdge(edge.getChildId())
                edge.updateChildId(newnode.getId())
                parent.updateChildId(id, newnode.getId())
                nodeRepository.updateNode(parent, ['outEdges', 'childrenId'])
                newnode.addParentId(parent.getId())
            nodeRepository.remove(id)  # TODO 先暂停
        for pid in parentEdgeMap:
            parent = nodeRepository.getnode(int(pid))
            edges = parentEdgeMap[pid]
            ce0 = edges[0]
            parent.addOutEdge(ce0)
            if len(edges) > 1:
                for idx in range(1, len(edges)):
                    ce0.mergeEdge(edges[idx])
            nodeRepository.delNodeFromBuffer(parent)
            nodeRepository.updateNode(parent, ['outEdges','childrenId'])
        return newnode, counter, starttime
    def mergeBranchNode(self, NodeIdList):
        upperNodesMap = {}  # 初始化上层节点列表
        mergeMap = {}  # 初始化映射字典 存储孩子节点的key
        if settings.DEBUG == True:
            file = "./log.text"
            print("当前节点的个数:   ", len(NodeIdList))
            string = "当前节点的个数:   " + str(len(NodeIdList))
            with open(file, 'a+') as f:
                f.write(string + '\n')
        counter = 0
        for id in NodeIdList:  # 扫描上层节点
            node = nodeRepository.getnode(int(id))
            if settings.DEBUG == True:
                counter += 1
                if counter % 1000 == 0:
                    print("mergeMap 大小:", len(mergeMap))
                    print("已处理的结点个数:", counter)

            for parentId in node.getParentsId():  # 如果不在upperNode中则入队
                if parentId not in upperNodesMap:
                    upperNodesMap[str(parentId)] = ""

            if len(node.getChildrenId()) == 1:  # 如果只有一个孩子节点
                childId = node.getChildrenId()[0]
                key = str(childId)
                if key in mergeMap:  # 如果当前键在字典中
                    mergeMap[key].append(node.getId())
                else:  # 如果当前键不在字典中
                    mergeMap[key] = [node.getId()]
            else:  # 如果不只有一个孩子节点
                OutEdges = node.getOutEdges()
                key = self.encode(OutEdges)
                if key in mergeMap:  # 如果当前键在字典中
                    mergeMap[key].append(node.getId())
                else:  # 如果当前键不在字典中
                    mergeMap[key] = [node.getId()]
        if settings.DEBUG == True:
            print("合并后结点的个数:   ", len(mergeMap))
            string1 = "合并后结点的个数:   " + str(len(mergeMap))
            with open(file, 'a+') as f:
                f.write(string1 + '\n')
        mergedNodes = {}
        counter1 = 0
        starttime1 = time.time()
        for key in mergeMap:
            starttime = time.time()
            newNode, counter1, starttime1 = self.merge(key, mergeMap[key], upperNodesMap, counter1, starttime1)
            if str(newNode.getId()) not in mergedNodes:
                mergedNodes[str(newNode.getId())] = newNode
            endtime = time.time()
            if settings.DEBUG == True:
                print("待合并的key:", key)
                print("该key对应的结点个数:", len(mergeMap[key]))
                print("合并这些结点耗时:", endtime - starttime)
        # for id in children:
        #    nodeRepository.updateNode(children[id],['parentsId'])

        return list(upperNodesMap.keys()), mergedNodes

    # 更改一个将要被合并结点的上下层联系
    def updateNodeLinks(self, oldNode, newNode, upperNodeMap):
        parentEdgeMap = {}
        newNode.addState(oldNode.getStates())  # TODO   错误的
        for pid in oldNode.getParentsId():
            parent = nodeRepository.getnode(pid)
            nodeRepository.addNodeToBuffer(parent)
            if str(pid) not in parentEdgeMap:
                parentEdgeMap[str(pid)] = []
            edge = parent.getOutEdge(oldNode.getId())
            parentEdgeMap[str(pid)].append(edge)
            parent.removeOutEdge(edge.getChildId())
            edge.updateChildId(newNode.getId())
            parent.updateChildId(oldNode.getId(), newNode.getId())
            # nodeRepository.addNodeToBuffer(parent)
            nodeRepository.updateNode(parent, ['outEdges', 'childrenId'])
            newNode.addParentId(parent.getId())

        for cid in oldNode.getChildrenId():
            child = nodeRepository.getnode(cid)
            nodeRepository.addNodeToBuffer(child)
            child.updateParentId(oldNode.getId(), newNode.getId())
            nodeRepository.updateNode(child, ['parentsId'])

        if str(oldNode.getId()) in upperNodeMap:
            del upperNodeMap[str(oldNode.getId())]
            upperNodeIdList[newNode.getId()] = ""

        return parentEdgeMap

    # 合并节点的孩子节点怎样处理
    def merge(self, key, toMergeIds, upperNodesMap, counter, starttime):
        newnode = ReducedGnode()
        if len(toMergeIds) == 1:
            GNode.Id = GNode.Id - 1
            node = nodeRepository.getnode(toMergeIds[0])
            newnode.copy(node)
            nodeRepository.updateNode(newnode, ['CMTs', 'stateSet', 'type'])
        else:
            parentEdgeMap = {}
            if "#" in key:  # 当含有#时,说明有多条边
                node = nodeRepository.getnode(toMergeIds[0])
                for edge in node.getOutEdges():
                    edge.updateParentId(newnode.getId())
                    newnode.addOutEdge(edge)  # TODO 是否用深copy
                for cid in node.getChildrenId():
                    newnode.addChildId(cid)
                for id in toMergeIds:
                    node = nodeRepository.getnode(id)
                    if settings.DEBUG == True:
                        counter = counter + 1
                        if counter % 1000 == 0:
                            endtime = time.time()
                            print("已合并的分支结点个数:", counter)
                            print("合并这些分支结点耗时:", endtime - starttime)
                            starttime = endtime
                    tempMap = self.updateNodeLinks(node, newnode, upperNodesMap)
                    for pid in tempMap:
                        if pid not in parentEdgeMap:
                            parentEdgeMap[pid] = tempMap[pid]
                        else:
                            parentEdgeMap[pid].extend(tempMap[pid])
                    # parentEdgeMap.update(tempMap)
                    nodeRepository.remove(id)

            else:
                cid = 0
                dict = {}
                for id in toMergeIds:
                    node = nodeRepository.getnode(id)
                    OutEdges = node.getOutEdges()
                    for edge in OutEdges:
                        if edge.toString() not in dict:  # 多个节点可能有重复的边
                            dict[edge.toString()] = edge
                    if settings.DEBUG == True:
                        counter = counter + 1
                        if counter % 1000 == 0:
                            endtime = time.time()
                            print("已合并的叶结点个数:", counter)
                            print("合并这些叶结点耗时:", endtime - starttime)
                            starttime = endtime
                    tempMap = self.updateNodeLinks(node, newnode, upperNodesMap)
                    for pid in tempMap:
                        if pid not in parentEdgeMap:
                            parentEdgeMap[pid] = tempMap[pid]
                        else:
                            parentEdgeMap[pid].extend(tempMap[pid])
                    cid = node.getChildrenId()[0]
                    nodeRepository.remove(id)
                newnode.addChildId(cid)  # 此种情况下所有待合并节点均只有一个相同的孩子

                outEdge = CompositeEdge(newnode.getId(), cid)
                for h in dict:
                    outEdge.mergeEdge(dict[h])
                newnode.addOutEdge(outEdge)

            for pid in parentEdgeMap:
                parent = nodeRepository.getnode(int(pid))
                edges = parentEdgeMap[pid]
                ce0 = edges[0]
                parent.addOutEdge(ce0)
                if len(edges) > 1:
                    for idx in range(1, len(edges)):
                        ce0.mergeEdge(edges[idx])
                nodeRepository.delNodeFromBuffer(parent)
                nodeRepository.updateNode(parent, ['outEdges', 'childrenId'])
            nodeRepository.addnode(newnode)
        return newnode, counter, starttime

    @staticmethod
    # edges [e1,e2]
    # idList [id1,id2]
    # Output e1*id1#e2*id2
    def encode(edges):
        compositeList = []
        for i in range(len(edges)):
            compositeList.append([edges[i].toString(), edges[i].getChildId()])
        # print(compositeList)
        l1 = sorted(compositeList, key=lambda ei: ei[1])
        rlt = ""
        for ei in l1:
            rlt += ei[0] + "*" + str(ei[1]) + "#"
        rlt = rlt[:-1]
        return rlt

    # 化简DGA
    # Input
    # keyCmts  关键条款id的列表
    # Leaf  叶子节点的集合
    def reduceDFA(self, keyCmts,classfiy):
        upperNodeIds, newLeaves = self.mergeleaf(keyCmts,classfiy)   #合并叶子节点
        leavesUtil = []
        for leaf in newLeaves:
            ua = random.randint(1, 50)
            ub = random.randint(1, 50)
            item = [leaf, ua, ub]
            leavesUtil.append(item)
        toMergeNodeIds = upperNodeIds
        while True:  # 当上层节点不为空 即没到根节点
            upperNodeIds, mergedNodes = self.mergeBranchNode(toMergeNodeIds)
            if len(upperNodeIds) == 0:
                break
            else:
                toMergeNodeIds = upperNodeIds
        nodeRepository.bufferUpdateToDB()
        root = list(mergedNodes.values())[0]
        trans = getTransfer(root)
        return (root.getStates(), trans, root, leavesUtil)

def search(root):
    queue = []
    queue.append(root)
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
        trans.append([node.getStates(), node.getOutEdge(child.getId()).toShow(), child.getStates()])
    return trans


def save_transfer(initState, transfers, contract_id):
    transfer_file = {'InitStatus': str(initState), "FsmArray": []}

    for i in range(0, len(transfers)):
        current_status = transfers[i][0]
        new_status = transfers[i][2]
        action = transfers[i][1]
        t = {'CurrentStatus': str(current_status), 'Action': action, 'NewStatus': str(new_status)}
        # print(transfers)
        transfer_file['FsmArray'].append(t)
    with open('./data/fsm/' + contract_id, 'w') as fs:
        fs.write(json.dumps(transfer_file, indent=2))


def save_Reducedtransfer( initState, transfers, contract_id):
    transfer_file = {'InitStatus': str(initState), "FsmArray": []}

    for i in range(0, len(transfers)):
        current_status = transfers[i][0]
        new_status = transfers[i][2]
        action = transfers[i][1]
        t = {'CurrentStatus': str(current_status), 'Action': action, 'NewStatus': str(new_status)}
        # print(transfers)
        transfer_file['FsmArray'].append(t)
    with open('./data/reducedFsm/' + contract_id, 'w') as fs:
        fs.write(json.dumps(transfer_file, indent=2))
        print("存放化简")
# 对外接口 创建状态机
def create_fsm(contract, contract_id):
    # 初始化一个状态机
    print("###################初始化状态机##################")
    DFA = DGA()
    DFA.setRoot(contract)
    rootId = DFA.getDGARoot().getId()
    initState, transfer = DFA.generateDGA()
    dfaNodes = nodeRepository.loadAllNodes()
    leavesIdsList = DFA.getLeafList()
    saveResultToFile(DFA,dfaNodes,rootId,leavesIdsList,'./data/MyWorkPlace/fsm/' + contract_id + '.pkl')
    save_transfer(initState, transfer, contract_id)
    nodeRepository.cleanTable()
    print("################初始化状态机完成##################")
#对外接口 化简状态机
def create_Reducedfsm(contract_id):
    print("################化简状态机完成##################")
    dfaResult = readResultFromFile('./data/MyWorkPlace/fsm/' + contract_id + '.pkl')
    DFA = dfaResult['DFA']
    dfaNodes = dfaResult['dfaNodes']
    nodeRepository.initRepository(dfaNodes)
    initState, transfer, root, leavesUtil = DFA.reduceDFA([1],[[[3]],[[4]],[[5]]])
    rootId = DFA.getDGARoot().getId()
    leavesIdsList = DFA.getLeafList()
    saveResultToFile(DFA, dfaNodes, rootId,leavesIdsList,'./data/MyWorkPlace/reducedFsm/' + contract_id + '.pkl')
    save_Reducedtransfer(initState, transfer, contract_id)
    nodeRepository.cleanTable()
    print("################化简状态机完成##################")
def generateCode(fsmPath,codePath):
    transferGo(fsmPath,codePath)
    transferSolidity(fsmPath,codePath)


if __name__ == '__main__':
    # file = open("../Bigcontract.text", 'r')
    data = input("输入")
    root = DGA()
    root.setRoot(data)
    root.generateDGA()
    input("导出状态机化简之前的节点: ")
    initState1, transfer1, DFA1, leavesUtil = root.reduceDFA([1],[[[3]],[[4]],[[5]]])
    print("结束")
    # saveReduceResultToFile(initState1,transfer1,DFA1,leavesUtil)
    # input("导出状态机化简之后的节点: ")
    # Nodes = nodeRepository.loadAllNodes()
    # mydb3 = open('dbase3', 'wb')  # 存储化简之后的节点
    # pickle.dump(Nodes, mydb3)
    # input("求策略组合转化为内存模式: ")
    mydb3 = open('dbase3', 'rb')
    Nodes = pickle.load(mydb3)
    nodeRepository.initRepository(Nodes)
    DFA1 = nodeRepository.getnode(1)
    # rlt = readReduceResultFromFile()
    # DFA1 = nodeRepository.getnode(rlt["rootId"])
    C, D,E,F = reduceStrategies(DFA1)
    # mydb = open('AAA', 'wb')
    # pickle.dump(C, mydb)
    # mydb = open('BBB', 'wb')
    # pickle.dump(D, mydb)
    # input("第三步求纳什均衡:")
    # mydb3 = open('dbase3', 'rb')
    # Nodes = pickle.load(mydb3)
    # nodeRepository.initRepository(Nodes)
    # mydb = open('AAA', 'rb')
    # C = pickle.load(mydb)
    # mydb = open('BBB', 'rb')
    # D = pickle.load(mydb)
    # rlt = readReduceResultFromFile()
    # leavesUtil = rlt['leavesUtil']
    # DFA1 = nodeRepository.getnode(rlt["rootId"])
    # createPayoffMatrix(C, D, DFA1, leavesUtil)
