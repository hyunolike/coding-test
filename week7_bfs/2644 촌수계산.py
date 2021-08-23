from collections import deque

def bfs(v, target):
    count = 0
    Q = deque([[v, count]])
    while Q:
        node, cnt = Q.popleft()
        if node==target:
            return count
        
        if not visited[node]:
            count += 1
            visited[node] = True
            for next in graph[v]:
                if not visited[next]:
                    Q.append([next, count])
    return -1

n = int(input())
s, e = map(int, input().split())
m = int(input())
graph = [[]*(n+1) for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph:
    print(g)

print(bfs(s, e))