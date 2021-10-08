#로봇 조종하기
import sys

n,m = map(int,sys.stdin.readline().split())
board =[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
dp = [[0]*m for _ in range(n)]
left=[[0]*m for _ in range(n)]
right=[[0]*m for _ in range(n)]
dp[0][0]= board[0][0]

# 맨 윗 줄 채우기 (무조건 -> 방향)
for i in range(1,m):
    dp[0][i] = dp[0][i-1]+board[0][i]

# 한 줄 씩 검사
for i in range(1,n):
    # 왼쪽 -> 오른쪽
    left[i][0] = dp[i-1][0] + board[i][0]
    for j in range(1,m):
        left[i][j] = max(left[i][j-1],dp[i-1][j]) + board[i][j]

    # 오른쪽 -> 왼쪽
    right[i][m-1] = dp[i-1][m-1] + board[i][m-1]
    for j in range(m-2,-1,-1):
        right[i][j] = max(right[i][j+1],dp[i-1][j]) + board[i][j]

    for j in range(m):
        dp[i][j] = max(left[i][j], right[i][j])
print(dp[n-1][m-1])