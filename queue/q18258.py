from sys import stdin
from collections import deque

n = int(stdin.readline())
q = deque()
result = []
for _ in range(n):
    order = list(stdin.readline().rstrip().split())

    if order[0] == 'push':
        q.append(order[1])
    elif order[0] == 'pop':
        result.append(q.popleft()) if q else result.append(-1)
    elif order[0] == 'size':
        result.append(len(q))
    elif order[0] == 'empty':
        result.append(0) if q else result.append(1)
    elif order[0] == 'front':
        result.append(q[0]) if q else result.append(-1)
    else:
        result.append(q[-1]) if q else result.append(-1)

print('\n'.join(map(str, result)))
