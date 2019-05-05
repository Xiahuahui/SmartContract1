import copy
import itertools
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
def Payoff(gametree,celues,player):  # 用图的广度优先搜索建立博弈树建立对应的相关收益矩阵
    NASH = []                 #构造纳什均衡路径的列表
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
    O = O - 1
    if O == 3:
        Row = [0] * 3          #用来显示收益矩阵的坐标
        Row[0] = Tnode['row%s' % 1]
        Row[1] = Tnode['row%s' % 2]
        Row[2] = Tnode['row%s' % 3]
        wight = [3, Tnode['P%s' % 1], Tnode['P%s' % 2], Tnode['P%s' % 3]] #显示的收益矩阵的行列数字以及纳什均衡的坐标
        juzhen = [0] * Tnode['P%s' % 1]
        for a in range(Tnode['P%s' % 1]):
            juzhen[a] = [0] * Tnode['P%s' % 2]
        for a in range(Tnode['P%s' % 1]):
            for b in range(Tnode['P%s' % 2]):
                juzhen[a][b] = [0] * Tnode['P%s' % 3]
        for a in range(Tnode['P%s' % 1]):
            for b in range(Tnode['P%s' % 2]):
                for c in range(Tnode['P%s' % 3]):
                    juzhen[a][b][c] = [0, 0, 0, 1]
        for a in range(Tnode['P%s' % 1]):
            for b in range(Tnode['P%s' % 2]):
                for c in range(Tnode['P%s' % 3]):
                    juzhen[a][b][c][0] = (Tnode['Row%s' % 1][a] + Tnode['Row%s' % 2][b]) + (Tnode['Row%s' % 3][c])
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
                    if t1 == max(Max):
                        juzhen[a][b][c][3] = juzhen[a][b][c][3] * 1
                    else:
                        juzhen[a][b][c][3] = juzhen[a][b][c][3] * 0
                    Mbx = []
                    t2 = juzhen[a][b][c][2][1]
                    for b1 in range(Tnode['P%s' % 2]):
                        Mbx.append(juzhen[a][b1][c][2][1])
                    if t2 == max(Mbx):
                        juzhen[a][b][c][3] = juzhen[a][b][c][3] * 1
                    else:
                        juzhen[a][b][c][3] = juzhen[a][b][c][3] * 0
                    Mcx = []
                    t3 = juzhen[a][b][c][2][2]
                    for c1 in range(Tnode['P%s' % 3]):
                        Mcx.append(juzhen[a][b][c1][2][2])
                    if t3 == max(Mcx):
                        juzhen[a][b][c][3] = juzhen[a][b][c][3] * 1
                    else:
                        juzhen[a][b][c][3] = juzhen[a][b][c][3] * 0
        for a in range(Tnode['P%s' % 1]):
            for b in range(Tnode['P%s' % 2]):
                for c in range(Tnode['P%s' % 3]):
                    if juzhen[a][b][c][3] == 1:
                        wight.append([a, b, c])               # 记下纳什均衡的角标
                        NASH.append([juzhen[a][b][c][1], juzhen[a][b][c][2]])   #将纳什均衡路径加入到均衡队列
        payoff = [0] * Tnode['P%s' % 1]
        for a in range(Tnode['P%s' % 1]):
            payoff[a] = [0] * Tnode['P%s' % 2]
        for a in range(Tnode['P%s' % 1]):
            for b in range(Tnode['P%s' % 2]):
                payoff[a][b] = [0] * Tnode['P%s' % 3]
        for a in range(Tnode['P%s' % 1]):
            for b in range(Tnode['P%s' % 2]):
                for c in range(Tnode['P%s' % 3]):
                    payoff[a][b][c] = list(juzhen[a][b][c][2])    #重新构造收益矩阵
    if O == 2:
        Row = [0] * 2
        Row[0] = Tnode['row%s' % 1]
        Row[1] = Tnode['row%s' % 2]
        wight = [2, Tnode['P%s' % 1], Tnode['P%s' % 2]]
        juzhen = [0] * Tnode['P%s' % 1]
        for b in range(Tnode['P%s' % 1]):
            juzhen[b] = [0] * (Tnode['P%s' % 2])
        for b in range(Tnode['P%s' % 1]):
            for c in range(Tnode['P%s' % 2]):
                juzhen[b][c] = [0, 0, 0, 1]
        for b in range(Tnode['P%s' % 1]):
            for c in range(Tnode['P%s' % 2]):
                juzhen[b][c][0] = (Tnode['Row%s' % 1][b] + Tnode['Row%s' % 2][c])
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
        ttt = []
        for b in range(Tnode['P%s' % 1]):
            for c in range(Tnode['P%s' % 2]):
                if juzhen[b][c][3] == 1:
                    ttt.append([b, c])
                    NASH.append([juzhen[b][c][1], juzhen[b][c][2]])
        wight.append(len(ttt))
        wight.append(ttt)

        payoff = [0] * Tnode['P%s' % 1]
        for b in range(Tnode['P%s' % 1]):
            payoff[b] = [0] * (Tnode['P%s' % 2])
        for b in range(Tnode['P%s' % 1]):
            for c in range(Tnode['P%s' % 2]):
                payoff[b][c] = list(juzhen[b][c][2])
    if O == 1:
        Row = [0]
        Row[0] = Tnode['row%s' % 1]

        wight = [1, Tnode['P%s' % 1]]
        juzhen = [0] * Tnode['P%s' % 1]
        for i in range(Tnode['P%s' % 1]):
            juzhen[i] = [0, 0, 0, 1]
        for i in range(Tnode['P%s' % 1]):
            juzhen[i][0] = Tnode['Row%s' % 1][i]
            for CL in celues:
                cl = CL[0]
                V = 1
                for l in cl:
                    if l not in juzhen[i][0]:
                        V = 0
                        break
                if V == 1:
                    juzhen[i][1] = CL[0]
                    juzhen[i][2] = CL[1]
                    break
        for i in range(Tnode['P%s' % 1]):
            Max = []
            a = juzhen[i][2]
            for a1 in range(Tnode['P%s' % 1]):
                Max.append(juzhen[a1][2])
            if a == max(Max):
                juzhen[i][3] = juzhen[i][3] * 1
            else:
                juzhen[i][3] = juzhen[i][3] * 0

        for i in range(Tnode['P%s' % 1]):
            if juzhen[i][3] == 1:
                wight.append([i])
                NASH.append([juzhen[i][1], juzhen[i][2]])
        payoff = [0] * Tnode['P%s' % 1]
        for i in range(Tnode['P%s' % 1]):
            payoff[i] = list(juzhen[i][2])

    return (NASH, payoff, wight, Row)
if __name__ == '__main__':
    print("收益矩阵")
