import sys
import time
sys.setrecursionlimit(1000000)
input=sys.stdin.readline
from collections import deque

N,L,R=map(int,input().split())
visit=[[0]*N for _ in range(N) ]
populationGrid=[]
for _ in range(N):
    populationGrid.append(list(map(int,input().split())))

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def sol(x,y):
    queue=deque()
    queue.append([x,y])
    year=0
    count=0
    while True:
        visit=[[0]*N for _ in range(N) ]
        while queue:
            a,b=queue.popleft()
            # print(a,b,'asdf')
            # print(visit)
            for i in range(4):
                mx=a+dx[i]
                my=b+dy[i]
                if (0<=mx<N) and (0<=my<N) and visit[mx][my]==0:
                    if (L<=abs(populationGrid[mx][my]-populationGrid[a][b])<=R):
                        queue.append([mx,my])
                        visit[mx][my]=1
                        count+=1
    
        sum=0
        for i in range(N):
            for j in range(N):
                if visit[i][j]==1:
                    sum+=populationGrid[i][j]
        for i in range(N):
            for j in range(N):
                if visit[i][j]==1:
                    print(i,j)
                    populationGrid[i][j]=int(sum/count)
        print(populationGrid)
        if count==0:
            break
        count=0
        year+=1
    print(year)


sol(0,0)

            
