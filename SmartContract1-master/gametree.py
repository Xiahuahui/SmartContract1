import pygraphviz as pgv
import itertools
import payoff1
class GTnode:  # 定义一颗博弈树的节点
    count = 0  # 定义节点的Id
    def __init__(self, edge, data):        #初始化节点
        GTnode.count = GTnode.count + 1
        self.ID = GTnode.count          #初始化节点
        self.data = data  # 该节点的状态    [1,2,3,4,5]
        self.edge = edge  # 生成该节点的行动 [[actperson,action],[actperson,action],...]
        self.children = []  # 定义该节点的孩子列表
        self.equal = []     # 记录节点加入空字符串的情况
    def getID(self):
        return self.ID  # 得到该节点的ID
    def getdata(self):
        return self.data  # 得到该节点的的状态数据
    def getchildren(self):  # 得到孩子列表
        return self.children
    def getedge(self):  # 得到该节点的入边
        return self.edge
    def getS(self):
        state = list(self.data)
        state.append(self.ID)
        return state
    def getPlayer(self):  #得到该节点入边的动作人
        edge=self.edge
        length = len(edge)
        Player = []
        for l in range(length):
            Player.append(edge[l][0]+str(edge[l][2]))
        Player = set(Player)
        Player = list(Player)
        return Player
    def getplayer(self):    #得到该节点的动作人 player
        player = []
        for child in self.children:
            edge = child.getedge()
            length = len(edge)
            Player = []
            for l in range(length):
                Player.append(edge[l][0]+str(edge[l][2]))
            player.extend(Player)
        player = set(player)
        player = list(player)
        return player
    def getplayerset(self):
        player = []
        for child in self.children:
            edge = child.getedge()
            length = len(edge)
            Player = []
            for l in range(length):
                Player.append(edge[l][0])
            player.extend(Player)
        player = set(player)
        player = list(player)
        return  player
    def getedges(self):  # 得到该节点的所有出边
        Edge = []
        for child in self.children:
            edge = child.getedge()
            Edge.append(edge)
        return Edge
    def add(self, GTnode): # 向树中加入节点
        self.children.append(GTnode)
    def getaction(self):       #得到该节点的所有动作
        action = []
        Edges = self.getedges()
        for e in Edges:
            for act in e :
                action.append(act)
        removal = []              #列表去重
        for i in action:
            if i not in removal:
                removal.append(i)
        action = list(removal)
        return action
def transfer(DFA):    #将状态机转化为博弈树  Input:状态机的根节点  Output: 博弈树的的根节点
    Gnode.count = 0
    Tnode = locals() #用于动态生成不同名称的节点
    I = 1            # 用于动态生成节点的变量名
    J = 0           # 用于记录出队的节点数  (即父亲节点的编号) 与ID相对应
    M = 0            # 用于记录所添加空字符串的个数
    Queue = []       # 存储遍历点状态机节点   用于广度优先遍历
    Queue.append(DFA)  # 是初始节点进队
    Tnode['Tnode%s' % I] = GTnode(DFA.edge, DFA.data)  # 初始化博弈树的根节点 
    I = I + 1
    while len(Queue) > 0:  # 用广度遍历算法的思想遍历DFA
        S = Queue[0]
        Queue.pop(0)
        J = J + 1          #出队节点的序号,因为game-tree中的节点都是一一对应的,其实就是将状态机一一遍历相对应
        Children = S.getchildren()
        for child in Children:            # 用于多个父状态的拆分     状态机中孩子节点的入边和父亲节点的Id一一对应的
            Queue.append(child)
            number = S.id
            nn = 0
            for n in range(len(child.edge)):# 状态机中边的结构
                if number == child .edge[n][0][0]:
                    break
                nn = nn+1
            edge = child.edge[nn][1]
            for e in edge:
                e.append(Tnode['Tnode%s' % J].ID)
            Tnode['Tnode%s' % I] = GTnode(edge, child.data)  #初始化节点I   edge 结构[[A,sat],[B,vio]]
            M = nodeadd(Tnode['Tnode%s' % J], Tnode['Tnode%s' % I], M,Tnode)    #将子节点加入到博弈树的指定地方
            I = I + 1
    return (Tnode['Tnode%s' % 1])
