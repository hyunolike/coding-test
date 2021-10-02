import sys

n, m = map(int,sys.stdin.readline().split())

arr = [int(sys.stdin.readline()) for _ in range(n)]

left = 0

right = 1

min_len =  2000000001

arr.sort()

while left < n-1 and right < n:
    if arr[right] - arr[left] >= m:
        min_len = min(min_len,arr[right]- arr[left])
        left += 1
    else:
        right += 1
print (min_len) 