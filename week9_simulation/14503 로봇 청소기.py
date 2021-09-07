n, m = map(int, input().split())
r,c,d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

dx=[-1,0,1,0] #북,동,남,서
dy=[0,1,0,-1]

def DFS(x, y, d):
    global answer
    if graph[x][y]==0:
        graph[x][y]=2
        answer+=1

    for _ in range(4):
        idx=(d+3)%4
        nx,ny=x+dx[idx],y+dy[idx]
        if graph[nx][ny]==0:
            DFS(nx,ny,idx)
            return 0
        d=idx
    nd=(d+2)%4 # 후진 위치 지정
    nx,ny=x+dx[nd],y+dy[nd]
    if graph[nx][ny]==1:
        return 0
    DFS(nx,ny,d) # 방향을 유지한 채 후진
        
answer = 0
DFS(r, c, d)
print(answer)
