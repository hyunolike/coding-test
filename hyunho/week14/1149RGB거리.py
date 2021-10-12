import sys
input = lambda : sys.stdin.readline()

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
R, G, B = 0, 1, 2

dp = [[0]*3 for _ in range(N)]
dp[0][R], dp[0][G], dp[0][B] = arr[0][R], arr[0][G], arr[0][B]

for i in range(1, N):
    dp[i][R] = min(dp[i-1][G], dp[i-1][B]) + arr[i][R]
    dp[i][G] = min(dp[i-1][R], dp[i-1][B]) + arr[i][G]
    dp[i][B] = min(dp[i-1][R], dp[i-1][G]) + arr[i][B]

print(min(dp[N-1]))
