import copy
import itertools
import graphviz as gz
import pygraphviz as pgv


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


class Gnode:  # 定义一个FSM节点的结构
    def __init__(self):
        self._children = []  # 定义该节点的孩子列表

    def getchildren(self):  # 得到孩子列表
        return self._children

    def add(self, node):
        self._children.append(node)  # 向树中加入节点


def transfer(S0, Tonde):
    Action = []  # 定义了博弈树每层取的动作
    I = 0  # 用于动态生成节点的变量名
    J = -1  # 用于记录出队的节点数  (即父亲节点的编号)
    M = 0  # 用于记录所添加空字符串的个数
    Queue = []  # 存储遍历点状态机节点   用于广度优先遍历
    Queue.append(S0)  # 是初始节点进队

    Tnode['Tnode%s' % I] = node(S0.actperson[0], S0.edge[0], S0.data[0])  # 初始化博弈树的节点
    Tnode['Tnode%s' % I].player = ''
    I = I + 1
    Tnode0.depth = 0  # 初始化根节点的深度
    while len(Queue) > 0:  # 用广度遍历算法的思想遍历DFA
        S = Queue[0]
        Queue.pop(0)
        J = J + 1
        Children = S.getchildren()
        for child in Children:
            Queue.append(child)
            V = len(child.visited)
            Tnode['Tnode%s' % I] = node(child.actperson[V], child.edge[V], child.data[0])
            Tnode['Tnode%s' % I].player = ''
            child.visited.append('1')
            Tnode['Tnode%s' % I].depth = Tnode['Tnode%s' % J].depth + 1
            nodeadd(Tnode['Tnode%s' % J], Tnode['Tnode%s' % I], M, Tnode, Action)
            I = I + 1
    return (Tnode0, Action)


def nodeadd(S, child, M, Tnode, Action):
    depth0 = S.depth  # 获得父亲节点的层数
    depth = child.depth  # 获得本节点的所在层数

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


def BFS(gametree):  # 用图的广度优先搜索建立博弈树对应的相关收益矩阵
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


def painting2(DFA):
    G = pgv.AGraph(directed=True, strict=True, encoding='UTF-8')
    G.graph_attr['epsilon'] = '0.001'
    (s, transfers) = DBFS(DFA)
    for node in list(s):
        G.add_node(str(node))
    for transfer in transfers:
        G.add_edge(str(transfer[0]), str(transfer[1]))
    G.layout('dot')
    G.draw('DFA3.png')


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
            celue1.append([Id, E, child.getID()])
            DFS1(child, child.getID(), celue1, celues)

    return (celues)


