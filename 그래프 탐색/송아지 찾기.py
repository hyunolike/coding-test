from collections import deque

s,e=map(int, input().split())
MAX=10000
visited=[0]*(MAX+1)
dist=[0]*(MAX+1)
visited[s]=1
q=deque()
q.append(s)

while q:
    now=q.popleft()
    if now==e:
        break
    for next in (now-1, now+1, now+5):
        if 1<=next<=MAX and not visited[next]:
            q.append(next)
            visited[next]=1
            dist[next]=dist[now]+1

print(dist[e])