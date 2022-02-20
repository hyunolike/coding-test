import sys
input=sys.stdin.readline
from collections import deque


N,K=map(int,(input().split()))
grid=[ list(map(int,(input().split()))) for _ in range(N) ]
S,X,Y=map(int,(input().split()))
dx=[1,0,0,-1]
dy=[0,1,-1,0]

virus=[]
for i in range(N):
    for j in range(N):
        if grid[i][j]!=0:
            virus.append( [grid[i][j],i,j,0]  )
virus.sort()
#print(virus)


Q=deque(virus)
while Q:
    VirusNum, XX, YY, time = Q.popleft()
    if time==S:
        break
    for i in range(4):
        mx=XX+dx[i]
        my=YY+dy[i]
        if 0<=mx<N and 0<=my<N:
            if grid[mx][my]==0:
                grid[mx][my]=VirusNum
                Q.append( [VirusNum,mx,my,time+1] )
                #print(grid)
print(grid[X-1][Y-1])