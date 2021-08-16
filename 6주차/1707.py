import sys
input=sys.stdin.readline

K=int(input())

def sol(graph):
    pass



for _ in range(K):
    V,E=map(int,input().split())
    graph=[[] for _ in range(V+1)]
    for _ in range(E):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    print(graph)

