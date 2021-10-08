import sys
input=sys.stdin.readline

n=int(input())
T,P=[],[]
dp=[0]*(n+1)
for i in range(n):
    t,p=map(int,input().split())
    T.append(t)
    P.append(p)

for i in range(n):
    if i+T[i]<=n:
        dp[i+T[i]]=max(dp[i+T[i]], dp[i]+P[i])
    dp[i+1]=max(dp[i+1], dp[i])

print(max(dp))