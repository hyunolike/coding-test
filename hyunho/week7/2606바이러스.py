import sys
from collections import deque
input = lambda : sys.stdin.readline()

n = int(input())
m = int(input())
computers = [[0]*(n+1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    computers[a][b] = 1
    computers[b][a] = 1

visited = [0] * (n+1)
q = deque()
q.append(1)
visited[1] = 1
cnt = 0
while q:
    now = q.popleft()
    for i in range(1, n+1):
        if computers[now][i] == 1 and visited[i] == 0: # 연결되어있고 방문한 적이 없으면
            visited[i] = 1
            q.append(i)
            cnt += 1

print(cnt)