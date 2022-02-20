from itertools import combinations

N,S=map(int,input().split())
numbers=list(map(int,input().split()))

c=list()
for i in range(N):
    c.append( (combinations(numbers,i+1) ))

count=0
for i in c:
    for j in i:
        if sum(j)==S:
            count+=1
           
print(count)