# n=int(input())
# for i in range(n-1,-1,-1):
#     print(i)
t = int(input())
for t_itr in range(t):
    flg=0
    n = int(input())
    q = list(map(int, input().rstrip().split()))
    #print(q2)
    ij=0
    min_=0
    alt_=0
    while ij<len(q):
        p1=q[ij]-1-ij
        if p1>2:
            print('Too chaotic')
            flg=1
            break
        ij+=1
    if flg==0:
        #find min
        print('work')
        for i in range(n-1,-1,-1):
            print('lop work')
            k=i
            print(i)
            if min_==-1:
                break
            while q[k]!=i+1:
                k-=1
                if i-k>2:
                    min_=-1
                    break
                else:
                    while k!=i:
                        tmp=q[k]
                        q[k]=q[k+1]
                        q[k+1]=tmp
                        k+=1
                        min_+=1
            #print(q2)
        print(min_)