dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]


def dfs(x, y, cnt, p):
    global ans

    if cnt == n:
        ans += p
        return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if board[nx][ny]:
            continue
        if not 0 <= nx < (2 * n) + 1 or not 0 <= ny < (2 * n) + 1:
            continue

        board[nx][ny] = 1
        dfs(nx, ny, cnt + 1, p * poss[i] * 0.01)
        board[nx][ny] = 0


n, east, west, south, north = map(int, input().split())
poss = [north, east, south, west]   # 위의 dx, dy 랑 순서 맞춰줌

board = [[0] * (2 * n + 1) for _ in range(2 * n + 1)]
board[n][n] = 1

ans = 0

dfs(n, n, 0, 1)
print(ans)