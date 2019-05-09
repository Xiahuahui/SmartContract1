import numpy as np
import copy
import itertools
def dfs(j, counts, index):
    for i in range(counts[index]):
        if index == len(counts) - 1:
            j[i] = [0, 0, 0, 1]
        else:
            c = j[i]
            dfs(c, counts, index + 1)
def init(j, counts, index):      #初始化矩阵
    dfs(j, counts, index)
    return j
def test(t, tlength, counts, clength):        # 查找收益矩阵下表标
    t[tlength - 1] = t[tlength - 1] + 1
    if t[tlength - 1] >= counts[clength - 1]:
        t[tlength - 1] = 0
        test(t, tlength - 1, counts, clength - 1)
def dfs2(j,t, counts, index,celues,row):  #构造收益矩阵
    for i in range(counts[index]):
        if index == len(counts) - 1:
            test(t, len(counts), counts, len(counts))
            Act = ()
            for l in range(len(counts)):
                Act = (Act+row[l][t[l]])
            j[i][0] = Act
            for CL in celues:
                cl = CL[0]
                V = 1
                for l in cl:
                    if l not in j[i][0]:
                        V = 0
                        break
                if V == 1:
                    j[i][1] = CL[0]
                    j[i][2] = CL[1]
                    break
        else:
            c = j[i]
            dfs2(c,t,counts, index + 1,celues,row)
    return t

def dfs3(j,t,juzhen, counts, index,P):  #构造收益矩阵   变为1
    for m in range(counts[index]):
        if index == len(counts) - 1:
            test(t, len(counts), counts, len(counts))
            for i in range(len(t)):
                Max = []
                a = j[m][2][i]
                for b1 in range(P[i]):
                    p = 'juzhen'
                    for h in range(len(t)):
                        if h == i:
                            p = p + '['+str(b1)+']'
                        else:
                            p = p + '['+str(t[h])+']'
                    p = p + '[2]['+str(i) +']'
                    Max.append(eval(p))
                if a == max(Max):
                    j[m][3] = j[m][3] * 1
                else:
                    j[m][3] = j[m][3] * 0
        else:
            c = j[m]
            dfs3(c,t,juzhen,counts, index + 1,P)
    return t
def dfs4(j,payoff, counts, index):      # 构造收益矩阵
    for i in range(counts[index]):
        if index == len(counts) - 1:
           payoff[i] = list(j[i][2])
        else:
            c = j[i]
            d = payoff[i]
            dfs4(c, d, counts, index+1)
def dfs5(j, t,ttt,NASH,counts, index):      # 构造收益矩阵
    for i in range(counts[index]):
        if index == len(counts) - 1:
            test(t, len(counts), counts, len(counts))
            if j[i][3] == 1:
                ttt.append(list(t))
                NASH.append(list([j[i][1], j[i][2]]))
        else:
            c = j[i]
            dfs5(c,t,ttt,NASH,counts, index + 1)
    return (t,ttt,NASH)
def Strategies(gametree, celue, celues):  # 用图的深度搜素遍历查找博弈树所有的策略以及这些策略的收益
    children = gametree.getchildren()
    if children == []:  # 如果是叶子节点   则为收益
        data = gametree.ID
        sore = data
        c = list(celue)
        celues.append([c, sore])
    else:
        for child in children:  # 如果不是叶子节点   则在原来的策略上加上一条边
            celue1 = copy.deepcopy(celue)
            E = child.getedge()
            length = len(E)
            for i in range(length):
                celue1.append(E[i])
            Strategies(child, celue1, celues)
    return (celues)
def data (gametree,celues):
    Data = [0]*len(celues)
    ID = [0] * len(celues)
    for i in range(len(celues)):
        Data[i] = []
        ID[i] = []
    for i in range(len(celues)):
        for j in celues[i][0]:
            if j[3] not in ID[i]:
                ID[i].append(j[3])
    for i in range(len(ID)):
        for j in range(len(ID[i])):
            id = ID[i][j]
            q = []
            q.append(gametree)
            while len(q):
                Tree = q[0]
                number = Tree.ID
                if id == number:
                    Data[i].append(Tree.ID)
                q.pop(0)
                children = Tree.getchildren()
                q.extend(children)
    for i in range(len(Data)):
        Data[i].append(celues[i][1])
    return Data
