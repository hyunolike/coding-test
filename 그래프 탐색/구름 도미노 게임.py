from collections import deque

a,b,c=map(int, input().split())
graph=[[0]*a for _ in range(a)]
visited=[0]*a
q=deque()

for _ in range(b):
    x,y=map(int, input().split())
    graph[x-1][y-1]=1
for _ in range(c):
    start=int(input())
    q.append(start-1)
    visited[start-1]=1
    
    while q:
        node=q.popleft()
        
        for next_node in range(node+1, a):
            if graph[node][next_node] and not visited[next_node]:
                q.append(next_node)
                visited[next_node]=1

print(sum(visited))