from collections import deque
import sys

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    move_q = deque()
    q.append([x, y])
    c[x][y] = 1
    people, cnt = 0, 0
    while q:
        x, y = q.popleft()
        move_q.append([x, y])
        people += a[x][y]
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not c[nx][ny]:
                if l <= abs(a[x][y] - a[nx][ny]) <= r:
                    c[nx][ny] = cnt
                    q.append([nx, ny])

    while move_q:
        x, y = move_q.popleft()
        a[x][y] = people // cnt

    if cnt == 1:
        return 0
    return 1

n, l, r = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

ans = 0
while True:
    q = deque()
    c = [[0]*n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not c[i][j]:
                cnt += bfs(i,j)
    if not cnt:
        break
    ans += 1

print(ans)