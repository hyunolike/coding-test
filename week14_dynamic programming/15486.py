import sys

n = int(sys.stdin.readline())

arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]


dp = [0]*(n+2)
max_value = 0
for i in range(len(arr)):
    today = i+1
    day_long = arr[i][0]
    money = arr[i][1]
    max_value = max(max_value, dp[i+1])
    if today + day_long < n+2:
        dp[today+day_long] = max(max_value + money, dp[today+day_long])
    
max_value = max(max_value,dp[-1])
print(max_value)