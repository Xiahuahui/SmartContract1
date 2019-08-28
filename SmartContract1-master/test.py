file = "./log.text"
for i in range(1,10):
    with open(file, 'a+') as f:
        f.write(str(i)+'\n')   #加\n换行显示