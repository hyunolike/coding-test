from bisect import bisect_left

N = int(input())
arr = list(map(int, input().split()))
result = []

for i in arr:
    k = bisect_left(result, i)
    if len(result) <= k:
        result.append(i)
    else: 
        result[k] = i

print(len(result))