import sys
import collections
n = int(sys.stdin.readline())

arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n-1)]
result =[]
for _ in range(n+1):
    result.append(0)
possible = [True]*n
graph = dict()

for i in arr:
    start , finish = i[0], i[1]
    try:
        graph[start].add(finish)
    except:
        graph[start]={finish}
    try:
        graph[finish].add(start)
    except:
        graph[finish] = {start}

stack = collections.deque([[1]])
possible[0] = False
while(len(stack)):
    this_turn = stack.pop()
    val = this_turn[0]
    for i in graph[val]:
        if possible[i-1]:
            stack.append([i])
            possible[i-1] = False
            result[i] = val
for i in range(2,n+1):
    print(result[i])
