#1520 내리막길

#문제풀이 1: dfs + visited로 돌릴시 시간초과 오류 발생
#2. 따라서 dp 개념 도입


import sys
input = sys.stdin.readline

N,M = map(int,input().rstrip().split())
dp = [[-1]* M for _ in range(N)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
arr = [list(map(int,input().rstrip().split())) for _ in range(N)]

def dfs(x,y):
#    print(x,y)
    if x== N-1 and y == M-1:
        return 1
        
    if dp[x][y] == -1:
        dp[x][y] = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]    
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] < arr[x][y]:
                    dp[x][y] += dfs(nx,ny)
    return dp[x][y]

print(dfs(0,0))
