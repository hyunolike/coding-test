from collections import deque

n=int(input())
graph=[list(map(int, input().split())) for _ in range(n)]
visited=[[0]*n for _ in range(n)]
answer=0
q=deque()
dx,dy=[0,0,-1,1],[-1,1,0,0]

for h in range(1, 101):
    ground=graph[:]
    cnt=0
    for i in range(n):
        for j in range(n):
            if ground[i][j]<=h:
                ground[i][j]=0
                
    visited=[[0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if ground[i][j] and not visited[i][j]:
                q.append([i,j])
                cnt+=1            
            
            while q:
                x,y=q.popleft()
                for k in range(4):
                    nx,ny=x+dx[k],y+dy[k]
                    if not (0<=nx<=n-1 and 0<=ny<=n-1):
                        continue
                    if ground[nx][ny] and not visited[nx][ny]:
                        visited[nx][ny]=1
                        q.append([nx,ny])
                        
    answer=max(answer, cnt)
    
print(answer)