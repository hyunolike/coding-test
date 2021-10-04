import sys
input = sys.stdin.readline
from collections import deque

n, d, k, c = map(int, input().split())
susi = list(int(input()) for _ in range(n))
q = deque()
answer = 0
cnt = 0

for i in range(n+k):
    idx = i%n
    if len(q) == k:
        tmp = q.popleft()
        if tmp not in q:
            cnt -= 1
        if susi[idx] in q:
            q.append(susi[idx])
        else:
            q.append(susi[idx])
            cnt += 1
    elif len(q) < k:
        if susi[idx] in q:
            q.append(susi[idx])
        else:
            q.append(susi[idx])
            cnt += 1
    if len(q)==k and c not in q:
        answer = max(answer, cnt+1)
    else:
        answer = max(answer, cnt)
print(answer)