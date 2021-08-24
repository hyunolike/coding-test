#18352 특정거리의 도시찾기

"""
문제풀이 1: 전형적인 bfs 느낌 잘알아두기
"""
import sys
input = sys.stdin.readline
from collections import deque

N,M,K,X = map(int,input().rstrip().split())
road = [[] for _ in range(N+1)]
visited = [-1] *(N+1)
cnt =0

for _ in range(M):
    x , y =map(int,input().rstrip().split())
    road[x].append(y)


def bfs(x):
    arr = deque()
    arr.append(x)
    visited[x] = 0

    while arr:
        x = arr.popleft()

        for i in road[x]:
            if visited[i]== -1:
                arr.append(i)
                visited[i] = visited[x] + 1
bfs(X)
for j in range(N+1):
    if visited[j] == K:
        print(j)
        


if K not in visited:
    print(-1)


