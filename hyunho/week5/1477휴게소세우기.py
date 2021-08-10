import sys

input = lambda : sys.stdin.readline()
n, m, l = map(int, input().split())
store = list(map(int, input().split()))
store.append(0)
store.append(l)
store.sort()

left, right = 1, l

while left <= right:
    mid = left + (right-left) // 2

    new_store = 0
    for i in range(1, len(store)):
        dist = store[i] - store[i-1] - 1
        new_store += dist // mid
    if new_store > m:
        left = mid + 1
    else:
        result = mid
        right = mid - 1
print(result)