from itertools import combinations, permutations
from collections import deque
import copy

def BFS(a, b):
    Q=deque([[a, b]])

    while Q:
        x, y = Q.popleft()
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if not (0<=nx<n and 0<=ny<m):
                continue
            if tmp[nx][ny]==0:
                tmp[nx][ny]=2
                Q.append([nx, ny])
    return 0

def count_map():
    global answer
    cnt = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j]==0:
                cnt += 1
    if answer < cnt:
        answer = cnt

n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]
virus = []
answer = 0

for i in range(n):
    for j in range(m):
        if graph[i][j]==2:
            virus.append([i,j])

cases = []
for i in range(n):
    for j in range(m):
        cases.append((i, j))
c = combinations(cases, 3)

for walls in c:
    flag = False
    tmp = copy.deepcopy(graph)
    for x, y in walls:
        if tmp[x][y]==0:
            tmp[x][y]=1
        else:
            flag = True
            break
    if flag:
        continue
    else:
        for x, y in virus:
            BFS(x, y)
        count_map()

print(answer)
