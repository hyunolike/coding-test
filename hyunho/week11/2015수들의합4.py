from collections import defaultdict
from itertools import accumulate

n, k = map(int, input().split())
nums = list(map(int, input().split()))
p_sum = list(accumulate(nums))
# print(p_sum)
s = 0


ans = 0
dic = defaultdict(int)
dic[0] = 1
for j in range(n):
    if dic[p_sum[j] - k] > 0:
        ans += dic[p_sum[j] - k]
    dic[p_sum[j]] += 1
print(ans)