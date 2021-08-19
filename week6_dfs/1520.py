import sys
import collections


def dfs(x,y):
    
    if x == n-1 and y == m-1:
        return 1
    if confirm[x][y] != -1:
        return confirm[x][y]
    
    confirm[x][y] = 0 #나중에 다른 dfs에서 날 찾았을때 위에꺼에 안걸리게 함...
    for i in range(4):
        row = x + dx[i]
        col = y + dy[i]
        if 0 <= row <= n-1 and 0 <= col <= m-1 and arr[x][y] > arr[row][col]:
            confirm[x][y] += dfs(row,col)
    return confirm[x][y]
            
            


n, m = map(int,sys.stdin.readline().split())

arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
dx = [+1,0,-1,0]
dy = [0,-1,0,+1]



confirm = [[-1]*m for _ in range(n)]


print(dfs(0,0))
