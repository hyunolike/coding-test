#10026 적록색약

#문제풀이 1:


import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
ans1 = 0
ans2 = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, c, arr):
    queue = deque()
    queue.append((x, y))
    arr[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < N and 0 <= ny < N) and arr[nx][ny] != 0:
                if arr[nx][ny] == c:
                    queue.append((nx, ny))
                    arr[nx][ny] = 0


graph = [list(map(str, input().rstrip())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if graph[i][j] == "R" or graph[i][j] == "G":
            visited[i][j] = 1
        else:
            visited[i][j] = 2


for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            bfs(i, j, graph[i][j], graph)
            ans1 += 1
        if visited[i][j] != 0:
            bfs(i, j, visited[i][j], visited)
            ans2 += 1

print(ans1, ans2)