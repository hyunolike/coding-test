import sys
sys.setrecursionlimit(10**9)

n = int(input())

Tree = [[] for _ in range(n+1)]
Parents = [0 for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int, sys.stdin.readline().split())
    Tree[a].append(b)
    Tree[b].append(a)

def DFS(start, tree, parents):
    for i in tree[start]:
        if parents[i]==0:
            parents[i] = start
            DFS(i, tree, parents)

DFS(1, Tree, Parents)

for i in range(2, n+1):
    print(Parents[i])