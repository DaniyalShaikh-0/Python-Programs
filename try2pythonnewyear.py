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
        if p1>2:
            print('Too chaotic')
            flg=1
            break
        i+=1
    if flg==0:
        #find min
        q2=list(i for i in range(1,len(q)+1))
        i=0
        c_ind=None
        #print(q2)
        while q2!=q and i<len(q)-1: 
            j=0
            p1=q[i]-1-i
            if p1!=0:
                d1=0
                for m in range(n):
                    if q2[m]==q[i]:
                        c_ind=m
                        p1=abs(d1-i)
                        break
                    d1+=1
                #good logic
                # if p1>0:
                #     min_+=p1
                for j in range(p1):
                    c_ind=c_ind-j
                    tmp=q[c_ind]
                    q[c_ind]=q[c_ind-1]
                    q[c_ind-1]=tmp
                    min_+=1
            i+=1
            #print(q2)
        print(min_)
