import sys
sys.setrecursionlimit(10 ** 8)
read = lambda: sys.stdin.readline().strip()

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]


def dfs(cx, cy):
    if dp[cx][cy] != -1:	# 이미 방문한 곳이면 그만큼 더해줌
        return dp[cx][cy]

    cnt = 0
    for i in range(4):
        nx, ny = cx + dx[i], cy + dy[i]

        if not 0 <= nx < n or not 0 <= ny < m:
            continue
        if arr[nx][ny] >= arr[cx][cy]:
            continue
        cnt += dfs(nx, ny)

    dp[cx][cy] = cnt

    return dp[cx][cy]


n, m = map(int, read().split())
arr = [list(map(int, read().split())) for _ in range(n)]

dp = [[-1] * m for _ in range(n)]
dp[n - 1][m - 1] = 1
print(dfs(0, 0))