from sys import stdin
from collections import deque

tc = int(stdin.readline())
result = list()

for _ in range(tc):
    n, m = map(int, stdin.readline().split())
    priority = list(map(int, stdin.readline().split()))
    q = deque()
    idx = 0

    for i in range(n):
        if i == m:
            q.append((priority[i], True))
        else:
            q.append((priority[i], False))
    priority.sort()

    while True:
        out = q.popleft()
        if out[0] != priority[-1]:
            q.append(out)
        else:
            priority.pop()
            idx += 1
            if out[1]:
                break
    result.append(idx)

for ele in result:
    print(ele)
