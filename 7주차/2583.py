import sys
input=sys.stdin.readline
from collections import deque

dx=[1,0,0,-1]
dy=[0,1,-1,0]

M,N,K=map(int,input().split())

grid=[ [0]*N for _ in range(M) ]

square=[]
for _ in range(K):
    square.append(list(map(int,input().split())))


for i in square:
    x1,y1,x2,y2=i
    for j in range(x1,x2):
        for k in range(y1,y2):
            grid[k][j]=1

visit=[[0]*N for _ in range(M) ]

def bfs(x,y):
    visit[x][y]=1
    queue=deque()
    queue.append((x,y))
    global area
    area=1
    while queue:
        tempX,tempY=queue.popleft()
        for i in range(4):
            mx=tempX+dx[i]
            my=tempY+dy[i]
            if 0<=mx<M and 0<=my<N:
                if grid[mx][my]==0 and visit[mx][my]==0:
                    visit[mx][my]=1
                    queue.append((mx,my))
                    area+=1
    temp.append(area)
temp=[]
count=0
for i in range(M):
    for j in range(N):
        if visit[i][j]!=1 and grid[i][j]==0:
            bfs(i,j)
            count+=1
temp.sort()
print(count)
for i in temp:
    print(i,end=' ')
print()


