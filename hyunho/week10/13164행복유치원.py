n, k = map(int,input().split())
arr = list(map(int, input().split()))

dp = []
for i in range(n):
  dp.append(arr[i + 1] - arr[i])

dp.sort()
print(sum(dp[:n-k]))
