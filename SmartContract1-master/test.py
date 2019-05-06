def dfs3(j,juzhen, counts, index,celues,P):  #构造收益矩阵   变为1
    for m in range(counts[index]):
        if index == len(counts) - 1:
            global t
            test(t, len(counts), counts, len(counts))
            for i in range(len(t)):
                Max = []
                print("喂奶",len(j[m][2]),i)
                a = j[m][2][i]
                for b1 in range(P[i]):
                    p = 'juzhen'
                    for h in range(len(t)):
                        if h == i:
                            p = p + '['+str(b1)+']'
                        else:
                            p = p + '['+str(t[h])+']'
                    Max.append(eval(p))
                if a == max(Max):
                    j[m][3] = j[m][3] * 1
                else:
                    j[m][3] = j[m][3] * 0
        else:
            c = j[m]
            dfs3(c,juzhen,counts, index + 1,celues,P)



