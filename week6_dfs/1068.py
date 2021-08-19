import sys
import collections
n = int(sys.stdin.readline())

arr = list(map(int,sys.stdin.readline().split()))

aim = int(sys.stdin.readline())
graph = dict()
result = 0
visited = dict()
for index, val in enumerate(arr):
    if val == -1:
        root = index
        continue
    try:
        graph[val].add(index)
    except:
        graph[val] = {index}
        visited[val] = True
    try :
        graph[index].add(val)
    except:
        graph[index] = {val}
        visited[index] = True


stack = collections.deque([root])
visited[root] = False
count = 0
if aim == root:
    print(0)
    sys.exit()
for i in graph[aim]:
    graph[i].remove(aim)
del(graph[aim])


while(len(stack)):
    this_turn = stack.pop()
    this_count = 0
    for i in graph[this_turn]:
        if visited[i]:
            this_count += 1
            visited[i] = False
            stack.append(i)
    if this_count == 0:
        result+=1
print(result)