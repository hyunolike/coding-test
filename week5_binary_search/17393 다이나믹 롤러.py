import sys

n = int(input())
ink = list(map(int, sys.stdin.readline().split()))
vis = list(map(int, sys.stdin.readline().split()))
answer = []

for i in range(n):
    pos = ink[i]
    l, r = i+1, n-1
    res = i

    while l <= r:
        mid = (l+r)//2
        if pos < vis[mid]:
            r = mid-1
        else:
            l = mid+1
            res = mid
    answer.append(str(res-(i+1)+1))
print(' '.join(answer))