from collections import deque
import sys
sys.setrecursionlimit(100000)
input=sys.stdin.readline

A,B=map(int,input().split())

grid=[ input().split() for _ in range(A) ]


dx=[0,0,1,-1]
dy=[1,-1,0,0]
def sol(x,y):
    visit=[[0]*B for _ in range(A)]    
    visit[x][y]=1
    queue=deque()
    queue.append((x,y))
    count=0
    while queue:
        tempX,tempY=queue.popleft()
        
        for i in range(4):
            mx=tempX+dx[i]
            my=tempY+dy[i]
            if 0<=mx<A and 0<=my<B:
                if  visit[mx][my]==0 and grid[mx][0][my]=='L':
                    visit[mx][my]=visit[tempX][tempY]+1
                    count=max(count,visit[mx][my])
                    queue.append((mx,my))

    return count-1

result=0
for i in range(A):
    for j in range(B):
        if grid[i][0][j]=='L':
            result=max(result,sol(i,j))
print(result)

# 7 7
# WLLLLLW
# LWLWLWW
# LLLWLWW
# LWWWLWW
# LLLLLWW
# LWWWWWW
# WWWWWWW