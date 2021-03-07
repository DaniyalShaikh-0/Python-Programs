from collections import  Counter
lol = ['avs','ass','srgw','wewq','sdew','sdew']
c =Counter(j for i in lol for j in i)
print(c)