from collections import deque

n=int(input())
graph=[list(map(int,input())) for _ in range(n)]
answer=[]
dx=[0,0,-1,1]
dy=[-1,1,0,0]
q=deque()
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            graph[i][j]=0
            q.append((i,j))
            cnt=1
            while q:
                x,y=q.popleft()
                for k in range(4):
                    nx,ny=x+dx[k],y+dy[k]
                    if not (0<=nx<=n-1 and 0<=ny<=n-1):
                        continue
                    if graph[nx][ny]==1:
                        graph[nx][ny]=0
                        q.append((nx,ny))
                        cnt+=1
            answer.append(cnt)

print(len(answer))
answer.sort()
for a in answer:
    print(a)