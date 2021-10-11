from collections import deque
n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
di = (0,0,1)
dj = (1,-1,0)

dp = [[[-1000000001] * 3 for _ in range(m)] for _ in range(n)]

q = deque([(mat[0][0], 0, 0, 0)])
dp[0][0][0] = max(dp[0][0][0], mat[0][0])

c = 0
while q:
    c+=1
    cnt, x, y, pre_d = q.popleft()

    for k in range(3):
        newX, newY = x+di[k], y+dj[k]
        if pre_d^1 == k:
            continue
        if not (0 <= newX<n and 0<= newY<m):
            continue
        if dp[newX][newY][k] < cnt + mat[newX][newY]:
            dp[newX][newY][k] = cnt + mat[newX][newY]

            q.append((cnt + mat[newX][newY], newX, newY, k))

print(max(dp[n-1][m-1]))
