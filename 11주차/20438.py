N, K = map(int, input().split())
A = list(map(int, input().split()))

res = 0
sm = 0 # sum of [0, now]
sum_counts = {0: 1}
for now in A:
    sm += now
    if sm - K in sum_counts:
        res += sum_counts[sm - K]
    sum_counts[sm] = sum_counts.get(sm, 0) + 1
print(res)