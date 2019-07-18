#通过博弈树的收益矩阵,并根据收益矩阵求解NASH均衡
import numpy as np
import copy
import itertools
import DFA
import json
import pickle as pickle
def Strategies(gametree, celue, celues):  # 用图的深度搜素遍历查找博弈树所有的策略以及这些策略的收益
    children = gametree.getchildren()       #直接取得是策略
    if children == []:  # 如果是叶子节点   则为收益
        data = gametree.id
        sore = data
        c = list(celue)
        celues.append([c, sore])
    else:
        for child in children:  # 如果不是叶子节点   则在原来的策略上加上一条边
            E = child.getedge()
            for e in E:
                celue1 = copy.deepcopy(celue)
                length = len(e)
                for i in range(length):
                    if e[i][0] == 'C':
                        continue
                    celue1.append(e[i])
                Strategies(child, celue1, celues)
    return (celues)
def NASHsecond (payoff):    #输入收益矩阵     输出纳什均衡点
    xlable = [0]*len(payoff)        #存储每个节点x的lable ,收益矩阵的行数,即第一个人的纯策略
    A = [0] * len(payoff)           #构造A矩阵
    ylable = [0]*len(payoff[0])         #存储每个节点y的lable ,收益矩阵的列数,即第二个人的纯策略
    B = [0] * len(payoff[0])           #构造矩阵B
    Tnode = locals()  # 用于动态生成不同名称的变量
    for i in range(len(payoff)): #取A矩阵的每行
        a = []                  #记录收益矩阵中每行A的收益
        for j in range(len(payoff[i])):
            a.append(payoff[i][j][0])
            A[i] = list(a)
    for j in range(len(payoff[0])): #取收益矩阵的每列
        b = []                  #记录收益矩阵中每列B的收益
        for i in range(len(payoff)):
            b.append(payoff[i][j][1])
            B[j] = list(b)
    for i in range(len(payoff)):
        k = i+1              #使得x的下角标从1开始
        Tnode['x%s' % k] = [0]*(len(payoff))
        Tnode['x%s' % k][i] = 1
        xlable[i]=[]        #初始化x的lable即x分量为0的下标加1
        for m in range(len(payoff)):
            if m == i:
                continue
            else:
                xlable[i].append(m+1)
        Max = []
        for n in range(len(B)):             #寻找策略x的最佳对应策略
            sum = 0
            for p in range(len(payoff)):
                sum = sum + (Tnode['x%s' % k][p]*B[n][p])
            Max.append(sum)
        M = max(Max)
        for q in range(len(Max)):                  #找到最佳即为lable
            if Max[q] == M:
                xlable[i].append(len(payoff)+1+q)
    for j in range(len(payoff[0])):
        k = j+1              #使得y的下角标从1开始
        Tnode['y%s' % k] = [0]*(len(payoff[0]))
        Tnode['y%s' % k][j] = 1
        ylable[j]=[]        #初始化y的lable即x分量为0的下标加1
        for m in range(len(payoff[0])):
            if m == j:
                continue
            else:
                ylable[j].append(len(payoff)+m+1)
        Max = []
        for n in range(len(A)):        #寻找策略y的最佳对应策略
            sum = 0
            for p in range(len(payoff[0])):
                sum = sum + (Tnode['y%s' % k][p]*A[n][p])
            Max.append(sum)
        M = max(Max)                  #找到最佳即为lable
        for q in range(len(Max)):
            if Max[q] == M:
                ylable[j].append(1+q)
    for i in range (len(payoff)):
        print("x"+str(1+i),xlable[i])
    for j in range(len(payoff[0])):
        print("y"+str(1+j),ylable[j])
    Nash = []                   #寻找纳什均衡点 即lable中包含(1到m +n中的所有数值即为纳什均衡点)
    for i in range (len(payoff)):
        for j in range(len(payoff[0])):
            lable = []
            lable.extend(xlable[i])
            lable.extend(ylable[j])
            flage = 1
            for k in range(len(payoff)+len(payoff[0])):
                l = k + 1
                if l not in lable:
                    flage = 0
            if flage == 1:
                nash = [i,j]
                Nash.append(nash)
    return Nash
