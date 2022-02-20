import sys
input=sys.stdin.readline

N=int(input())

tree=[[] for _ in range(N+1)]

for _ in range(N-1):
    a,b=map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

visit=[0 for _ in range(N+1)]
result=[0 for _ in range(N+1)]
que=[1]
print(tree)
print(visit)
while que:
    point=que.pop(0)
    for i in tree[point]:
        if visit[i]==0:
            result[i]=point
            visit[i]=999
            que.append(i)


for i in range(2,N+1):
    print(result[i])

