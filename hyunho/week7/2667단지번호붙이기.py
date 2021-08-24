import sys
from collections import deque, defaultdict

input = sys.stdin.readline

N = int(input())
graph = [list(map(int , input().rstrip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
cnt = 0
cnt_dict = defaultdict(int)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, cnt):
    q = deque()
    q.append((x,y))
    visited[x][y] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if graph[nx][ny] == 1 and visited[nx][ny] == False:
                q.append((nx, ny))
                visited[nx][ny] = True
                cnt_dict[cnt] += 1

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visited[i][j] == False:
            cnt += 1
            cnt_dict[cnt] += 1
            bfs(i,j,cnt)

print(cnt)
print('\n'.join(map(str, sorted(cnt_dict.values()))))