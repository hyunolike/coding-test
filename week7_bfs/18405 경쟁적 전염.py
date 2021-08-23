import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
s, x, y = map(int, input().split())

queue = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            queue.append((graph[i][j], i, j, 0))

queue.sort()
queue = deque(queue)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    virus, a, b, time = queue.popleft()
    if time == s:
        break
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
            graph[nx][ny] = virus
            queue.append((virus, nx, ny, time + 1))

print(graph[x - 1][y - 1])