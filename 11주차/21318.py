import sys
input=sys.stdin.readline
N=int(input())
music=list(map(int,input().split()))
Q=int(input())
Question=[list(map(int,input().split())) for _ in range(Q)]


sum,s=0,[0]
for i in range(N-1):
    if music[i+1]<music[i]:
        sum+=1
    s.append(sum)

print(s)
for x,y in Question:
    print(s[y-1]-s[x-1])