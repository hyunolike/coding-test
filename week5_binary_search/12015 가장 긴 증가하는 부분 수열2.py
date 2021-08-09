import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
lis = []
ans = 0

for num in a:
    if not lis:
        lis.append(num)
        ans += 1
        continue
    if lis[-1] < num:
        lis.append(num)
        ans += 1
    else:
        index = bisect_left(lis, num)
        lis[index] = num
print(lis)
print(ans)