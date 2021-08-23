import sys
input=sys.stdin.readline
sys.setrecursionlimit(1000000)
from collections import deque
N=int(input().rstrip())

grid=[ list(input().rstrip()) for _ in range(N) ]

visit=[ [0]*N for _ in range(N) ]

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def sol(x,y):
    queue=deque()
    queue.append((x,y,0))
    result=[]
    while queue:
        tempX,tempY,count=queue.popleft()
        
        visit[tempX][tempY]=1
        if tempX==N-1 and tempY==N-1:
            print(count)
            return count
            
        for i in range(4):
            mx=tempX+dx[i]
            my=tempY+dy[i]
            if (0<=mx<N) and (0<=my<N):
                if grid[mx][my]=='1' and visit[mx][my]==0:
                    queue.append((mx,my,countㅁ
                elif grid[mx][my]=='0' and visit[mx][my]==0:
                    grid[mx][my]='1'
                    count=count+1
                    queue.append((mx,my,count))
    print(count)
sol(0,0)