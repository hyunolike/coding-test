import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
lis = []

for num in a:
    if not lis:
        lis.append(num)
        continue
    if lis[-1] < num:
        lis.append(num)    
    else:
        index = bisect_left(lis, num)
        lis[index] = num
print(len(lis))