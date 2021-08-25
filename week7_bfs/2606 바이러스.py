from collections import deque

def BFS(start):
    Q=deque([start])
    visited[start]=True

    while Q:
        node = Q.popleft()
        for next in graph[node]:
            if not visited[next]:
                visited[next] = True
                Q.append(next)
    print(visited.count(True)-1)

n = int(input())
m = int(input())
graph = [[] for _ in range(n)]
visited = [False]*n

for _ in range(m):
    a, b = map(int,input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

BFS(0)