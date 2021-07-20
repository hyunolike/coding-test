from sys import stdin
from collections import deque

n = int(stdin.readline())
q = deque(x for x in range(1, n+1))

while len(q) != 1:
    q.popleft()
    q.append(q.popleft())

print(q.pop())


# https://tooo1.tistory.com/88
# (n - 2^(n//2))*2