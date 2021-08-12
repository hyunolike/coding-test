from collections import deque

def dfs(v):
    visited[v] = 1
    print(v, end=' ')
    for i in range(1, n+1):
        if graph[v][i] == 1 and visited[i] ==0:
            dfs(i)

def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = 1

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in range(1, n+1):
            if graph[v][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i]=1

n, m, v = map(int, input().split())
graph = [[0]*(n+1) for i in range(n+1)]
visited = [0]*(n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

dfs(v)
visited = [0]*(n+1)
print()
bfs(v)