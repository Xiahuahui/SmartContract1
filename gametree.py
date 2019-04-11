import copy
import itertools
import graphviz as gz
import pygraphviz as pgv
import DFA

class node:  # 定义一颗博弈树的节点
    count = 0  # 定义节点的Id

    def __init__(self, actperson, edge, data):
        node.count = node.count + 1
        self._ID = node.count
        self._actperson = actperson  # 生成该节点的动作方
        self._data = data  # 该节点的状态
        self._edge = edge  # 生成该节点的行动
        self._children = []  # 定义该节点的孩子列表

    def getID(self):
        return self._ID  # 得到该节点的动作发出者
    def getactperson(self):
        return self._actperson  # 得到该节点的动作发出者
    def getS(self):
        state = list(self._data)
        state.append(self._ID)
        return state
    def getdata(self):
        return self._data  # 得到该节点的动作发出者

    def getchildren(self):  # 得到孩子列表
        return self._children

    def getedge(self):  # 得到该节点的入边
        return self._edge

    def getedges(self):  # 得到该节点的所有出边
        Edge = []
        for child in self._children:
            edge = child.getedge()
            Edge.append(edge)
        return Edge

    def add(self, node):
        self._children.append(node)  # 向树中加入节点
def transfer1(S0):
    Tnode = locals()
    Action = []  # 定义了博弈树每层取的动作
    I = 0  # 用于动态生成节点的变量名
    J = -1  # 用于记录出队的节点数  (即父亲节点的编号)
    M = 0  # 用于记录所添加空字符串的个数
    Queue = []  # 存储遍历点状态机节点   用于广度优先遍历
    Queue.append(S0)  # 是初始节点进队
    Tnode['Tnode%s' % I] = node(S0.actperson[0], S0.edge[0], S0.data[0])  # 初始化博弈树的节点
    Tnode['Tnode%s' % I].player = ''
    Tnode['Tnode%s' % I].depth = 0  # 初始化根节点的深度
    I = I + 1
    while len(Queue) > 0:  # 用广度遍历算法的思想遍历DFA                          
        S = Queue[0]
        Queue.pop(0)
        J = J + 1
        Children = S.getchildren()
        for child in Children:
            Queue.append(child)
            xuhao = S.getId()
            print(xuhao,S.data,child.getId(),child.data)
            nn = 0
            for nnn in range(len(child.edge)):
                if xuhao == child .edge[nnn][0]:
                    break
                nn = nn+1
            Tnode['Tnode%s' % I] = node(child.actperson[nn], child.edge[nn][1], child.data[0])
            Tnode['Tnode%s' % I].player = ''
            Tnode['Tnode%s' % I].depth = Tnode['Tnode%s' % J].depth + 1
            nodeadd(Tnode['Tnode%s' % J], Tnode['Tnode%s' % I], M, Tnode, Action)
            I = I + 1
    return ( Tnode['Tnode%s' % 0], Action)
def nodeadd(S, child, M, Tnode, Action):
    depth0 = S.depth  # 获得父亲节点的层数
    depth = child.depth  # 获得本节点的所在层数
    Tnode = locals()
    ActPerson = child.getactperson()
    if depth > len(Action):  # 是这一层的第一个做动作的人
        Action.append(ActPerson)
        S.add(child)
        S.player = Action[S.depth]
    else:  # 该层已经做完动作

        if Action[depth - 1] == ActPerson:  # 与这一层的动作相同  则可以直接添加到父亲节点
            S.add(child)
            S.player = Action[S.depth]
        elif Action[depth - 1] != ActPerson:  # 如果动作不同   则需要加空字符串
            depth1 = depth
            if depth1 == len(Action):  # 如果这是最大层则加一个空字符串
                depth1 = depth1 + 1
                Action.append(ActPerson)
            else:
                while depth1 < len(Action):  # 如果不是则遍历
                    depth1 = depth1 + 1
                    if Action[depth1 - 1] == ActPerson:
                        break
                if (depth1 == len(Action)) and (Action[depth1 - 1] != ActPerson):
                    depth1 = depth1 + 1
                    Action.append(ActPerson)

            N = depth1 - depth  # 需要假的空字符串数
            child.depth = depth1
            depth0 = depth0 + 1
            Tnode['n%s' % M] = node(Action[depth0 - 1], '', S.getdata())
            Tnode['n%s' % M].player = ''
            Tnode['n%s' % M].depth = depth0
            S.add(Tnode['n%s' % M])
            S.player = Action[S.depth]
            T = M + N - 1
            for i in range(N - 1):
                depth0 = depth0 + 1
                O = M + i
                K = M + i + 1
                Tnode['n%s' % K] = node(Action[depth0 - 1], '', S.getdata())
                Tnode['n%s' % K].player = ''
                Tnode['n%s' % K].depth = depth0
                Tnode['n%s' % O].add(Tnode['n%s' % K])
                Tnode['n%s' % O].player = Action[Tnode['n%s' % O].depth]

            Tnode['n%s' % T].add(child)
            Tnode['n%s' % T].player = Action[Tnode['n%s' % T].depth]
            M = M + N
    return M
