import collections

def arrayManipulation(n, queries):
    c = collections.Counter()
    for a,b,k in queries:
        c[a]  +=k
        c[b+1]-=k
    arrSum = 0
    maxSum = 0
    print('Counnter : ',end=' ')
    print(c)
    print('\n\n')
    # for i in sorted(c)[:-1]:
    #     print(i)
        # arrSum+= c[i]
        # maxSum = max(maxSum,arrSum)
    print('After sort',end=' ')
    print(sorted(c))
    return maxSum

n,m = map(int,input().split())
queries = [list(map(int,input().split())) for _ in range(m)]
print(arrayManipulation(n, queries))