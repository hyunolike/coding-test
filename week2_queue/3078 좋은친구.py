from collections import deque
import sys

n, k = map(int, input().split())
answer = 0
cnt = [0]*21
queue = deque()

for i in range(n):
    length = len(sys.stdin.readline().strip())
    answer += cnt[length]
    if len(queue) >= k:
        cnt[queue.popleft()] -= 1
    cnt[length] += 1
    queue.append(length)

print(answer)
