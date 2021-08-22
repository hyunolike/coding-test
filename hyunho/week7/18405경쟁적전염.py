import sys
from collections import deque

input = lambda : sys.stdin.readline()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, K = map(int, input().split())
test = []
data = []

for i in range(N):
    test.append(list(map(int, input().split())))
    for j in range(N):
        if test[i][j] != 0:
            data.append((test[i][j], i, j, 0))

S, X, Y = map(int, input().split())

data.sort()
q = deque(data)

while q:
    virus, x, y, time = q.popleft()
    if time == S:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if test[nx][ny] == 0:
                test[nx][ny] = virus
                q.append((virus, nx, ny, time+1))

print(test[X-1][Y-1])
