from collections import deque
import sys
input = lambda : sys.stdin.readline()

def bfs(x, y):
    q.append((x,y))
    visited = [[0] * m for _ in range(n)]
    visited[x][y] = 1
    num = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if treasure_map[nx][ny] == 'L' and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    num = max(num, visited[nx][ny])
                    q.append((nx,ny))
    return num - 1


n, m = map(int, input().split())
treasure_map = [list(map(str,input().rstrip())) for _ in range(n)]
q = deque()
dx = [-1,1,0,0]
dy = [0,0,-1,1]


cnt = 0
for i in range(n):
    for j in range(m):
        if treasure_map[i][j] == 'L':
            cnt = max(cnt, bfs(i,j))

print(cnt)