def nodeadd(parent, child, M ,Tnode):              #按照博弈树的规则往博弈树中加入新节点构成博弈树
    Edge = locals()                         #按照动作人(player)的不同,构造边集,将边分类
    player = parent.getplayer()             #得到父亲节点的动作人的集合(player)
    player1 = list(player)                  #保留原来父亲节点的动作人
    Player = child.getPlayer()              #得到孩子节点入边的动作人Player
    player.extend(Player)                   #得到父亲节点的所有动作人
    player = set(player)                    #去重
    Player = set(Player)                    #去重
    player = list(player)                    #去重
    Player = list(Player)
    for person in player:                   #构造每个player的边集
        Edge['Edge%s' % person]=[]
        Edges = parent.getedges()
        for edge in Edges:
            for e in edge:
                actperson = e[0]+str(e[2])
                if person == actperson:
                    Edge['Edge%s' % person].append(e)
    for person in player:                   #构造每个player的边集 将新加入的子节点的边也加入
        edge = child.getedge()
        for e in edge:
            actperson = e[0]+str(e[2])
            if person == actperson:
                Edge['Edge%s' % person].append(e)
    for person in player:           # 动作人动作去重
        removal = []              #列表去重
        for i in  Edge['Edge%s' % person]:
            if i not in removal:
                removal.append(i)
        Edge['Edge%s' % person] = list(removal)
    E = []                                  #构造每个player的边集
    for person in player:                   #构造每个player的边集的笛卡尔积
        E.append(Edge['Edge%s' % person])
    ES = []     #存放边集的笛卡尔积
    for l in itertools.product(*E):
        ES.append(l)
    Edges = parent.getedges()
    Edges.append(child.getedge())
    gables = 1                #查看加上边后的是否加入空串
    for l in ES:              #查看笛卡尔积中有几条边
        T = 0  # 判断一个节点在一次选择中是否有两条路径
        for e in Edges:
            flag = 1          #查看该边是否在笛卡尔积中
            el = len (e)      #这条边有几个动作 即边的长度
            for i in range (el):
                if e[i] not in l:
                    flag = 0
                    break 
            if flag == 1:
                T = T + 1
        if T >= 2:             #查看是否有两条以上的边
            gables = 2
            break
    if gables == 1:
        parent.add(child)
    if gables == 2:                 #当加入这个节点含有两条路径
        if len(parent.equal) == 0:    #当父亲节点还没有加入空字符串
            Tnode['n%s' % M] = GTnode('',parent.data)           #初始化等价节点x
            actperson = ''              #确定空节点的动作人
            number = 0
            edges = parent.getedges()
            for edge in edges:
                for e in edge:
                    actperson = e[0]
                    number = e[2]
                    break
                break
            addedge = [[actperson,'',number,parent.ID]]  #初始化等价节点的入边       TODO ：需要改动
            Tnode['n%s' % M].edge = addedge
            parent.equal.append(M)    # 记下等价节点的编号
            parent.add(Tnode['n%s' % M]) # 和父亲节点链接
            for e in child.edge:
                e [3] = Tnode['n%s' % M].ID
            Tnode['n%s' % M].add(child)#将孩子节点加到等价节点
            M = M + 1
        else: #当父亲节点已经加入等价节点时则在
            m = parent.equal[0]
            M = nodeadd(Tnode['n%s' % m],child,M,Tnode)
    return M
def BSFDFA(DFA):             #广度遍历状态机DFA
    I = 0
    J = 0
    transfers = []           #构造一个状态转移队列
    datalist = []            #构造一个节点队列
    Queue = []
    Queue.append(DFA)
    J = J + 1
    while len(Queue) > 0:
        Tree = Queue[0]
        I = I + 1
        Odata = list(Tree.data)
        Odata.append([I])
        datalist.append(Odata)     #重复也可以
        Queue.pop(0)
        children = Tree.getchildren()
        for child in children:
            J = J + 1
            Idata = list(child.data)
            Idata.append([J])
            transfers.append([Odata, Idata])
            Queue.append(child)
    return (datalist, transfers)
