import sys
import copy
input=sys.stdin.readline
from collections import deque
N,M,D=map(int,input().split())

grid1 = [ list(map(int,input().split())) for _ in range(N) ]

Q=deque()
visit=[ [0]*M for _ in range(N) ]

def dist(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)

def goFoward(grid):
    grid[1:]=grid[0:-1]
    grid[0]=[0]*M
    return grid

def isValid(grid):
    for i in grid:
        if 1 in i:
            return True

def sol(ii,jj,kk,grid):
    count=0
    while True:
        if not isValid(grid):
            break
        
        Q.append(ii)
        Q.append(jj)
        Q.append(kk)
        stack=[]
        
        while Q:
            pop = Q.popleft()
            d=99999
            f=False
            for x1 in range(N-1,0,-1):
                for y1 in range(M):
                    if grid[x1][y1]==1 :
                        distance=dist(x1,y1,N,pop-1)
                        if distance<=D:
                            if f:
                                if y1<tempY and distance==dist(tempX,tempY,N,pop-1):
                                    tempX,tempY=x1,y1
                            if distance<d:
                                d=distance
                                tempX,tempY=x1,y1
                                f=True
                        
            if f:
                stack.append((tempX,tempY))

        for i,j in stack:
            if grid[i][j]==1:
                count=count+1
                grid[i][j]=0
        
        grid=goFoward(grid)
    return count

result=0
for i in range(1,M-1):
   for j in range(i+1,M):
       for k in range(j+1,M+1):
           temp=copy.deepcopy(grid1)
           result=max(result,sol(i,j,k,temp))
print(result)
