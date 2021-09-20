#21758 꿀 따기


n = int(input())
honey = list(map(int, input().split()))
dp = [0]*n
result = 0
for i in range(n):
  result += honey[i] 
  dp[i] = result
case1, case2, case3= 0, 0, 0
for start2 in range(1, n-1):
  result1 = (dp[start2] - dp[0]) + (dp[n-2] - dp[start2 - 1])
  
  result2 = dp[start2 - 1] + dp[n-2] - honey[start2]
  
  result3 = (dp[n-1] - dp[0]) + (dp[n-1] - dp[start2]) - honey[start2]

  if case1 < result1 : case1 = result1
  if case2 < result2 : case2 = result2
  if case3 < result3 : case3 = result3
print(max(case1, case2, case3))