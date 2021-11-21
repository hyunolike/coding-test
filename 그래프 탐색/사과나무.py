from collections import deque

n=int(input())
graph=[list(map(int, input().split())) for _ in range(n)]
visited=[[0]*n for _ in range(n)]
q=deque()
mid=n//2
q.append([mid, mid])
answer=graph[mid][mid]
visited[mid][mid]=1
dx=[0,0,-1,1]
dy=[-1,1,0,0]
L=0

while q:
    if L==mid:
        break
    size=len(q)
    for j in range(size):
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]

            if (0<=nx<=n-1 and 0<=ny<=n-1) and not visited[nx][ny]:
                visited[nx][ny]=1
                answer+=graph[nx][ny]
                q.append([nx,ny])
    L+=1
print(answer)