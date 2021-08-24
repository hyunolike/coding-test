from collections import deque

def BFS(a, b):
    global cnt
    Q = deque([[a, b]])
    flag = False
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if not (0<=nx<n and 0<=ny<m):
                continue
            if graph[nx][ny]==0 and not visited[nx][ny]:
                visited[nx][ny]=1
                Q.append([nx,ny])
                flag=True
    if flag:
        cnt += 1

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[0]*m  for _ in range(n)]
cnt = 0
dx=[-1,1,0,0]
dy=[0,0,-1,1]
for i in range(n):
    for j in range(m):
        BFS(i, j)

print(cnt)