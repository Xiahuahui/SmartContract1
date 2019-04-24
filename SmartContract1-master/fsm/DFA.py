## python 3.6.1
import json
import numpy as np
import operator
import graphviz as gz
import pygraphviz as pgv

# DFS遍历的节点
class St_node:                              # 定义了状态机中一个合理状态节点
    def __init__(self, Id, S, matrix):
        self.Id = Id               
        self.S = S
        self.m = matrix
    def print_content(self):
        print(self.Id)
        print(self.S)

# 生成的状态机，与前端相适应
class Transfer:
    def __init__(self, current, action, newS):
        self.current = current
        self.action = action
        self.newS = newS
    def print_content(self):
        print("==========Transfer==========")
        print(self.current)
        print(self.action)
        print(self.newS)

# 博弈树节点
class node:                                  
    def __init__(self,actperson,edge,data):
        self._actperson = actperson    #生成该节点的动作方
        self._data = data             #该节点的状态
        self._edge = edge             # 生成该节点的行动
        self._children = []     #定义该节点的孩子列表
 
    def getactperson(self):
        return self._actperson      #得到该节点的动作发出者
    def getdata(self):
        return self._data      #得到该节点的动作发出者
    def getchildren(self):       #得到孩子列表
        return self._children

    def getedge(self):           #得到该节点的入边
        return self._edge

    def getedges(self):           #得到该节点的所有出边
        Edge = []
        for child in self._children:
            edge=child.getedge()
            Edge.append(edge)
        return Edge

    def add(self, node):
        self._children.append(node)   #向树中加入节点



#================ DFA节点 =========================
# 与生成game tree算法对接
class Gnode:                     #定义一个FSM节点的结构                       
    def __init__(self):

        self._children = []     #定义该节点的孩子列表
 

    def getchildren(self):       #得到孩子列表
        return self._children


    def add(self, node):
        self._children.append(node)   #向树中加入节点

# 状态机DFA生成算法
def generate(jsondata):
    print ("start generate:")
    print ("")

    # get data & decode
    #jsondata = input("json data:")
    data = json2python(jsondata)
    print(len(data))
    # state num
    n = len(data)

    # =============================================================
    # initial state - n dim vector [1, 1, ..., 1]
    initState = np.ones(n)

    # 找到正确的初态
    for i in range(n):
        # no dependence with others
        if data[i]['premise'] == None:
            initState[i] = 2
    print("initial state:", initState)

    # =============================================================
    # caculate correlation matrix
    matrix = getCorrelation(data, n)

    # =============================================================
    # begin with initial state & BFS
    # prepared for BFS
    id = 0
    st = St_node(0, initState, matrix)
    queue = []
    # ch list便于生成边
    ch = {2:'B', 3:'S', 4:'E', 5:'V'}
    # transfer是和前端对接的状态机
    # GNodeList是和game tree对接的状态机
    transfer = []
    GNodeList = []
    queue.append(st)

    # =============================================================
    # BFS算法
    while len(queue):
        st = queue.pop(0)
        state = st.S.copy()
        matrix = np.copy(st.m)
        print("=======================================================")
        print("current state:")
        print(state)
        # =============================================================
        # update matrix - if commitment finished(3,4,5), change value to -1
        # check whether state is a final state
        done = 0
        for i in range(n):
            if state[i] >= 3:
                matrix[i, :] = -1
                done+=1
                # update correlation matrix(column ith)
            for t in range(n):
                if matrix[t][i] == state[i]:
                    matrix[t][i] = 0
        # 所有的承诺的状态均变为终态
        if done == n:
            print("##################################################")
            print("final state:")
            print(state)
            print("##################################################")
            continue
        # =============================================================
        # get uncorrelated terms
        # maybe bug
        uclist = getUncorrelated(state, matrix)
        print("Uncorrelated list:")
        print(uclist)
        if len(uclist)==0:
            print("[getUncorrelated] Uncorrelated list return nil.")
            continue
            
        # =============================================================
        for i in range(len(uclist)):
            id = id + 1
            newState = st.S.copy()
            newMatrix = np.copy(matrix)
            action = "" 
            
            index = uclist[i][0]
            change = uclist[i][1]
            newState[index] = change

            # 向前走一步，提前更新1=>2的状态变化
            for k in range(n):
                for t in range(n):
                    if newMatrix[t][k] == newState[k]:
                        newMatrix[t][k] = 0
            sums = np.sum(newMatrix, axis=1) # Sum by line
            print("mysums")
            print(sums)
            for t in range(n):
                if sums[t] == 0 and newState[t] == 1:
                    newState[t] = 2

            # 生成状态机的边
            action = action+ch[change]+str(index)
            newSt = St_node(id, newState, newMatrix)
            queue.append(newSt)
            tran = Transfer(state, action, newState)
            transfer.append(tran)
            # 产生GNode树节点
            GNodeList,curgnode = findGNode(GNodeList,state)
            GNodeList,nextgnode = findGNode(GNodeList,newState)
            curgnode.add(nextgnode)
            nextgnode.actperson.append(data[index]['person'][0])
            nextgnode.edge.append(ch[change])

    #GNodeList的第0位就是DFA的根节点
    GNodeList[0].actperson=['']
    GNodeList[0].edge=['']
    return (initState, transfer, GNodeList[0])

