import random
outval=0
inval=0
def display(arr):
    print('\n\n-----------------Displaying------------------\n')
    for i in arr:
        print(i)
    print('\n-----------------End------------------\n\n')
def rotate_90(state,n):
    choice = choose(state,n)
    len_ = len(state)
    init= [['', '', ''],
           ['', '', ''],
           ['', '', '']]
    index=2
    for row in choice:
        for ind,val in enumerate(row):
            init[ind][index]=val
        index-=1
    #print('Before Rotating')
    #display(state)
    global outval
    global inval
    x=0
    for v in range(outval,outval+3):
        y=0
        for w in range(inval,inval+3):
            retstate[v][w]=init[x][y]
            y+=1
        x+=1
    for i in range(len_):
        for j in range(len_):
            if retstate[i][j]!='':
                continue
            retstate[i][j]=state[i][j]
    #print('After Rotating')
    # display(retstate)
    return retstate
def choose(block,n=0):
#    n = int(input("enter n :   "))
    if n==0:
        n=random.randrange(1,10,1)
    #print(n,end='  ')
    # if n==10:
    #     print('exited with val 9')
    #     exit()
    retarr = list()
    global outval
    global inval
    if n<=3:
        outval =0
        inval = n-1
    elif n<=6:
        outval =1
        inval = n-4
    else:
        outval =2
        inval = n-7
    for index,i in enumerate(block):
        if index >=outval and index < (outval+3):
            ret =list()
            for ind,val in enumerate(i):
                
                if ind >=inval and ind < (inval+3):
                    ret.append(val)
                elif ind == inval+3:
                    break
            retarr.append(ret)
        elif index == outval+3:
            break     
    return retarr
def app(l1,l2):
    l3 = [[0] * 5 for i in range(5)]
    for i,val in enumerate(l2):
        for j,v2 in enumerate(val):
            l3[i][j]=v2
    l1.append(l3)
    
def same(initial,final):
    x = len(final)
    for i in range(x):
        if initial[i] != final[i]:
            return False
    return True
if __name__=='__main__':
    initial = [
        ['Yellow','Blue','Yellow','Purple','Green'],
        ['Green','Red','Blue','Red','Blue'],
        ['Blue','Red','Green','Red','Purple'],
        ['Red','Green','Green','Blue','Yellow'],
        ['Purple','Purple','Purple','Yellow','Yellow']
        ]
    comp = [
        ['Yellow','Yellow','Yellow','Yellow','Yellow'],
        ['Red','Red','Red','Red','Red'],
        ['Green','Green','Green','Green','Purple'],
        ['Blue','Blue','Blue','Blue','Purple'],
        ['Purple','Purple','Purple','Blue','Green']
        ]
    final = [
        ['Yellow','Yellow','Yellow','Yellow','Yellow'],
        ['Red','Red','Red','Red','Red'],
        ['Green','Green','Green','Green','Green'],
        ['Blue','Blue','Blue','Blue','Blue'],
        ['Purple','Purple','Purple','Purple','Purple']
        ]
    retstate=[['', '', '','',''],
           ['', '', '','',''],
           ['', '', '','',''],
           ['', '', '','',''],
           ['', '', '','','']]
#   val=rotate_90(rotate_90(rotate_90(rotate_90(initial))))
    #print('After rotating : ')
    #initial=final
    val=final
    checker = list()
    checker.append(val)
#   if val==final:
#      print('Puzzle completed')
    pre=0
    possib=1
    rotater=1
    cval=0
    # for i in range(5):
    #     while val[i]!=final[i]:
    while  True:
        print('Possiblities : ',possib)
        if cval==len(checker):
            print('Possiblities : ',possib)
            break
            cval+=1
        if rotater==10:
            rotater=1
            print('Possiblities : ',possib)
            break
        val=rotate_90(val,rotater)
        pre+=1
        if val not in checker:
            app(checker,val[:])
            possib+=1
        if pre==4:
            pre=0
            rotater+=1
    for c in checker:
        for i in c:
            print(i)
        print('\n\n\n')

    # while val!=final:
    #     val=rotate_90(val,0)
    #     display(val)
    #     tries+=1
    #     if tries > 5:
    #         print('too many tries..')
    #         exit()
    #     if val==final:
    #         print('puzzle completed')
    #         break