def DFS(x,y):
    global answer
    if x==ex and y==ey:
        answer+=1
    else:
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if not (0<=nx<=n-1 and 0<=ny<=n-1):
                continue
            if graph[x][y]<graph[nx][ny] and not visited[nx][ny]:
                visited[nx][ny]=1
                DFS(nx,ny)
                visited[nx][ny]=0

n=int(input())
graph=[list(map(int, input().split())) for _ in range(n)]
visited=[[0]*n for _ in range(n)]
dx,dy=[0,0,-1,1],[-1,1,0,0]
start,end=2e9,0
answer=0
for i in range(n):
    for j in range(n):
        if start>graph[i][j]:
            start=graph[i][j]
            sx,sy=i,j
        if end<graph[i][j]:
            end=graph[i][j]
            ex,ey=i,j
DFS(sx,sy)
print(answer)