def BFS1(gametree, Action, celues):  # 用图的广度优先搜索建立博弈树对应的相关收益矩阵
    NASH = []
    print(Action)
    Tnode = locals()
    Player = set(Action)
    print(Player)
    print(celues)
    for s in range(len(celues)):
        shouyi = input("策略对应收益:")
        celues[s][1] = eval(shouyi)
    print(celues)
    for i in Player:
        T = i
        Tnode['A%s' % i] = []
    Queue = []
    Queue.append(gametree)
    while len(Queue) > 0:
        Tree = Queue[0]
        player = Tree.player
        for i in Player:
            if player == i:
                T = i
                edges = Tree.getedges()
                child = Tree.getchildren()
                Act = []
                for j in range(len(edges)):
                    Act.append([Tree.getID(), edges[j], child[j].getID()])
                Tnode['A%s' % i].append(Act)
        Queue.pop(0)
        child = Tree.getchildren()
        Queue.extend(child)
    O = 1
    for i in Player:
        Tnode['P%s' % O] = 1
        Tnode['Row%s' % O] = []
        for j in range(len(Tnode['A%s' % i])):
            Tnode['P%s' % O] = (Tnode['P%s' % O]) * (len(Tnode['A%s' % i][j]))
        for l in itertools.product(*(Tnode['A%s' % i])):
            Tnode['Row%s' % O].append(l)
        O = O + 1
    O = O - 1
    if O == 3:
        juzhen =[0]*Tnode['P%s' % 1]
        for a in range(Tnode['P%s' % 1]):
            juzhen[a] = [0]*Tnode['P%s' % 2]
        for a in range(Tnode['P%s' % 1]):
            for b in range(Tnode['P%s' % 2]):
                juzhen[a][b] = [0]*Tnode['P%s' % 3]
        for a in range(Tnode['P%s' % 1]):
            for b in range(Tnode['P%s' % 2]):
                for c in range(Tnode['P%s' % 3]):
                    juzhen[a][b][c]=[0,0,0,1]
        for a in range(Tnode['P%s' % 1]):
            for b in range(Tnode['P%s' % 2]):
                for c in range(Tnode['P%s' % 3]):
                    juzhen[a][b][c][0] = (Tnode['Row%s' % 1][a]+Tnode['Row%s' % 2][b])+(Tnode['Row%s' % 3][c])
                    for CL in celues:
                        cl = CL[0]
                        V = 1
                        for l in cl:
                            if l not in juzhen[a][b][c][0]:
                                V = 0
                                break
                        if V == 1:
                            juzhen[a][b][c][1] = CL[0]
                            juzhen[a][b][c][2] = CL[1]
                            break
        for a in range(Tnode['P%s' % 1]):
            for b in range(Tnode['P%s' % 2]):
                for c in range(Tnode['P%s' % 3]):
                    Max = []
                    t1 = juzhen[a][b][c][2][0]
                    for a1 in range(Tnode['P%s' % 1]):
                        Max.append(juzhen[a1][b][c][2][0])
                    if t1 == max(Max) :
                        juzhen[a][b][c][3]*1
                    else:
                        juzhen[a][b][c][3]* 0
                    Mbx = []
                    t2 = juzhen[a][b][c][2][1]
                    for b1 in range(Tnode['P%s' % 2]):
                        Mbx.append(juzhen[a][b1][c][2][1])
                    if t2 == max(Mbx) :
                        juzhen[a][b][c][3]*1
                    else:
                        juzhen[a][b][c][3]*0
                    Mcx = []
                    t3 = juzhen[a][b][c][2][2]
                    for c1 in range(Tnode['P%s' % 3]):
                        Mcx.append(juzhen[a][b][c1][2][2])
                    if t3 == max(Mcx) :
                        juzhen[a][b][c][3]*1
                    else:
                        juzhen[a][b][c][3]* 0
        for a in range(Tnode['P%s' % 1]):
            for b in range(Tnode['P%s' % 2]):
                for c in range(Tnode['P%s' % 3]):
                    if juzhen[a][b][c][3] == 1:
                        NASH.append([juzhen[a][b][c][1], juzhen[a][b][c][2]])
    if O == 2:
        juzhen = [0] * Tnode['P%s' % 1]
        for b in range(Tnode['P%s' % 1]):
            juzhen[b] = [0] * (Tnode['P%s' % 2])
        for b in range(Tnode['P%s' % 1]):
            for c in range(Tnode['P%s' % 2]):
                juzhen[b][c] = [0, 0, 0, 1]
        for b in range(Tnode['P%s' % 1]):
            for c in range(Tnode['P%s' % 2]):
                juzhen[b][c][0] = (Tnode['Row%s' % 1][b] + Tnode['Row%s' % 2][c])
                print(juzhen[b][c][0])
                for CL in celues:
                    cl = CL[0]
                    V = 1
                    for l in cl:
                        if l not in juzhen[b][c][0]:
                            V = 0
                            break
                    if V == 1:
                        juzhen[b][c][1] = CL[0]
                        juzhen[b][c][2] = CL[1]
                        break
        print(juzhen)
        for b in range(Tnode['P%s' % 1]):
            for c in range(Tnode['P%s' % 2]):

                Max = []
                a = juzhen[b][c][2][0]

                for b1 in range(Tnode['P%s' % 1]):
                    Max.append(juzhen[b1][c][2][0])
                if a == max(Max):
                    juzhen[b][c][3] = juzhen[b][c][3] * 1
                else:
                    juzhen[b][c][3] = juzhen[b][c][3] * 0
                Mbx = []
                a1 = juzhen[b][c][2][1]
                for b1 in range(Tnode['P%s' % 2]):
                    Mbx.append(juzhen[b][b1][2][1])
                if a1 == max(Mbx):
                    juzhen[b][c][3] = juzhen[b][c][3] * 1
                else:
                    juzhen[b][c][3] = juzhen[b][c][3] * 0
        for b in range(Tnode['P%s' % 2]):
            for c in range(Tnode['P%s' % 1]):

                if juzhen[b][c][3] == 1:
                    NASH.append([juzhen[b][c][1], juzhen[b][c][2]])

    return NASH


if __name__ == '__main__':
    Tnode = locals()
    S0 = Gnode()
    S0.actperson = ['']
    S0.data = [[1, 1, 1]]
    S0.visited = []
    S0.edge = ['']
    S1 = Gnode()
    S1.actperson = ['A']
    S1.data = [[4, 1, 1]]
    S1.visited = []
    S1.edge = ['A']
    S2 = Gnode()
    S2.actperson = ['A']
    S2.data = [[1, 4, 1]]
    S2.visited = []
    S2.edge = ['B']
    S3 = Gnode()
    S3.actperson = ['B']
    S3.data = [[1, 1, 4]]
    S3.visited = []
    S3.edge = ['C']
    S4 = Gnode()
    S4.actperson = ['C']
    S4.data = [[4, 1, 4]]
    S4.visited = []
    S4.edge = ['D']
    S0.add(S1)
    S0.add(S2)
    S2.add(S4)
    S1.add(S3)

    (Tree, Action) = transfer(S0, Tnode)
    painting(Tree)
    painting2(S0)
   
    (celues) = DFS1(Tree, Tree.getID(), [], [])
    print(BFS1(Tree, Action, celues))