def Payoff(DGA,celues):  # 用图的广度优先搜索建立博弈树建立对应的相关收益矩阵      #          #构造纳什均衡路径的列表
    player = ['A','B']
    Tnode = locals()
    for s in celues:
        print("策略" , s)
    for s in range(len(celues)): #根据策略赋值
        length = len(player)
        shouyi = [0] * length
        for i in range(length):
            shouyi[i] = s + 1
        celues[s][1] = list(shouyi)
    for yyy in celues:
        print("策略" , yyy)
    wholeChoice = []               #存储所有节点的策略
    wholeact = []                  #存储所有节点的动作组合用来前端显示
    for i in player:               #根据参与人构造策略矩阵
        wholeChoice.append([])
        wholeact.append([])
    Queue = []
    Queue.append(DGA)         #遍历DGA
    while len(Queue) > 0:
        dNode = Queue[0]
        actperson = dNode.getplayer()    #得到该节点的所有动作人
        Action = dNode.getaction()  #得到该节点的所有动作序列
        for i in actperson:
            Tnode['Act%s' % i] = []            #每个节点的动作人
            Tnode['Bct%s' % i] = []            #每个节点的动作人的动作
        for act in Action:
            p = act[0]+str(act[2])             #具体是哪个参与人
            Tnode['Act%s' % p].append(act)     #加入策略
            Tnode['Bct%s' % p].append(act[1])  #加入动作
        for j in actperson:
            if j[0] == 'A':
                wholeChoice[0].append(Tnode['Act%s' % j])      #构造信息集
                wholeact[0].append(Tnode['Bct%s' % j])
            if j[0] == 'B':
                wholeChoice[1].append(Tnode['Act%s' % j])      #构造信息集
                wholeact[1].append(Tnode['Bct%s' % j])
        Queue.pop(0)
        child = dNode.getchildren()
        Queue.extend(child)
    Strnum = [1,1] #存储策略数
    Str = [[],[]] #存储策略组合笛卡尔积每个参与人的策略
    Stract = [[],[]]#存储动作的笛卡尔积
    for i in range(len(player)):
        for j in range(len(wholeChoice[i])):
            Strnum[i]= Strnum[i] * len(wholeChoice[i][j])    #查看笛卡尔积最后的个数
        for l in itertools.product(*(wholeChoice[i])):              #形成笛卡尔积
            Str[i].append(l)
        for l in itertools.product(*(wholeact[i])):             #形成笛卡尔积
            Stract[i].append(l)
    row = []        #记录每个参与人策略的笛卡尔积
    P = []          #记录每个参与人的策略的笛卡尔积的个数
    for i in range(len(player)):
        row.append(Str[i])        #每个参与人的策略的笛卡尔积
        P.append(Strnum[i])       #每个参与人的策略的笛卡尔积的个数
    NASH = []
    ttt = []
    Row = [0] * len(player)  # 用来显示收益矩阵的坐标
    for i in range(len(player)):
        Row[i] = Stract[i]
    wight = []   # 确定坐标
    for i in range(len(player) + 1):
        if i == 0:
            wight.append(len(player))
        else:
            wight.append(Strnum[i-1])
    strategies = [0] * Strnum[0] #策略矩阵
    path = [0] * Strnum[0]   #路径
    payoff = [0] * Strnum[0] #收益矩阵
    flag = [0] * Strnum[0] #标志矩阵
    for a in range(Strnum[0]):
        path[a] = [0] * Strnum[1]
        payoff[a] = [0] * Strnum[1]
        strategies[a] = [0] * Strnum[1]
        flag[a] = [0] * Strnum[1]
    for a in range(Strnum[0]):
        for b in range(Strnum[1]):
            strategies[a][b] = 0
            path[a][b] = 0
            payoff[a][b] = 0
            flag[a][b] = 1
    for a in range(Strnum[0]):
        for b in range(Strnum[1]):
            strategies[a][b] = (Str[0][a] + Str[1][b])
            for CL in celues:
                cl = CL[0]
                V = 1
                for l in cl:
                    if l not in strategies[a][b]:
                        V = 0
                        break
                if V == 1:
                    path[a][b] = CL[0]
                    payoff[a][b] = CL[1]
                    break
    for a in range(Strnum[0]):
        for b in range(Strnum[1]):
            Max = []
            c1 = payoff[a][b][0]
            for a1 in range(Strnum[0]):
                Max.append(payoff[a1][b][0])
            if c1 == max(Max):
                flag[a][b] = flag[a][b] * 1
            else:
                flag[a][b] = flag[a][b] * 0
            Mbx = []
            c2 = payoff[a][b][1]
            for b1 in range(Strnum[1]):
                Mbx.append(payoff[a][b1][1])
            if c2 == max(Mbx):
                flag[a][b] = flag[a][b] * 1
            else:
                flag[a][b] = flag[a][b] * 0
    for a in range(Strnum[0]):
        for b in range(Strnum[1]):
            if flag[a][b] == 1:
                print("流畅")
                NASH.append([path[a][b],payoff[a][b]])
                ttt.append([a,b])

    wight.append(len(ttt))
    wight.append(ttt)
    print("查看是否相同")
    ttt1 = NASHsecond(payoff)
    if len(ttt) == len(ttt1):
        f = 1
        for i in range(len(ttt)):
            if ttt[i] not in ttt1:
                f = 0
        if f == 1:
            print("纳什均衡点是相同的")
    print(ttt)
    print(ttt1)
    return (NASH, payoff, wight, Row,strategies)
def save_payoff(NASH,payoff,wight,Row,contract_id):
    with open('./NASH/' + contract_id, 'w') as fs:
        fs.write(json.dumps(NASH, indent=2))
    with open('./payoff/' + contract_id, 'w') as fs:
        fs.write(json.dumps(payoff, indent=2))
    with open('./wight/' + contract_id, 'w') as fs:
        fs.write(json.dumps(wight, indent=2))
    with open('./Row/' + contract_id, 'w') as fs:
        fs.write(json.dumps(Row, indent=2))
def create_payoff(contract, contract_id):
    read_file = open('./MyWorkPlace/'+contract_id+'.pkl', 'rb+')
    NASH = []
    Tree = pickle.load(read_file)
    celues = Strategies(Tree, [], [])
    (NASH, payoff, wight, Row,strategies) = Payoff(Tree, celues)
    print("xiahuahui ")

    NE = []
    read_file.close()
    save_payoff(NE,payoff,wight,Row, contract_id)


if __name__ == '__main__':
    print("收益矩阵")