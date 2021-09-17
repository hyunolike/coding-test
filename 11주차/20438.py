N, K = map(int, input().split())
numbers = list(map(int, input().split()))

res = 0
sum = 0 # sum of [0, now]
sum_counts = {0: 1}
for now in numbers:
    sum += now
    if sum - K in sum_counts:
        res += sum_counts[sum - K]
    sum_counts[sum] = sum_counts.get(sum, 0) + 1
print(res)