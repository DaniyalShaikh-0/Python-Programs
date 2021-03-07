from collections import Counter
def countTriplets(arr, r):
    count=0
    i=0
    j=1
    k=2
    c1 = Counter(arr)
    c2 = Counter()
    for i in arr:
        j = int(i/r)
        k = i*r
        c1[i]-=1
        if i%r==0:
            if (c1[k]*c2[j])!=0:
                count+=c1[k]*c2[j]
        c2[i]+=1
    return count


if __name__ == '__main__':

    f1 = open('input05.txt','r')
    st = f1.read().rstrip().split()
    st = [int(i) for i in st]
    n =st[0]

    r = st[1]
    # print(list(st[2:]))
    print(countTriplets(st[2:], r))
