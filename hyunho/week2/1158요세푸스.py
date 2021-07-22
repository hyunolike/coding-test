from collections import deque
n, k = map(int, input().split())
queue = deque([i for i in range(1,n+1)])

result = []
while queue:
    queue.rotate(-k+1)
    result.append(str(queue.popleft()))

print(f'<{", ".join(result)}>')