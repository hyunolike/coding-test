from collections import deque

n,k = map(int, input().split())
answer = deque()
queue = deque(i for i in range(1, n+1))
cnt = 0
while queue:
    cnt += 1
    if cnt == k:
        answer.append(queue.popleft())
        cnt = 0
    else:
        queue.append(queue.popleft())

print("<", ", ".join(str(i) for i in answer), ">", sep='')