import heapq
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
miles = []
ans = 0

for _ in range(n):
    p, l = map(int, input().split())
    s = list(map(int, input().split()))

    if l > p:
        miles.append(1)
    else:
        s.sort(reverse=True)
        while len(s) > l:
            s.pop()
        miles.append(s.pop())

miles.sort()
for e in miles:
    if m < e:
        break
    m -= e
    ans += 1

print(ans)

