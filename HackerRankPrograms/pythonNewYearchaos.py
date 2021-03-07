#python hacker rank new year chaos
t = int(input())
for t_itr in range(t):
    flg=0
    n = int(input())
    q = list(map(int, input().rstrip().split()))
    #print(q2)
    i=0
    min_=0
    alt_=0
    while i<len(q):
        p1=q[i]-1-i
        if p1<=0:
            #print('neg at ',q[i]) 1 2 5 3 7 8 6 4
            min_+=p1
            j=i
            if j<len(q)-1:
                #print(q[j])
                while True:
                    if q[j]>q[j+1]:
                        min_+=-1
                    else:
                        break
                    j+=1
                    if j>=len(q)-1:
                        break
            #print('neg at ',q[i])
        elif p1>2:
            print('Too chaotic')
            flg=1
            break
            # print('positive at ',q[i])
        i+=1
    if flg==0:
        print(-min_)
#         for j in range(len(q)):
#             if q[j]!=q2[j]:
#                 t=q2[j]
#                 q2[j+1]=q2[j]
"""
t = int(input())
for t_itr in range(t):
    flg=0
    n = int(input())
    q = list(map(int, input().rstrip().split()))
    i=0
    min_=0
    alt_=0
    while i<len(q):
        p1=q[i]-1-i
        if p1<0:
            min_+=p1
        elif p1>2:
            print('Too chaotic')
            flg=1
            break
        i+=1
    if flg==0:
        print(min_*-1)
"""
