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
            if settings.DEBUG == True:
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
                trans = [node.getStates(),action,chd.getStates()]
                transfer.append(trans)
                #if settings.DEBUG==True:
                    #print("transfer: ",transfer)
            nodeRepository.addnode(node)
        nodeRepository.saveLeafIdList(self.getLeafList(),GNode.Id)      #TODO check
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
        upperNodesMap = {}      #叶子节点的上层节点的id的字典
        mergeMap = {}       #节点的收益与id的映射
        if settings.DEBUG==True:
            file = "./log.text"
            print("叶节点的个数:   ",len(self._LeafIdList))
            string = "叶节点的个数:   "+str(len(self._LeafIdList))
            with open(file, 'a+') as f:
                f.write(string + '\n')

        counter = 0
        starttime = time.time()
        for leafId in self._LeafIdList:
            if settings.DEBUG==True:
                counter += 1
                if counter % 1000 == 0:
                    endtime = time.time()
                    print("已合并的叶结点个数:", counter)
                    print("合并这些叶结点耗时:", endtime - starttime)
                    starttime = endtime

            leaf = nodeRepository.getnode(leafId)
            parentsIdList = leaf.getParentsId()
            for parentId in parentsIdList:
                if parentId not in upperNodesMap:
                    upperNodesMap[str(parentId)] = ""

            keyStates = []
            for i in keyCmts:
                keyStates.append(leaf.getStates()[i-1])

            newnode = None

            if str(keyStates) in mergeMap:
                newnode = mergeMap[str(keyStates)]
            else:
                newnode = ReducedGnode()
                mergeMap[str(keyStates)] = newnode
            newnode.addState(leaf.getStates())
            parents = nodeRepository.loadNodes(leaf.getParentsId())
            for parent in parents:
                edge = parent.getOutEdge(leafId)
                edge.updateChildId(newnode.getId())
                parent.updateChildId(leafId,newnode.getId())
                nodeRepository.updateNode(parent,['outEdges','childrenId'])
                newnode.addParentId(parent.getId())      # TODO
            nodeRepository.remove(leafId)           # TODO 先暂停

        for newnode in mergeMap.values():
            nodeRepository.addnode(newnode)
        if settings.DEBUG==True:
            print("合并后叶结点的个数:   ", len(mergeMap))
            string1 = "合并后叶结点的个数:   " + str(len(mergeMap))
            with open(file, 'a+') as f:
                f.write(string1 + '\n')
        return list(upperNodesMap.keys()), list(mergeMap.values())

    def mergeBranchNode(self,NodeIdList, children):
        upperNodesMap = {}             #初始化上层节点列表
        mergeMap = {}              #初始化映射字典 存储孩子节点的key
        if settings.DEBUG==True:
            file = "./log.text"
            print("当前节点的个数:   ", len(NodeIdList))
            string = "当前节点的个数:   "+str(len(NodeIdList))
            with open(file, 'a+') as f:
                f.write(string + '\n')
        counter = 0
        for id in NodeIdList:      #扫描上层节点
            node = nodeRepository.getnode(int(id))
            if settings.DEBUG==True:
                counter += 1
                if counter % 1000 == 0:
                    print("mergeMap 大小:", len(mergeMap))
                    print("已处理的结点个数:", counter)

            for parentId in node.getParentsId():                       #如果不在upperNode中则入队
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
        if settings.DEBUG==True:
            print("合并后结点的个数:   ", len(mergeMap))
            string1 = "合并后结点的个数:   " + str(len(mergeMap))
            with open(file, 'a+') as f:
                f.write(string1 + '\n')
        mergedNodes = {}
        counter1 = 0
        starttime1 = time.time()
        for key in mergeMap:
            starttime = time.time()
            newNode,counter1,starttime1= self.merge(key, mergeMap[key],upperNodesMap,counter1,starttime1)
            if str(newNode.getId()) not in mergeMap:
                mergedNodes[str(newNode.getId())] = newNode
            endtime = time.time()
            if settings.DEBUG==True:
                print("待合并的key:", key)
                print("该key对应的结点个数:", len(mergeMap[key]))
                print("合并这些结点耗时:", endtime - starttime)
        #for id in children:
        #    nodeRepository.updateNode(children[id],['parentsId'])

        return list(upperNodesMap.keys()),mergedNodes

    # 更改一个将要被合并结点的上下层联系
    def updateNodeLinks(self,oldNode,newNode,upperNodeMap):
        parentEdgeMap = {}
        newNode.addState(oldNode.getStates())                           #TODO   错误的
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
            #nodeRepository.addNodeToBuffer(parent)
            nodeRepository.updateNode(parent,['outEdges','childrenId'])
            newNode.addParentId(parent.getId())
        
        children =[]
        for cid in oldNode.getChildrenId():
            child=nodeRepository.getnode(cid)
            children.append(child)
            nodeRepository.addNodeToBuffer(child)
            child.updateParentId(oldNode.getId(),newNode.getId())
            nodeRepository.updateNode(child,['parentsId'])

        if str(oldNode.getId()) in upperNodeMap:
            del upperNodeMap[str(oldNode.getId())]
            upperNodeIdList[newNode.getId()] = ""

        return parentEdgeMap


    #合并节点的孩子节点怎样处理
    def merge(self,key,toMergeIds,upperNodesMap,counter,starttime):
        newnode = ReducedGnode()
        if len(toMergeIds) == 1:
            GNode.Id = GNode.Id - 1
            node = nodeRepository.getnode(toMergeIds[0])
            newnode.copy(node)
            nodeRepository.updateNode(newnode,['CMTs','stateSet','type'])
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
                    if settings.DEBUG==True:
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
                    if settings.DEBUG==True:
                        counter = counter + 1
                        if counter % 1000 == 0:
                            endtime = time.time()
                            print("已合并的叶结点个数:", counter)
                            print("合并这些叶结点耗时:", endtime - starttime)
                            starttime = endtime
                    tempMap= self.updateNodeLinks(node, newnode, upperNodesMap)
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
                nodeRepository.updateNode(parent,['outEdges','childrenId'])
            nodeRepository.addnode(newnode)
        return newnode,counter,starttime

    @staticmethod
    #edges [e1,e2]
    #idList [id1,id2]
    #Output e1*id1#e2*id2
    def encode(edges):
        compositeList = []
        for i in range(len(edges)):
            compositeList.append([edges[i].toString(),edges[i].getChildId()])
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
        # print("当前的叶子个数:  ",len(self._LeafIdList))
        #upperNodeIds, newLeaves = self.mergeleaf(keyCmts)   #合并叶子节点
        #==========如果不需要保存到数据库可以注释======================
        #newIdList = []
        #for node in newLeaves:
        #    newIdList.append(node.getId())
        #nodeRepository.saveUpperNodeIds(upperNodeIds,newIdList)
        #input("mergeleaf end，please enter:")
        #==========如果不需要从数据库中读取mergeleaf之后的数据可以注释===============
        upperNodeIds,newLeaveIds=nodeRepository.getUpperNodeIds()
        GNode.Id=int(1690842)
        newLeaves = []
        for id in newLeaveIds:
            newLeaves.append(nodeRepository.getnode(id))
        #print(newLeaves)
        #input("stop.")

        # print("合并后的叶子数:  ",len(newLeaves))
        leavesUtil = []
        children = {}
        for leaf in newLeaves:
            ua = random.randint(1, 50)
            ub = random.randint(1, 50)
            item = [leaf, ua, ub]
            leavesUtil.append(item)
            children[str(leaf.getId())] = leaf
        #print("upperNodes ",upperNodes)


        toMergeNodeIds = upperNodeIds
        i = 0
        while True:#当上层节点不为空 即没到根节点
            if i == 2:
                print("A")
            upperNodeIds,mergedNodes= self.mergeBranchNode(toMergeNodeIds,children)
            #print("newUpperNodes:",newUpperNodes)
            if len(upperNodeIds) == 0:
                break
            else:
                toMergeNodeIds = upperNodeIds
                children = mergedNodes
            i = i+1
        # if settings.DEBUG:
        #     print(root,root.getId())
        #TODO 从根遍历生成Transfer
        nodeRepository.bufferUpdateToDB()
        root = list(mergedNodes.values())[0]
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
    initState1, transfer1, DFA1,leavesUtil= root.reduceDFA([1])
    #search(DFA1)
    A,B = createStrategies(DFA1)
    print("输出")
    #search(DFA1)
    createPayoffMatrix(A, B, DFA1, leavesUtil)
    # print(DFA1.getStates())
    # print(DFA1.getId())
    # print(nodeRepository.printl())
    #outEdges = DFA1.getOutEdges()
    # for id in outEdges:
    #     print(id.toString())
    print("A")
    print("B")
    print("后",nodeRepository.getnum())
    print("输出")
    # search(DFA1)
    write_file = open('./MyWorkPlace/' + contract_id + '.pkl', 'wb')
    pickle.dump(DFA, write_file)
    write_file.close()
    save_transfer(initState, transfer, contract_id)
    save_transfer1(initState1, transfer1, contract_id)

