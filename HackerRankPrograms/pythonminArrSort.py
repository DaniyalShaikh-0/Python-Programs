def is_sort(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True
# Complete the minimumSwaps function below.
def swap(n,ind,arr):
    t=arr[n]
    arr[n]=arr[ind]
    arr[ind]=t
def minimumSwaps(arr):
    min_=0
    i=0
    while True:
        if is_sort(arr) or i==len(arr):
            break
        if i+1!=arr[i]:
            #print('swapping values : ',arr[i],' and : ',arr[arr[i]-1])
            swap(i,arr[i]-1,arr)
            min_+=1
        else:
            i+=1
    #print(arr)
    return min_

if __name__ == '__main__':

    n = int(input())

    arr = list()

    for i in range(n):
        arr.append(n-i)
    #print (arr)
    print(minimumSwaps(arr))
   
   # print (arr)