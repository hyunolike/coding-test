import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
grid = [list(input().rstrip()) for i in range(N)]
direction = ((1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1))

def dfs(i, j, v):
    if v == len(test):
        dp[i][j][v] = 1
        return 1
    if dp[i][j][v] >= 0:
        return dp[i][j][v]

    ret = 0
    for di, dj in direction:
        ni, nj = (di + i) % N, (dj + j) % M
        if 0 <= ni < N and 0 <= nj < M and grid[ni][nj] == test[v]:
            # print(i, j, ni, nj, v)
            ret += dfs(ni, nj, v + 1)
    dp[i][j][v] = ret
    return ret


for _ in range(K):
    test = list(input().rstrip())
    answer = 0
    dp = [[[-1 for i in range(6)] for i in range(11)] for i in range(11)]
    for i in range(N):
        for j in range(M):
            if grid[i][j] == test[0]:
                answer += dfs(i, j, 1)

    print(answer)