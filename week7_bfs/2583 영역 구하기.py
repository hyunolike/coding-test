from collections import deque

def BFS(i,j):
    Q=deque([[i,j]])
    cnt = 1
    while Q:
        x, y = Q.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if not (0<=nx<m and 0<=ny<n):
                continue
            if graph[nx][ny]==0:
                graph[nx][ny]=1
                Q.append([nx,ny])
                cnt+=1
    answer.append(cnt)


m,n,k=map(int,input().split())
graph=[[0]*n for _ in range(m)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
answer = []
for _ in range(k):
    x1,y1,x2,y2 = map(int,input().split())

    for i in range(y1,y2):
        for j in range(x1,x2):
            graph[i][j]=1

for i in range(m):
    for j in range(n):
        if graph[i][j]==0:
            graph[i][j]=1
            BFS(i, j)

print(len(answer))
answer.sort()
for a in answer:
    print(a, end=' ')