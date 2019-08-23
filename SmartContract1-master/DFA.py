from  GNode import GNode
from NodeRepository import nodeRepository
from ReduceGNode import ReducedGnode
import json
import generateGo
import generateSol
import pickle as pickle
import time
from Settings import settings
#DGA的类结构
#各个成员变量的含义
#root DGA的根节点 GNode
class DGA:
    #构造函数 构建DGA
    def __init__(self):
        self._root = GNode()    #初始化一个根节点
        self._LeafList = []
    def setRoot(self,inputdata): #设置根节点
        jsondata = self.json2python(inputdata)
        self._root.generateInitNode(jsondata)  # 设置根节点
    #构造整棵树
    def generateDGA(self):
        counter = 0
        transfer = []
        queue = []  # 建立节点队列
        queue.append(self._root)  # 根节点入队
        nodeRepository.addnode(self._root)
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
                self._LeafList.append(node)
                continue

            changeList = node.getAllChanges()  # 计算所有独立的变化   序号变id  {[[Term1,2],[Term2,3]],...}
            #print(changeList)
            for combinedChange in changeList:  # 每个变化的组合对应一条边
                chd,action = node.createChild(combinedChange)  # 根据父节点和复合边，生成子节点。生成过程中，更新子节点各承诺的premise
                chd.addParentId(node.getId())  #将其父亲节点加入
                queue.append(chd)
                nodeRepository.addnode(chd)
                action = ""
                trans = [node.getStates(),action,chd.getStates()]
                transfer.append(trans)
        #print(transfer)
        return (self._root.getStates(),transfer,self._root)
    def getLeafList(self):
        return self._LeafList
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
        upperNodes = []      #叶子节点的上层节点
        mergeMap = {}       #节点的收益与id的映射
        # print("List: ",self._LeafList)
        for leaf in self._LeafList:
            parents = leaf.getParents()
            for parent in parents:
                if parent not in upperNodes:
                    upperNodes.append(parent)
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
            nodeRepository.addnode(newnode)
            for id in mergeMap[key]:
                node = nodeRepository.getnode(id)
                newnode.addState(node.getStates())
                parents = node.getParents()
                for parent in parents:
                    # print("更新前的孩子id",parent.getChildrenId())
                    # children = parent.getChildren()
                    # for child in children:
                    #     print(child.getStates())
                    parent.updateChildId(id,newnode.getId())  # TODO 只需要该边父亲节点的孩子id换成newnodeid
                    # print("更新后的孩子id", parent.getChildrenId())
                    # children = parent.getChildren()
                    # for child in children:
                    #     print(child.getStates())
                    newnode.addParentId(parent.getId())
                nodeRepository.remove(id)           # 从仓库中删除该合并过的节点,并更新映射集合
        # for node in self._LeafList:
        #     print("当前节点的状态",node.getStates(),node.getId())
        # print(mergeMap)
        return upperNodes
    def mergeBranchNode(self,NodeList):
        upperNodes = []             #初始化上层节点列表
        mergeMap = {}              #初始化映射字典 存储孩子节点的key
        for node in NodeList:      #扫描上层节点
            parents = node.getParents()                  #得到双亲节点
            for parent in parents:                       #如果不在upperNode中则入队
                if parent not in upperNodes:
                    upperNodes.append(parent)

            Children = node.getChildren()  # 得到该节点的孩子节点
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
            self.merge(key, mergeMap[key],upperNodes)

        return upperNodes
    #合并节点的孩子节点怎样处理
    def merge(self,key,value,upperNodes):
        #print("value:  ",value)
        #Mapping = { }    #存储新旧节点的映射"oldId":"newId"
        newnode = ReducedGnode()
        nodeRepository.addnode(newnode)
        if "#" in key:     #当含有#时,说明有多条边
            #print(key)
            #print(value)
            node = nodeRepository.getnode(value[0])
            for edge in node.getOutEdges() :
                #print(edge.toString())
                newnode.addOutEdge(edge)        #TODO 是否用深copy
            for cid in node.getChildrenId():
                newnode.addChildId(cid)
        else:
            cid = 0
            dict = {}
            for id in value:
                node = nodeRepository.getnode(id)
                OutEdges = node.getOutEdges()
                for edge in OutEdges:
                    if edge.toHash() not in dict:
                        dict[edge.toHash()] = edge
                cid = node.getChildrenId()[0]
            for h in dict:
                newnode.addOutEdge(dict[h]) #TODO 用一个就行
                newnode.addChildId(cid)
        for id in value:
            # print(id)
            #Mapping[str(id)] = newnode.getId()
            node = nodeRepository.getnode(id)
            newnode.addState(node.getStates())
            parents = node.getParents()                          #TODO 名称规范
            ids = node.getParentsId()
            # print("双亲节点的id",ids)
            for parent in parents:
                # print(parent)
                parent.updateChildId(id,newnode.getId())                            #TODO
                newnode.addParentId(parent.getId())
            children = node.getChildren()
            for child in children:
                child.updateParentId(id,newnode.getId())
            if node in upperNodes:
                # newid = newnode.getId()#Mapping[str(id)]
                # changenode = nodeRepository.getnode(newid)
                index = upperNodes.index(node)
                upperNodes[index] = newnode
            nodeRepository.remove(id)
            #print(id," has been removed")
        #print("ChildrenId: ",newnode.getChildrenId())


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
            rlt += str(ei[0])+"*"+str(ei[1])+"#"
        rlt = rlt[:-1]
        return rlt
    #化简DGA
    #Input
           #keyCmts  关键条款id的列表
           #Leaf  叶子节点的集合
    def reduceDFA(self,keyCmts):
        #print("调用")
        upperNodes = self.mergeleaf(keyCmts)   #合并叶子节点
        #print("upperNodes ",upperNodes)
        while True:#当上层节点不为空 即没到根节点
            newUpperNodes= self.mergeBranchNode(upperNodes)
            #print("newUpperNodes:",newUpperNodes)
            if len(newUpperNodes) == 0:
                break
            else:
                upperNodes = newUpperNodes
        root = upperNodes[0]
        # if settings.DEBUG:
        #     print(root,root.getId())
        #TODO 从根遍历生成Transfer
        trans = getTransfer(root)
        return (root.getStates(), trans, root)
    def search(self):
        queue = []
        queue.append(self._root)
        while len(queue) != 0:
            node = queue.pop(0)
            # print(node.getParentsId())
            # print(node.getStates())
            # print(node.getChildrenId())
            children = node.getChildren()
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
        trans.extend(node.getTransfer())
        children = node.getChildren()
        for child in children:
            if str(child.getId()) not in Mapping:
                queue.append(child)
                Mapping[str(child.getId())] = ""
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
    initState1, transfer1, DFA1 = root.reduceDFA([3])
    print("后",nodeRepository.getnum())
    write_file = open('./MyWorkPlace/' + contract_id + '.pkl', 'wb')
    pickle.dump(DFA, write_file)
    write_file.close()
    save_transfer(initState, transfer, contract_id)
    save_transfer1(initState1, transfer1, contract_id)
if __name__ == '__main__':
    data = input("jsonData")
    root = DGA()
    root.setRoot(data)
    root.generateDGA()
    print("化简前的节点数量", nodeRepository.getnum())
    # #root.search()
    # upperNodes = root.mergeleaf([3])
    # for node in upperNodes:
    #     print(node.getStates())
    # upperNodes = root.mergeBranchNode(upperNodes)
    # print("化简后的节点数量",nodeRepository.getnum())
    # upperNodes = root.mergeBranchNode(upperNodes)
    # print("化简后的节点数量",nodeRepository.getnum())
    # upperNodes = root.mergeBranchNode(upperNodes)
    # print("化简后的节点数量",nodeRepository.getnum())
    trans = root.reduceDFA([3])

    print(trans)