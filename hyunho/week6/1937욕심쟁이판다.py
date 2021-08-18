import sys
sys.setrecursionlimit(10 ** 6)
input = lambda : sys.stdin.readline()

N = int(input())
trees = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dp = [[-1] * N for _ in range(N)]

def dfs(x, y):
    if dp[x][y] < 0:
        dp[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and trees[nx][ny] > trees[x][y]:
                dp[x][y] = max(dp[x][y], dfs(nx, ny))
        dp[x][y] += 1
    return dp[x][y]

ans = 0
for i in range(N):
    for j in range(N):
        ans = max(ans, dfs(i,j))

print(ans)