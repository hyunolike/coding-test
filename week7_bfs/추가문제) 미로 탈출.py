from collections import deque

def BFS(a, b):
    Q=deque([[a,b]])
    while Q:
        x,y = Q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if not (0<=nx<n and 0<=ny<m): # 범위를 벗어나면 무시
                continue
            if graph[nx][ny]==0: # 벽인 경우 무시
                continue
            if not visited[nx][ny]:
                visited[nx][ny]=visited[x][y]+1
                Q.append([nx,ny])

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,1,-1]
visited[0][0]=1
BFS(0,0)
print(visited[n-1][m-1])