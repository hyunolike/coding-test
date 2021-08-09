import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
tile = []

def upper_bound(lst, n):
    start = 0
    end = len(lst)

    while start < end:
        mid = start + (end-start) // 2
        if lst[mid] > n:
            end = mid
        else:
            start = mid + 1
    return end
for i in range(N):
    t = upper_bound(B, A[i])

    if t <= i:
        tile.append(0)
    else:
        tile.append(t-i-1)
print(*tile)
