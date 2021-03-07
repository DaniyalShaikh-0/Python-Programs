listOfStr = ["hello", "at" , "test" , "this" , "here" , "now" ]
# dictOfWords = { i : 6 for i in range(0, len(listOfStr) ) }
# print(dictOfWords)
queries = []
for _ in range(3):
        queries.append(list(map(int, input().rstrip().split())))
x = dict()
p=2
for i in queries:
    try:
        x[i[0]]+=i[2]
    except KeyError:
        x[i[0]]=i[2]
    try:
        x[i[1]+1]-=i[2]
    except KeyError:
        x[i[1]+1]=-i[2]
y=list(x.keys())
y.sort()
sum_=0
max_=0
for i in y:
    sum_=sum_+x[i]
    if sum_ > max_:
        max_+=x[i]
# for i in D:
#     sum_+=i
#return max_