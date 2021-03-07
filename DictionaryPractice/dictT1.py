import time
dict1 = dict()
for i in range(25):
    dict1[chr(65+i)]=i+1
d2 = dict1.copy()
x = list(item[1] for item in d2.items())