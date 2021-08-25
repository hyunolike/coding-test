from collections import deque

def BFS(start):
    Q=deque([start])
    visited=[-1]*n
    visited[start]=0

    while Q:
        node = Q.popleft()
        for next in graph[node]:
            if visited[next]==-1:
                visited[next]=visited[node]+1
                Q.append(next)
    
    for i in range(n):
        if visited[i]==k:
            answer.append(i+1)

n,m,k,x = map(int,input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
answer = []
BFS(x-1)
if not answer:
    print(-1)
else:
    for a in answer:
        print(a)