import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
circle = deque(str(x) for x in range(1, n+1))
result = []
flag = False

while circle:
    if flag:
        result.append(circle.popleft())
        flag = False
    else:
        for _ in range(k-1):
            circle.append(circle.popleft())
        flag = True

print('<', end='')
print(', '.join(result), end='')
print('>')
