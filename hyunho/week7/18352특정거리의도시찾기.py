import sys
from collections import deque
input = lambda : sys.stdin.readline()

N, M, K, X = map(int, input().split())
arr = [[] for _ in range(N + 1)]
distance = [-1] * (N + 1)
distance[X] = 0

for _ in range(M):
    a, b = map(int,input().split())
    arr[a].append(b)



q = deque([X])
while q:
    now = q.popleft()
    for next_node in arr[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)

for i in range(N+1):
    if distance[i] == K:
        print(i)
if K not in distance:
    print(-1)