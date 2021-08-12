from collections import deque

N, M, V = map(int, input().split())

graph = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    m1, m2 = map(int, input().split())
    graph[m1][m2] = graph[m2][m1] = 1

def bfs(start_v):
    discoverd = [start_v]
    queue = deque([start_v])

    while queue:
        v = queue.popleft()
        for w in range(len(graph[start_v])):
            if graph[v][w] == 1 and (w not in discoverd):
                discoverd.append(w)
                queue.append(w)
    return discoverd

def dfs(start_v, discovered = []):
    discovered.append(start_v)
    for w in range(len(graph[start_v])):
        if graph[start_v][w] == 1 and (w not in discovered):
            discovered = dfs(w, discovered)
    return discovered

print(*dfs(V))
print(*bfs(V))