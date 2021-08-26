import sys
input=sys.stdin.readline
from collections import deque
from itertools import combinations
import copy
dx=[1,0,0,-1]
dy=[0,1,-1,0]

N,M=map(int,input().split())

grid=[ list(map(int,input().split())) for _ in range(N) ]

for i in grid:
    print(i)



def calcSafe(mapp):
    for i in range(N):
        for j in range(M):
            if mapp[i][j]==2:
                visit=[ [0]*M for _ in range(N) ]
                queue=deque()
                queue.append((i,j))
                visit[i][j]=1
                while queue:
                    tempX,tempY=queue.popleft()
                    for i in range(4):
                        mx=tempX+dx[i]
                        my=tempY+dy[i]
                        if 0<=mx<N and 0<=my<M:
                            if visit[mx][my]==0 and mapp[mx][my]==0:
                                mapp[mx][my]=2
                                visit[mx][my]=1
                                queue.append((mx,my))
    count=0
    for pp in range(N):
        for ll in range(M):
            if mapp[pp][ll]==0:
                count+=1
    return count



result=-999
list=[]
for i in range(N):
    for j in range(M):
        if grid[i][j]==0:
            list.append([i,j])

c=combinations(list,3)
for abc in c:
    grid2=copy.deepcopy(grid)
    for hhh in range(0,3):
        grid2[abc[hhh][0]][abc[hhh][1]]=1
    for i in range(N):
        for j in range(M):
            if grid2[i][j]==2:
                visit=[ [0]*M for _ in range(N) ]
                queue=deque()
                queue.append((i,j))
                #visit[i][j]=1
                while queue:
                    tempX,tempY=queue.popleft()
                    for i in range(4):
                        mx=tempX+dx[i]
                        my=tempY+dy[i]
                        if 0<=mx<N and 0<=my<M:
                            if visit[mx][my]==0 and grid2[mx][my]==0:
                                grid2[mx][my]=2
                                #visit[mx][my]=1
                                queue.append((mx,my))
    count=0
    for pp in range(N):
        for ll in range(M):
            if grid2[pp][ll]==0:
                count+=1
    if result<count:
        result=count
        print(result,abc,'aaa')
        for i in grid2:
            print(i)
        
        #print(grid2)

print(result)


