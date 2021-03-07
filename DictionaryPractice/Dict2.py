import time
dict1 = dict()
for i in range(25):
    dict1[chr(65+i)]=i+1
d2 = dict1.copy()
d2.update(Z=16)
x = list(d2.values())
for item in range(len(d2),0,-1):
    print(d2.popitem(),end='  ')