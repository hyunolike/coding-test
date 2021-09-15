import heapq
import sys
input = sys.stdin.readline

n = int(input())
data = list(int(input().strip()) for _ in range(n))
total = 0
heapq.heapify(data)
while len(data) != 1:
    a = heapq.heappop(data)
    b = heapq.heappop(data)
    c = a+b
    heapq.heappush(data,c)
    total += c
print(total)