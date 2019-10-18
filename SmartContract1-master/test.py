idList = [1,2,3]
print("idList: ",idList)
idListTmp = [str(id) for id in idList]
print("idListTmp:", idListTmp)
idListstr = "(" + ",".join(idListTmp) + ")"
print("idListstr:", idListstr)