#1707 이분탐색



import sys
input =sys.stdin.readline
from collections import deque
N = int(input().rstrip())


def bfs(a):
    arr.append(a)
    visited[a] = 1
    while arr:
        node = arr.popleft()
        for i in range(len(lines[node])):
            if visited[lines[node][i]] == 0:
                visited[lines[node][i]] = -1 * visited[node]
                arr.append(lines[node][i])
            if visited[lines[node][i]] == visited[node]:
                return 0
    return 1



for _ in range(N):
    v , e = map(int,input().rstrip().split())
    lines = [ [] for _ in range(v+1)]
    for _ in range(e):
        x,y = map(int,input().rstrip().split())
        lines[x].append(y)
        lines[y].append(x)
    visited = [ 0 for _ in range(v+1)]
    arr = deque()
    ans = 1
    for i in range(v):
        if visited[i] == 0:
            ans = bfs(i)
            if ans == 0:
                break
    if ans == 1:
        print("YES")
    else:
         print("NO")

