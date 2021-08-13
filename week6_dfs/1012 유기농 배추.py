from collections import deque

t = int(input())

def BFS(x,y):
    dx=[-1,0,1,0]
    dy=[0,-1,0,1]
    queue=deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<m:
                if field[nx][ny]==1:
                    queue.append((nx,ny))
                    field[nx][ny]=2

for _ in range(t):
    m,n,k = map(int, input().split())
    field=[[0]*m for _ in range(n)]
    cnt = 0

    for _ in range(k):
        x,y = map(int, input().split())
        field[y][x]=1
    
    for i in range(n):
        for j in range(m):
            if field[i][j]==1:
                BFS(i,j)
                cnt+=1
    print(cnt)
