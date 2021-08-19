import sys
import collections

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

arr = [list(map(int,sys.stdin.readline().split())) for _ in range(m)]
graph = dict()
visited = dict()
for i in arr:
    try:
        graph[i[0]].add(i[1])
    except:
        graph[i[0]] = {i[1]}
        visited[i[0]] = True
    try:
        graph[i[1]].add(i[0])
    except:
        graph[i[1]] = {i[0]}
        visited[i[1]] = True
stack = collections.deque([1])
visited[1] = False
count = 0
while(len(stack)):
    this_turn = stack.pop()
    for i in graph[this_turn]:
        if visited[i]:
            count+=1
            stack.append(i)
            visited[i] = False
#
print(count)
