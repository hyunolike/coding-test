from collections import deque

n=int(input())
graph=[list(map(int, input().split())) for _ in range(n)]
visited=[[0]*n for _ in range(n)]
q=deque()
visited=[0][0]=1
q.append([0,0])
dx=[0,0,-1,1]
dy=[-1,1,0,0]

while q:
    x,y=q.popleft()
    
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if (0<=nx<=n-1 and 0<=ny<=n-1) and graph[nx][ny] and not visited[nx][ny]:
            visited[nx][ny]=visited[x][y]+1
            q.append([nx,ny])

print(visited[n-1][n-1])
