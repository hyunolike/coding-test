# import sys
# input=sys.stdin.readline
# from collections import deque

# N,M=map(int,input().split())

# grid=[ input().rstrip() for _ in range(N) ]

# dx=[1,0,0,-1]
# dy=[0,1,-1,0]

# visit1=[ [-1]*M for _ in range(N) ]
# visit1[0][0]=1

# visit2=[ [-1]*M for _ in range(N) ]
# visit2[0][0]=1

# queue=deque()
# queue.append((0,0,False))
# while queue:
#     tempX,tempY,f=queue.popleft()
#     if tempX==N-1 and tempY==M-1:
#         break
#     for i in range(4):
#         mx=tempX+dx[i]
#         my=tempY+dy[i]
#         if (0<=mx<N) and (0<=my<M):
#             if grid[mx][my]=='0' and visit1[mx][my]==-1:
#                 visit1[mx][my]=visit1[tempX][tempY]+1
#                 queue.append((mx,my,f))
#             elif grid[mx][my]=='1' and visit2[mx][my]==-1:
#                 if not f:
#                     visit2[mx][my]=visit2[tempX][tempY]+1
#                     queue.append((mx,my,True))
                    
# for i in visit1:
#     print(i)
# print(visit1[N-1][M-1])
# for i in visit2:
#     print(i)
# print(visit2[N-1][M-1])


import sys 
dx = [1, -1, 0, 0] 
dy = [0, 0, 1, -1] 
def bfs(): 
    q = [] 
    q.append([0, 0, 1]) 
    visit = [[[0] * 2 for _ in range(m)] for __ in range(n)] 
    visit[0][0][1] = 1 
    while q: 
        x, y, w = q.pop(0) 
        if x == n - 1 and y == m - 1: 
            return visit[x][y][w] 
        for i in range(4): 
            nx = x + dx[i] 
            ny = y + dy[i] 
            if 0 <= nx < n and 0 <= ny < m: 
                if location[nx][ny] == 1 and w == 1: 
                    visit[nx][ny][0] = visit[x][y][1] + 1 
                    q.append([nx, ny, 0]) 
                elif location[nx][ny] == 0 and visit[nx][ny][w] == 0: 
                    visit[nx][ny][w] = visit[x][y][w] + 1 
                    q.append([nx, ny, w]) 
    return -1 
n, m = map(int, sys.stdin.readline().split()) 
location = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)] 
print(bfs())
