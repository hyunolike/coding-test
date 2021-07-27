import sys
import heapq

n = int(input())
heap = []
for i in range(n):
    data = list(map(int, sys.stdin.readline().split()))
    for num in data:
        if len(heap) == n and heap[0] < num:
            heapq.heappop(heap)
            heapq.heappush(heap, num)
        elif len(heap) < n:
            heapq.heappush(heap, num)

print(heapq.heappop(heap))