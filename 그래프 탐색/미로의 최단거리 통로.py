
from collections import deque

graph=[list(map(int, input().split())) for _ in range(7)]
visited=[[0]*7 for _ in range(7)]
q=deque()
q.append([0,0])
visited[0][0]=0
dx,dy=[0,0,-1,1],[-1,1,0,0]

while q:
    x,y=q.popleft()
    
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if not (0<=nx<=6 and 0<=ny<=6):
            continue
        if graph[nx][ny]==0 and not visited[nx][ny]:
            visited[nx][ny]=visited[x][y]+1
            q.append([nx,ny])
if visited[6][6]:
    print(visited[6][6])
else:
    print(-1)