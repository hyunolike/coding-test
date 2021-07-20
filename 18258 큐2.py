import sys
from collections import deque

n = int(input())
queue = deque()

for i in range(n):
    op = sys.stdin.readline().strip().split()
    if op[0]=='push':
        queue.append(op[1])
    elif op[0]=='pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif op[0]=='size':
        print(len(queue))
    elif op[0]=='empty':
        if queue:
            print(0)
        else:
            print(1)
    elif op[0]=='front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif op[0]=='back':
        if queue:
            print(queue[-1])
        else:
            print(-1)


