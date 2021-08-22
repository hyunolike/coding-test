import sys
from collections import deque
input = sys.stdin.readline

t=int(input())
for _ in range(t):
    l=int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())

    dx=[-2,-2,2,2,1,-1,1,-1]
    dy=[1,-1,1,-1,-2,-2,2,2]

    visited = [[-1]*l for _ in range(l)]
    visited[sx][sy] = 0
    Q=deque()
    Q.append([sx,sy])
    
    while Q:
        x, y = Q.popleft()
        if x==ex and y==ey:
            break
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<l and 0<=ny<l and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y]+1
                Q.append([nx,ny])
    
    print(visited[ex][ey])