def saveReduceResultToFile(state,trans,root,leavesUtil):
    file = "../reduceResult.txt"
    reduceResultDict={
        'state':state,
        'trans':trans,
        'rootId':root.getId(),
        'leavesUtil':leavesUtil
    }
    with open(file, 'wb') as f:
        pickle.dump(reduceResultDict,f)

def readReduceResultFromFile():
    file = "../reduceResult.txt"
    with open(file,'rb') as f:
        reduceResult=pickle.load(f)
    return reduceResult

if __name__ == '__main__':
    #file = open("../Bigcontract.text",'r')
    #data=file.read()
    #root = DGA()
    #root.setRoot(data)
    #root.generateDGA()
    # print("化简前的节点数量", nodeRepository.getnum())
    # root.reduceDFA([3])
    # print("化简后的节点数量", nodeRepository.getnum())
    #input("enter:")
    # =============第二步==========================
    root = DGA()
    root._root = nodeRepository.getnode(1)
    root._LeafIdList, GNode.Id = nodeRepository.getLeafIdList()
    #print(root._LeafIdList)
    print("化简前的节点数量", nodeRepository.getnum())
    state, trans, root, leavesUtil = root.reduceDFA([12,19])
    #saveReduceResultToFile(state,trans,root,leavesUtil)
    print("化简后的节点数量", nodeRepository.getnum())
    #reduceResult=readReduceResultFromFile()







