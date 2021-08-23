import sys
input=sys.stdin.readline

from collections import deque



def sol(X,K):
    queue=deque()
    queue.append(X)
    count=0
    while queue:
        temp=queue.popleft()
        for i in grid[temp]:
            if visit[i]==-1:
                visit[i]=count+1
                queue.append(i)
        count+=1
    #print(visit)
    for i in range(N+1):
        if visit[i]==K:
            print(i)
    if K not in visit:
        print(-1)

    

N,M,K,X=map(int,input().split())

grid=[[]*N for _ in range(N+1)]


for i in range(M):
    a,b=map(int,input().split())
    grid[a].append(b)




visit=[-1]*(N+1)
visit[X]=0
sol(X,K)
# if K==1 and grid[X]:
#     for i in grid[X]:
#         print(i)
# if K==1 and not grid[X]:
#     print(-1)
# else:
#     sol(X,K)
# 5 4 2 1
# 1 2
# 1 3
# 2 3
# 2 5

# 4 4 1 1
# 1 3
# 1 2
# 2 3
# 2 4