def DFS1(gametree, Id, celue, celues):  # 用图的深度搜素遍历查找博弈树所有的策略以及这些策略的收益

    children = gametree.getchildren()
    if children == []:  # 如果是叶子节点   则为收益

        player = gametree.player
        sore = player
        c = list(celue)
        celues.append([c, sore])

    else:
        for child in children:  # 如果不是叶子节点   则在原来的策略上加上一条边
            celue1 = copy.deepcopy(celue)
            E = child.getedge()
            celue1.append([Id,gametree.getdata(), E, child.getID(),child.getdata()])
            DFS1(child, child.getID(), celue1, celues)

    return (celues)


def BFS1(gametree, Action, celues):  # 用图的广度优先搜索建立博弈树对应的相关收益矩阵
    Tnode = locals()
    NASH = []
    print(Action)
    Tnode = locals()
    Player = set(Action)
    print(Player)
    print(len(celues))
    for s in range(len(celues)):
        shouyi = input("策略对应收益:")
        celues[s][1] = shouyi.split(" ")
  
   
   

    NASH = [] 
    payoff=[]
    wight= []
    Row = [] 
    return (NASH,payoff,wight,Row)
def BFS(gametree): 
    I = 0
    O = 0
    transfers = []
    datalist = []
    Queue = []
    Queue.append(gametree)
    I = I + 1
    while len(Queue) > 0:
        Tree = Queue[0]
        Odata = list(Tree.getdata())
        O = O + 1
        Odata.append([O])
        datalist.append(Odata)
        Queue.pop(0)
        children = Tree.getchildren()
        for child in children:
            Idata = list(child.getdata())
            I = I + 1
            Idata.append([I])
            transfers.append([Odata, Idata])
            Queue.append(child)
    return (datalist, transfers)


def painting(Tnode0):
    G = pgv.AGraph(directed=True, strict=True, encoding='UTF-8')
    G.graph_attr['epsilon'] = '0.001'
    (s, transfers) = BFS(Tnode0)
    for node in list(s):
        G.add_node(str(node))
    for transfer in transfers:
        G.add_edge(str(transfer[0]), str(transfer[1]))
    G.layout('dot')
    G.draw('game-tree3.png')


def DBFS(gametree):
    transfers = []
    datalist = []
    Queue = []
    Queue.append(gametree)
    while len(Queue) > 0:
        Tree = Queue[0]
        Odata = list(Tree.data[0])
        datalist.append(Odata)
        Queue.pop(0)
        children = Tree.getchildren()
        for child in children:
            Idata = list(child.data[0])
            transfers.append([Odata, Idata])
            Queue.append(child)
    return (datalist, transfers)
def BFS2(gametree): 
    I = 0
    O = 0
    transfers = []
    datalist = []
    Queue = []
    Queue.append(gametree)
    I = I + 1
    while len(Queue) > 0:
        Tree = Queue[0]
        Odata = list(Tree.data)
        O = O + 1
        Odata.append([O])
        datalist.append(Odata)
        Queue.pop(0)
        children = Tree.getchildren()
        for child in children:
            Idata = list(child.data)
            I = I + 1
            Idata.append([I])
            transfers.append([Odata, Idata])
            Queue.append(child)
    return (datalist, transfers)

def painting2(DFA):
    G = pgv.AGraph(directed=True, strict=True, encoding='UTF-8')
    G.graph_attr['epsilon'] = '0.001'
    (s, transfers) = BFS2(DFA)
    for node in list(s):
        G.add_node(str(node))
    for transfer in transfers:
        G.add_edge(str(transfer[0]), str(transfer[1]))
    G.layout('dot')
    G.draw('DFA3.png')
def GT (gametree,NASH):

    transfer2 = []
    q = [ ]
    q.append(gametree)
    while len(q):
        Tree = q[0]
        q.pop(0)
        children = Tree.getchildren()
        for child in children:
            trans =[]
            tree = list(Tree.getS())
            chid = list(child.getS())
            trans.append(tree)
            trans.append(chid)
            lables = Tree.player+child.getedge()
            trans.append(lables)
            transfer2.append(trans)
        q.extend(children)

    return transfer2
def FSM (DFA):
    q = []
    q.append(DFA)
    while len(q):
        Tree = q[0]
        q.pop(0)
        children = Tree.getchildren()
        for child in children:
            if Tree.getId() == 23:
                print(Tree.getId(),Tree.data,child.getId(),child.data)
        print("xiahuahui")
        q.extend(children)
def FSM2 (DFA):
    q = []
    q.append(DFA)
    while len(q):
        Tree = q[0]
        q.pop(0)
        children = Tree.getchildren()
        for child in children:
            print(Tree.getID(),Tree.getdata(),child.getID(),child.getdata())
        q.extend(children)
def check (DFA):
    FSM(DFA)
    NASH = []
    S0 = DFA
    painting2(DFA)
    (Tree, Action) = transfer1(S0)
    painting(Tree)
    (celues) = DFS1(Tree,Tree.getID(),[],[])
    (NASH, payoff, wight,Row) = BFS1(Tree, Action, celues)

    nash = []
    for i in range(len(NASH)):
        for j in range(len(NASH[i][0])):
            nash.append(NASH[i][0][j][0])
            nash.append(NASH[i][0][j][3])
    goodID = set(nash)
    nash = list(goodID)
    print(NASH)
    print(nash)
    gt = GT(Tree,NASH)

    return (nash,payoff,wight,Row,gt)



  
if __name__ == '__main__':
    print()
