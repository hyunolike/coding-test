from collections import defaultdict
n = int(input())
numbers = [list(map(str, input())) for _ in range(n)]

hash=defaultdict(int)
for num in numbers:
    for i in range(len(num)):
        hash[num[i]]+=10**(len(num)-i-1)
hash = sorted(hash.items(), key=lambda x:x[1], reverse=True)

hash_map={}
value = 9
for alpha, _ in hash:
    hash_map[alpha]=value
    value-=1

answer=[]
for num in numbers:
    ans=''
    for alpha in num:
        ans+=str(hash_map[alpha])
    answer.append(int(ans))
print(sum(answer))