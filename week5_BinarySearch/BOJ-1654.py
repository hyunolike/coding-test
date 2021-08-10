

#1654 랜선 자르기

import sys
input = sys.stdin.readline


k , n = map(int,input().rstrip().split())
arr = []
for _ in range(k):
    arr.append(int(input().rstrip()))

start ,end = 1, max(arr)
ans = 0

while start <= end:
    mid = (start+end) //2
    temp = sum([(i // mid)for i in arr])

    if temp >= n:
        ans = mid
        start = mid +1
    else:
        end = mid -1

print(ans)