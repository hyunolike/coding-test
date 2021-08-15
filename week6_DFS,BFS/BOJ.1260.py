#1260 DFS 와 BFS

#문제풀이 1: 가장 기본적인 dfs bfs 자료구조 with python

import sys
input = sys.stdin.readline

from collections import deque

N,M,V = map(int,input().rstrip().split())

arr= [[0]* (N+1) for _ in range(N+1)] #0 없으니까 N+1
visited = [False] * (N+1)

for i in range(M):
    a,b = map(int,input().rstrip().split())
    arr[a][b] = arr[b][a] = True #True = 있는지 없는지 판별위함
    
def dfs(x):
    if visited[x] ==False:
        visited[x] = True
        print(x,end=" ")
        for i in range(1,N+1):
            if arr[x][i]==True:
                dfs(i)  #재귀형태로 내려감

def bfs(x):
    queue = deque([x]) 
    visited[x] = False
    while queue:
        
        x = queue.popleft() #실행시간 단축
        print(x,end=" ")
        for i in range(1,N+1):
            if(visited[i] == True and arr[x][i] == True):
                visited[i] = False
                queue.append(i)  #큐형태로 자기 노드 다처리후 내려감
dfs(V)               
print()
bfs(V)