
    Row = [0] * len(player) # 用来显示收益矩阵的坐标
    for i in range(len(player)):
        j = i + 1
        Row[i] = Tnode['row%s' % j]
    wight = [0] * (len(player)+1)          #确定坐标
    for i in range(len(player)+1):
        if i == 0:
            wight.append(len(player))
        else:
            wight.append(Tnode['P%s' % i])

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
                    wight.append([a, b, c])  # 记下纳什均衡的角标
                    NASH.append([juzhen[a][b][c][1], juzhen[a][b][c][2]])  # 将纳什均衡路径加入到均衡队列
    payoff = [0] * Tnode['P%s' % 1]
    for a in range(Tnode['P%s' % 1]):
        payoff[a] = [0] * Tnode['P%s' % 2]
    for a in range(Tnode['P%s' % 1]):
        for b in range(Tnode['P%s' % 2]):
            payoff[a][b] = [0] * Tnode['P%s' % 3]
    for a in range(Tnode['P%s' % 1]):
        for b in range(Tnode['P%s' % 2]):
            for c in range(Tnode['P%s' % 3]):
                payoff[a][b][c] = list(juzhen[a][b][c][2])  # 重新构造收益矩阵