def Payoff(gametree,celues,player):  # 用图的广度优先搜索建立博弈树建立对应的相关收益矩阵                #构造纳什均衡路径的列表
    Tnode = locals()
    for s in range(len(celues)):
        length = len(player)
        shouyi = [0] * length
        for i in range(length):
            shouyi[i] = s + 1
        celues[s][1] = list(shouyi)
    for i in player:               #根据参与人构造策略矩阵
        Tnode['A%s' % i] = []
        Tnode['B%s' % i] = []
    Queue = []
    Queue.append(gametree)         #遍历博弈树
    while len(Queue) > 0:
        Tree = Queue[0]
        actperson = Tree.getplayer()
        Action = Tree.getaction()  #得到该节点的所有动作序列
        for i in actperson:
            Tnode['Act%s' % i] = []
            Tnode['Bct%s' % i] = []
        for act in Action:
            p = act[0]+str(act[2])
            Tnode['Act%s' % p].append(act)
            Tnode['Bct%s' % p].append(act[1])
        for i in player:
            for j in actperson:
                if len(Tnode['Act%s' % j])>= 1:     #如果该参与人在给节点没有动作
                    for k in Tnode['Act%s' % j]:
                        if k[0] == i:
                            Tnode['A%s' % i].append(Tnode['Act%s' % j])
                            Tnode['B%s' % i].append(Tnode['Bct%s' % j])
                            break
        Queue.pop(0)
        child = Tree.getchildren()
        Queue.extend(child)
    O = 1
    for i in player:
        Tnode['P%s' % O] = 1
        Tnode['Row%s' % O] = []
        Tnode['row%s' % O] = []
        for j in range(len(Tnode['A%s' % i])):
            Tnode['P%s' % O] = (Tnode['P%s' % O]) * (len(Tnode['A%s' % i][j]))    #查看笛卡尔积最后的个数
        for l in itertools.product(*(Tnode['A%s' % i])):              #形成笛卡尔积
            Tnode['Row%s' % O].append(l)
        for l in itertools.product(*(Tnode['B%s' % i])):             #形成笛卡尔积
            Tnode['row%s' % O].append(l)
        O = O + 1
    row = []
    P = []
    for i in range(len(player)):
        j =i+1
        row.append(Tnode['Row%s' % j])
        P.append(Tnode['P%s' % j])
    NASH = []
    Row = [0] * len(player)  # 用来显示收益矩阵的坐标
    for i in range(len(player)):
        j = i + 1
        Row[i] = Tnode['row%s' % j]
    wight = []   # 确定坐标
    for i in range(len(player) + 1):
        if i == 0:
            wight.append(len(player))
        else:
            wight.append(Tnode['P%s' % i])
    arraay = []
    for i in range(len(player)):
        j = i + 1
        arraay.append(Tnode['P%s' % j])
    test = np.zeros(arraay, dtype=np.int)
    payoff = np.zeros(arraay, dtype=np.int)
    payoff = list(test.tolist())
    juzhen = list(test.tolist())
    juzhen = init (juzhen,arraay,0)
    t = [0] * (len(player)-1)
    t.append(-1)
    dfs2(juzhen,t,arraay,0,celues,row)           #TODO t的初始化
    t = [0] * (len(player)-1)
    t.append(-1)
    trans = list(juzhen)
    dfs3(juzhen,t,trans, arraay, 0, P)
    t = [0] * (len(player)-1)
    t.append(-1)
    dfs4(juzhen,payoff,arraay,0)
    ttt = []
    (t,ttt,NASH)=dfs5(juzhen,t,ttt,NASH,arraay,0)
    wight.append(len(ttt))
    wight.append(ttt)
    return (NASH, payoff, wight, Row)
if __name__ == '__main__':
    print("收益矩阵")
