import sys
input = lambda : sys.stdin.readline()

n, k = map(int, input().split())
arr = list(map(int, input().split()))
dp = [1] * (n-1)

for i in range(n-1):
    cnt = 0
    for j in range(i, n-1):
        if arr[j] <= k:
            dp[i] += 1
        elif arr[j] > k:
            cnt += 1
            if cnt > 1:
                break
            dp[i] += 1
print(max(dp))
