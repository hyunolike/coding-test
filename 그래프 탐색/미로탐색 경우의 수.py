def DFS(x,y):
    global answer
    if x==6 and y==6:
        answer+=1
        return 0
    else:
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if not (0<=nx<=6 and 0<=ny<=6):
                continue
            if graph[nx][ny]==0 and not visited[nx][ny]:
                visited[nx][ny]=1
                DFS(nx, ny)
                visited[nx][ny]=0

graph=[list(map(int, input().split())) for _ in range(7)]
visited=[[0]*7 for _ in range(7)]
dx,dy=[0,0,-1,1],[-1,1,0,0]
visited[0][0]=1
answer=0
DFS(0,0)
print(answer)