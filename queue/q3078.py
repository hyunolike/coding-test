import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
ans = 0
names = deque(deque() for _ in range(19))

for rank in range(n):
    length = len(input().rstrip()) - 2

    while names[length]:
        base = names[length][0]
        if rank - base <= k:  # 비교대상과 기준이 k이내라면
            ans += len(names[length])  # 큐의 맨끝도 포함되므로, 그 전원소는 모두 포함
            break
        else:
            names[length].popleft()
    names[length].append(rank)

print(ans)

# sliding window
