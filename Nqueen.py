def display(check2,total):
    if check2  not in prev_nq: 
        for i in range(N):
            prev_nq[nq_ct][i]=check2[i]
        print("\nSolution ",total,' : \n\n\n')
        for i in range(N):
            x = curr(check2[i],check)
            for j in range(N):
                if j==(x-1)%N:
                    print(" Q ",end=' ')
                else:
                    print(" * ",end=' ')
            print('\n')
        print('\n\n\n')
        return True
    return False
def check_diagonals(i,ch):
    for j in range(N):
        if (check2[i]==((check[ch][0]+j,check[ch][1]+j)) or check2[i]==((check[ch][0]-j,check[ch][1]-j)) or
            check2[i]==((check[ch][0]+j,check[ch][1]-j)) or check2[i]==((check[ch][0]-j,check[ch][1]+j))):
            return True
    return False   
def check_all(check2,j):
    for i in range(len(check2)):
        if (check2[i][1]==check[j][1] or check2[i][0]==check[j][0] or check_diagonals(i,j)):
            return True
    return False

def curr(i,check):
    c = 0
    for x in check:
        if x==i:
            return c+1
        c+=1

if __name__=='__main__': 
    N  = int(input("enter a number for NxN grid : "))
    check2=list()
    check =list()
    total=0
    nq_ct=0
    for i in range(N):
        for j in range(N):
            check.append((i,j))
    prev_nq = [[0]*N for i in range(len(check))]
    for m in range(N):
        prev_vals = [[0]*N for i in range(N)]
        for k in range(N):
            if(len(check2)==N):
                x = display(check2,total+1)
                if x:
                    nq_ct+=1
                    total+=1
            del check2[:]
            if check[m] not in prev_vals[i]:
                prev_vals[0][k]=((check[m]))
            check2.append(check[m])
            prev = curr(check2[0],check)
            for i in range(N):
                pter = 0
                len_ch2 = len(check2)
                if len_ch2>0 and i<len_ch2:
                    prev=curr(check2[i],check)
                for j in range(prev,len(check)):
                    if check_all(check2,j) or check[j] in prev_vals[check[j][0]]:
                        continue
                    else:
                        prev_vals[check[j][0]][pter]=((check[j]))
                        check2.append(check[j])
                        pter+=1
                        break
    print("\n\n\n\nTOTAL NUMBER OF POSSIBLE PLACEMENTS ARE : ",total,'\n\n')