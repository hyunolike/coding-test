import sys

def dfs(loc,visited,start, length):
    global min_val
    if len(visited) == len(compare_set):
        if arr[loc][start] != 0:
            min_val = min (min_val, length + arr[loc][start])
            return
    can_visit = compare_set - visited
    for i in can_visit:
        if arr[loc][i] != 0:
            visited.add(i)
            dfs(i,visited, start, length+arr[loc][i])
            visited.remove(i)

n = int(sys.stdin.readline())

arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

min_val = 1000000*10

compare_set = set(range(n))

for i in range(n):
    dfs(i,{i},i,0)
print(min_val)