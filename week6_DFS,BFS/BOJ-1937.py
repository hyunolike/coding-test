#1937 욕심쟁이 판다

"""
dfs  문제
문제풀이1: dp + dfs 문제
포인트 : 1. dp 구현을 위한 return 은 무슨 생각으로 구현을 해야하나?
2. dfs with dp 에서는 Recursion 구현을 어떻게 진행해야하나?

이거2개를 알고하는게 point 
+전문제인 내리막길과 비슷함

"""
import sys
input =sys.stdin.readline

N = int(input().rstrip())
dp = [[0]*N for _ in range(N)]
dx,dy = [0,0,1,-1],[1,-1,0,0]
arr = [list(map(int,input().rstrip().split()))for _ in range(N)]
ans = []

def dfs(x,y):
    print(dp,x,y)
    if dp[x][y] != 0:
        return dp[x][y]
    dp[x][y] = 1
    for i in range(4):
        nx, ny = x + dx[i] , y + dy[i]
        if 0 <= nx < N and 0 <=ny < N:
            if arr[x][y] < arr[nx][ny]:
                dp[x][y] = max(dp[x][y],dfs(nx,ny)+1)
    return dp[x][y]
        
    
for i in range(N):
    for j in range(N):
        ans.append(dfs(i,j))
        print(ans)
        
        
print(max(ans))