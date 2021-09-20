import sys

n, k, b = map(int,sys.stdin.readline().split())

light = [int(sys.stdin.readline()) for _ in range(b)]

arr = [0]*(n+1)

for i in light:
    arr[i] = 1

for i in range(1,len(arr)):
    arr[i] = arr[i-1]+arr[i]
Min = b

for i in range(k,len(arr)):
    Min = min (Min, arr[i]- arr[i-k])
print(Min)

