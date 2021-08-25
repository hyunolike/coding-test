import sys
import collections
from itertools import combinations
import copy
def dfs(x,y):
    graph[x][y] = 2
    
    for i in range(4):
        row = x + dx[i]
        col = y + dy[i]
        if 0 <= row < n and 0 <= col < m and graph[row][col]==0:
            dfs(row,col)
        
n, m = map(int,sys.stdin.readline().split())

arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]
safe = 0
result =0
walls = []
q = collections.deque([])
virus = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            walls.append([i,j])
           
        elif arr[i][j] == 2 :
            virus.append([i,j])
comb = combinations(walls,3)

for k in comb:
    graph = copy.deepcopy(arr)
    
    graph[k[0][0]][k[0][1]] = 1
    graph[k[1][0]][k[1][1]] = 1
    graph[k[2][0]][k[2][1]] = 1
    safe = 0
    for i in virus:
        dfs(i[0],i[1])
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                safe+=1
    result = max(result,safe)
print(result)