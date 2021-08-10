import sys
input = lambda : sys.stdin.readline()
K, N = map(int, input().split())

arr = [int(input().rstrip()) for _ in range(K)]
start, end = 1, max(arr)

while start <= end:
    mid = start + (end-start) // 2
    lines = 0
    for i in arr:
        lines += i // mid
    if lines >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)