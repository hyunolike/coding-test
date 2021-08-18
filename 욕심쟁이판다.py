import sys
from collections import deque

sys.setrecursionlimit(40000)
n = int(sys.stdin.readline().rstrip())
arr = []
dp = [[-1 for _ in range(n)] for _ in range(n)]
d = [[1, 0], [-1, 0], [0, 1], [0, -1]]
answer = 0

for i in range(n):
    x = list(map(int, sys.stdin.readline().rstrip().split()))
    arr.append(x)


def isin(y, x):
    if -1 < y < n:
        if -1 < x < n: return True
    return False


def dfs(y, x):
    global dp, answer

    if dp[y][x] != -1: return dp[y][x]

    tmp = 0
    dp[y][x] = 1

    for i in range(4):
        ny = y + d[i][0]
        nx = x + d[i][1]

        if isin(ny, nx):
            if arr[ny][nx] > arr[y][x]:
                tmp = max(tmp, dfs(ny, nx))

    dp[y][x] += tmp

    if answer < dp[y][x]: answer = dp[y][x]

    return dp[y][x]


for i in range(n):
    for j in range(n):
        dfs(i, j)

print(answer)
