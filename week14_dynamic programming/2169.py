import sys

n, m = map(int,sys.stdin.readline().split())

arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

num = 0

dp = [[0]]

for i in range(m):
    dp[0].append(dp[0][i]+arr[0][i])
dp[0].append(0)

for i in range(1,n):
    dp.append([])
    for _ in range(m+2):
        dp[i].append(0)


for i in range(1,n):
    dp[i][0], dp[i][-1] = dp[i-1][1], dp[i-1][-2]
    templ = [0]*(m+2)
    tempr = [0]*(m+2)
    templ[0], tempr[0], tempr[-1], templ[-1] = dp[i-1][1], dp[i-1][1], dp[i-1][-2],dp[i-1][-2]
   
    for j in range(1,m+1):
        templ[j] = max(dp[i-1][j], templ[j-1]) + arr[i][j-1]
        tempr[m+1-j] = max(dp[i-1][m+1-j], tempr[m+2-j]) + arr[i][m-j]
    
    for j in range(1,m+1):
        dp[i][j] = max(templ[j],tempr[j])

print(dp[-1][-2])