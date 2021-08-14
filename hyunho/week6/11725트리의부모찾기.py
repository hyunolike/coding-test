import sys
sys.setrecursionlimit(10**6)
input = lambda : sys.stdin.readline()

N = int(input())
tree = [[] for _ in range(N+1)]
visited = [False] * (N + 1)
dic = {}

for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(v):
    visited[v] = True
    for i in tree[v]:
        if not visited[i]:
            dic[i] = v
            dfs(i)

dfs(1)
for i in range(2, N+1):
    if i in dic:
        print(dic[i])
    else:
        break