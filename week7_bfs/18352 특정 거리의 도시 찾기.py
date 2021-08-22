import sys
input = sys.stdin.readline

from collections import deque

n,m,k,x = map(int, input().split())

graph = [[] for _ in range(n+1)]
distance = [-1]*(n+1)
distance[x] = 0

for _ in range(m):
    a,b = list(map(int, input().split()))
    graph[a].append(b)

Q = deque([x])
while Q:
    now = Q.popleft()
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now]+1
            Q.append(next_node)

for i in range(n+1):
    if distance[i]==k:
        print(i)
if k not in distance:
    print(-1)