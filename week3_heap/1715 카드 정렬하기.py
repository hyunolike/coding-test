import heapq
import sys

n = int(input())
data = list(int(sys.stdin.readline().strip()) for _ in range(n))
result = 0
heapq.heapify(data)
while len(data) != 1:
    a = heapq.heappop(data)
    b = heapq.heappop(data)
    c = a+b
    heapq.heappush(data, c)
    result += c
print(result)
