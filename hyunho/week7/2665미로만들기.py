from collections import deque
import sys
input = lambda : sys.stdin.readline()

def bfs():
    q = deque()
    q.append((0,0))
    dist[0][0] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if dist[nx][ny] == -1:
                if room[nx][ny] == '0':
                    dist[nx][ny] = dist[x][y] + 1 # 검은방이면 이동거리는 전보다 +1 해주고 사용
                    q.append((nx,ny))
                else:
                    dist[nx][ny] = dist[x][y]
                    q.appendleft((nx, ny)) # 먼저 흰방을 방문하기 위한 로직

n = int(input())
room = [list(input().rstrip()) for _ in range(n)]
dist = [[-1]*n for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

bfs()
print(dist[n-1][n-1])

