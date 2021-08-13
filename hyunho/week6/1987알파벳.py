import sys

input = lambda : sys.stdin.readline()
r, c = map(int, input().split())
arr = [list(map(lambda x : ord(x) - 65, input().rstrip())) for _ in  range(r)]
alpha = [0] * 26

dx = [-1,1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, count):
  global ans
  ans = max(ans, count)
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < r and 0 <= ny < c and alpha[arr[nx][ny]] == 0:
      alpha[arr[nx][ny]] = 1
      dfs(nx, ny, count + 1)
      alpha[arr[nx][ny]] = 0

ans = 1
alpha[arr[0][0]] = 1
dfs(0, 0, 1)

print(ans)