from collections import deque

n=int(input())
graph=[list(map(int, input().split())) for _ in range(n)]
answer=0
dx,dy=[0,0,-1,1,-1,-1,1,1],[1,-1,0,0,-1,1,-1,1]
q=deque()

for i in range(n):
    for j in range(n):
        if graph[i][j]:
            answer+=1
            graph[i][j]=0
            q.append([i,j])
            
            while q:
                x,y=q.popleft()
                
                for k in range(8):
                    nx,ny=x+dx[k],y+dy[k]
                    if not (0<=nx<=n-1 and 0<=ny<=n-1):
                        continue
                    if graph[nx][ny]:
                        graph[nx][ny]=0
                        q.append([nx,ny])
print(answer)