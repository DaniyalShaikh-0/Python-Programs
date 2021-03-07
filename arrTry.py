def bitOr(a,b):
    x=''
    tot=0
    for i,j in zip(a,b):
        if int(i)+int(j)>=1:
            x+='1'
            tot+=1
        else:
            x+='0'

    return x,tot
ans,l=bitOr('1000101001','0011100')
print(f'{ans} and len:  {l}')
