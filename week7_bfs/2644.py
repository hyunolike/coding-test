import sys
import collections
n = int(sys.stdin.readline())

aim1 , aim2 = map(int,sys.stdin.readline().split())

m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
visited = [1]* (n+1)
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(m)]

for i in arr:
    graph[i[0]].append(i[1])
    graph[i[1]].append(i[0])

stack = collections.deque([(aim1,0)])
flag = 1
while stack:
    number, count = stack.pop()
    if number == aim2:
        print(count)
        flag = 0
    for i in graph[number]:
        if visited[i]:
            visited[i] = 0
            stack.append((i,count+1))
if flag:
    print(-1)