# 在lists找到和data相同的node，如果没有就生成新的node并加入到lists
def findGNode(lists, data):
    data = data.astype(int)
    tmp = data.tolist()
    for i in range(len(lists)):
        if operator.eq(tmp,lists[i].data[0])==True:
            return (lists,lists[i])
    node = Gnode()
    node.data=[data.tolist()]
    node.actperson = []
    node.visited =[]
    node.edge = []
    lists.append(node)
    return (lists,node)

def judge(reality, ideal):
    if ideal == 0:
        return True
    if reality == ideal:
        return True
    elif reality == 1:
        return True
    elif reality == 2 and (ideal == 3 or ideal == 4 or ideal == 5):
        return True
    return False

# middleware
# combination
# ith - No.i commitment
# tth - No.i commitment's No.t change
def combination(res, ith, tmplist, lists, index):
    if ith == len(lists) and len(tmplist):
        res.append(tmplist)
        return res

    for t in range(len(lists[ith])):
        tmp = tmplist.copy()
        
        tmp.append([index[ith], lists[ith][t]])
        res = combination(res, ith+1, tmp, lists, index)
    return res

# get uncorrelated terms
# question: how to judge uncorrelated terms
# example: term1 * term2 = 0 & term1 * term3 = 0 & term2 * term3 != 0
# way1: caculate dot product, if equel 0 => uncorrelate
# return all changes
def getUncorrelated(state, matrix):
    # the possible change for each commitment
    # uncorrelated terms(satisfied m[i,:]==0)
    m = np.copy(matrix)
    change = []
    n = len(state)
    for i in range(n):
        tmp = []
        if state[i] == 1 :
            #tmp.append(4)
            # judge the commitment whether change to 2
            flag = 1
            for t in range(n):
                if judge(state[t], m[i][t]) == False:
                    flag = 0
                print("[judge] ",state[t], m[i][t],judge(state[t], m[i][t]) )
            sums = np.sum(m[i], axis=0)
            if flag == 1 and sums == 0:
                tmp.append(2)
            if flag == 0:
                tmp.append(4)
        elif state[i] == 2:
            tmp.append(3)
            tmp.append(5)
        change.append(tmp)

    zeroslist = []
    for i in range(n):
        for t in range(n):
            if i!=t and judge(state[t], m[i][t]) == False:
                m[i][t] = 0

    sums = np.sum(m, axis=1) # Sum by line
    print("matrix:")
    print(m)
    print("Sum by line:")
    print(sums)
    # 如果sum[i]==0，表示这个承诺可以发生变化了，就将他加入zerolists
    for i in range(len(sums)):
        if sums[i] == 0:
            zeroslist.append(i)

    res = []
    # zerolists中每一个承诺的变化展开
    for i in range(len(zeroslist)):
        for t in range(len(change[zeroslist[i]])):
            tmp = []
            tmp.append(zeroslist[i])
            tmp.append(change[zeroslist[i]][t])
            res.append(tmp)

    return res

# get all term's correlation coefficent matrix
# more info on the document
def getCorrelation(terms, n):
    print("caculate correlation coefficent...")

    # n x n matrix
    m = np.zeros((n,n), dtype=int)

    for i in range(n):
        print("caculate Term ",i)
        print("content:")
        print(terms[i]['premise'])
        # m[i][i] = 1
        if terms[i]['premise'] == None:
            continue
        premise = terms[i]['premise']
        
        # need test
        # test1 - only find words like 'Term '
        # test2 - recognition: Sat Vio Exp Bas Act
        for t in range(len(premise)):
            # no dependence
            if premise[t].find('Term') != 0:
                continue
            tmp = premise[t].split(" ")
            index = int(tmp[0][4:]) - 1
            print("index ", index)
            
            if tmp[1] == 'Sat':
                m[i][index] = 3
            elif tmp[1] == 'Exp':
                m[i][index] = 4
            elif tmp[1] == 'Vio':
                m[i][index] = 5
        print("Term ",i , " end...\n")
    return m

def json2python(JsonData):
    print ("before decoding:")
    print (JsonData)
    data = json.loads(JsonData)

    print ("after decoding:")
    print (data)
    return data

def save_transfer(initState, transfers,contract_id):
    transfer_file = {'InitStatus':str(initState.astype(int).tolist()), "FsmArray":[]}
    
    for i in range(0, len(transfers)):
        current_status = str(transfers[i].current.astype(int).tolist())
        new_status = str(transfers[i].newS.astype(int).tolist())
        action = str(transfers[i].action)
        t = {'CurrentStatus': str(current_status), 'Action': action, 'NewStatus': str(new_status)}
        #print(transfers)
        transfer_file['FsmArray'].append(t)
    
    with open('./fsm/'+contract_id, 'w') as fs:
        fs.write(json.dumps(transfer_file, indent=2))

def create_fsm(contract, contract_id):
    print(contract)
    data = str(contract[0])
    initState, transfer, DFA = generate(data)
    save_transfer(initState, transfer, contract_id)  

if __name__ == '__main__':
    data = input("jsonData")
    initState, transfer, DFA= generate(data)
    save_transfer(initState, transfer,"tmp")  
    #painting2(DFA)