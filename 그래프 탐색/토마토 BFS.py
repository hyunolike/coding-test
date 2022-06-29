from collections import deque

m,n=map(int, input().split())
graph=[list(map(int, input().split())) for _ in range(n)]
visited=[[0]*m for _ in range(n)]
dx,dy=[0,0,-1,1],[-1,1,0,0]
q=deque()

for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            q.append([i,j])
            
while q:
    x,y=q.popleft()
    
    for k in range(4):
        nx,ny=x+dx[k],y+dy[k]
        if not (0<=nx<=n-1 and 0<=ny<=m-1):
            continue
        if graph[nx][ny]==0 and not visited[nx][ny]:
            graph[nx][ny]=1
            visited[nx][ny]=visited[x][y]+1
            q.append([nx,ny])

flag=True
for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            flag=False
if flag:
    answer=0
    for v in visited:
        answer=max(answer,max(v))
    print(answer)
else:
    print(-1)