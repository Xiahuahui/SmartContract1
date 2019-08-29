a = {"1":[1],"2":[2]}
b = {"1":[4],"2":[5]}
for i in a.keys():
    print(a.keys())
    print(i)
    print(type(i))
a.update(b)
print(a)