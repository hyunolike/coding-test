import sys
input=sys.stdin.readline
N,K,B=map(int,input().split())
broken=[int(input()) for _ in range(B)]
sign=[0 for _ in range(N)]

for i in broken:
    sign[i-1]=1

sumlist=[0]
sum=0
for i in range(N):
    sum+=sign[i]
    sumlist.append(sum)

#print(sumlist)

ans=B
for i in range(K,N+1):
 #   print(i,i-K,sumlist[i]-sumlist[i-K])
    ans=min(ans,sumlist[i]-sumlist[i-K])
print(ans)
