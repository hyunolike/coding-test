import sys
import collections
from functools import reduce
def row(arr):
    mx = 0
    for i in range(len(arr)):
        this_turn_dict = collections.Counter(arr[i])
        del this_turn_dict[0]
        items = list(this_turn_dict.items())
        items.sort(key = lambda x : (x[1],x[0]))
        if len(items) > 50:
            items = items[:50]
        arr[i] = reduce(lambda x, y : list(x) + list(y), items[1:], list(items[0]))
        mx = max(mx, len(arr[i]))
    for i in range(len(arr)):
        if len(arr[i]) < mx:
            arr[i].extend([0]* (mx-len(arr[i])))

r, c, k = map(int,sys.stdin.readline().split())

arr = [list(map(int,sys.stdin.readline().split())) for _ in range(3)]

r, c= r-1, c-1

count = 0

while count<100:
    if r < len(arr) and c < len(arr[0]):
        if arr[r][c] == k:
            print(count)
            sys.exit()
    if len(arr) >= len(arr[0]):
        row(arr)
    else:
        arr = list(map(list,zip(*arr)))
        row(arr)
        arr = list(map(list,zip(*arr)))
    count += 1
print(-1)
sys.exit()