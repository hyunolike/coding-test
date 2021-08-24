import sys
from collections import deque
input = sys.stdin.readline

def BFS(a,b):
    Q=deque()
    Q.append([0,0,1])
    visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
    visited[0][0][1]=1

    while Q:
        x,y,c = Q.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][c]
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny]==1 and c==1:
                    visited[nx][ny][0]=visited[x][y][1]+1
                    Q.append([nx,ny,0])
                elif graph[nx][ny]==0 and visited[nx][ny][c]==0:
                    visited[nx][ny][c]=visited[x][y][c]+1
                    Q.append([nx,ny,c])
    return -1


n,m=map(int, input().split())
graph=list(list(map(int, input().rstrip())) for _ in range(n))
dx=[-1,1,0,0]
dy=[0,0,1,-1]
print(BFS(0,0))