def paintDFA(DFA):       #将状态机DFA画出来
    G = pgv.AGraph(directed=True, strict=True, encoding='UTF-8')
    G.graph_attr['epsilon'] = '0.001'
    (s, transfers) = BSFDFA(DFA)
    for node in list(s):
        G.add_node(str(node))
    for transfer in transfers:
        G.add_edge(str(transfer[0]), str(transfer[1]))
    G.layout('dot')
    G.draw('DFA3.png')
def BFSTree(gametree):  # 用图的广度遍历博弈树
    A = gametree.getedges()
    I = 0
    O = 0
    player = []       #构造参与人的列表
    transfers = []    #构造转移矩阵
    datalist = []     #构造节点队列
    Queue = []
    Queue.append(gametree)
    I = I + 1
    while len(Queue) > 0:
        Tree = Queue[0]
        Odata = list(Tree.getdata())
        player.extend(Tree.getplayerset())
        O = O + 1
        Odata.append([O])   #加一个后缀用于显示
        datalist.append(Odata)
        Queue.pop(0)
        children = Tree.getchildren()
        for child in children:
            Idata = list(child.getdata())
            I = I + 1
            Idata.append([I])
            transfers.append([Odata, Idata])
            Queue.append(child)
    player = set(player)
    player = list(player)
    return (datalist, transfers,player)
def paintTree(Tree):   #将博弈树画下来
    G = pgv.AGraph(directed=True, strict=True, encoding='UTF-8')
    G.graph_attr['epsilon'] = '0.001'
    (s, transfers,p) = BFSTree(Tree)
    for node in list(s):
        G.add_node(str(node))
    for transfer in transfers:
        G.add_edge(str(transfer[0]), str(transfer[1]))
    G.layout('dot')
    G.draw('game-tree3.png')
def GT (gametree):   #用来遍历博弈树生成图片
    transfers = []
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
            edge = child.getedge()
            lables = ''
            for act in edge:
                lables = lables+(act[0]+act[1]+' ')       #显示时显示的边信息
            trans.append(lables)
            transfers.append(trans)
        q.extend(children)
    return transfers
def check (DFA):
    NASH = []
    paintDFA(DFA)
    Tree = transfer(DFA)
    paintTree(Tree)
    (datalist, transfers,player) = BFSTree(Tree)
    celues = payoff1.Strategies(Tree,[],[])
    Data = payoff1.data(Tree,celues)
    (NASH, payoff, wight,Row) = payoff1.Payoff(Tree,celues,player)
    gables = []
    nash = []
    for i in range(len(NASH)):
        for j in range(len(celues)):
            if NASH[i] == celues[j]:
                gables.append(j)
    for j in range(len(gables)):
        nash.append(Data[gables[j]])
    NE = []
    for i in range (len(nash)):
        for j in nash[i]:
            if j not in NE:
                NE.append(j)

    gt = GT(Tree)

    return (NE,payoff,wight,Row,gt)
class Gnode:
    def __init__(self):
        self.children =[]
    def add(self, Gnode): # 向树中加入节点
        self.children.append(Gnode)
    def getchildren(self):  # 得到孩子列表
        return self.children
if __name__ == '__main__':
    S0 = Gnode()
    S0.Id = 0
    S0.data =[2,1,1,1]
    S0.edge =[[[],[]]]
    S1 =Gnode()
    S1.Id = 1
    S1 .data=[3,2,2,1]
    S1.edge=[[[0],[['A','sat']]]]
    S2 = Gnode()
    S2.Id = 2
    S2.data = [2,1,1,4]
    S2.edge = [[[0],[['B','exp']]]]
    S3 = Gnode()
    S3.Id = 3
    S3.data = [3,3,3,1]
    S3.edge = [[[1],[['C','Sat'],['B','St']]],[[2],[['A','S']]]]
    S0.add(S1)
    S0.add(S2)
    S1.add(S3)
    S2.add(S3)
    check(S0)


