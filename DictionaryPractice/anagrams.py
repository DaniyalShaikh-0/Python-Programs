from collections import Counter

def sherlockAndAnagrams(s):
    count=Counter()
    for i in range(1,len(s)):
        for j in range(0,len(s)-i+1):
            count["".join(sorted(s[j:j+i]))]+=1
    #count = Counter(("".join(sorted(s[j:j+i])) for i in range(1,len(s)) for j in range(0,len(s)-i+1) ))
    x=0
    # for i in count:
    #     print(i)
    print(count)
    return sum(sum(range(i)) for i in count.values())

for _ in range(int(input())):
    s = input()
    print(sherlockAndAnagrams(s))