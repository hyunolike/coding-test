import sys
import collections

n, m, k, x = map(int,sys.stdin.readline().split())


graph = [[] for _ in range(n+1)]
visited = [True]*(n+1)
for i in range(m):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    

stack = collections.deque([(x,0)])

distance = [-1] * (n+1)
result = set()
distance[x] = 0
while(len(stack)):
    loc, count = stack.popleft()
    if count == k:
        result.add(loc)
        continue
    elif count < k:
        for i in graph[loc]:
            if distance[i] == -1:
                distance[i] = count+1
                stack.append((i,count+1))
                
if len(result) == 0:
    print(-1)

else:
    result = list(result)
    result.sort()
    for t in result:
        print(t)