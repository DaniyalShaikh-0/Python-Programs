import random
outval=0
inval=0
def rotate_90(state):
    choice = choose(state)
    print('Before rotating : ')
    for i in state:
        print(i)
    init= [['', '', ''],
           ['', '', ''],
           ['', '', '']]
    index=2
    for row in choice:
        for ind,val in enumerate(row):
            init[ind][index]=val
        index-=1
    global outval
    global inval
    x=0
    for v in range(outval,outval+3):
        y=0
        for w in range(inval,inval+3):
            initial[v][w]=init[x][y]
            y+=1
        x+=1
    return initial
def choose(block):
    n = int(input("enter n :   "))
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


if __name__=='__main__':
    initial = [
        ['Yellow','Blue','Yellow','Purple','Green'],
        ['Green','Red','Blue','Red','Blue'],
        ['Blue','Red','Green','Red','Purple'],
        ['Red','Green','Green','Blue','Yellow'],
        ['Purple','Purple','Purple','Yellow','Yellow']
        ]
    final = [
        ['Yellow','Yellow','Yellow','Yellow','Yellow'],
        ['Red','Red','Red','Red','Red'],
        ['Green','Green','Green','Green','Green'],
        ['Blue','Blue','Blue','Blue','Blue'],
        ['Purple','Purple','Purple','Purple','Purple']
        ]
    val=rotate_90(rotate_90(rotate_90(rotate_90(initial))))
    print('After rotating : ')
    for i in val:
        print(i)