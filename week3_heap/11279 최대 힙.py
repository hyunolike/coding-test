import heapq
import sys

n = int(input())
data = list(int(sys.stdin.readline().strip()) for _ in range(n))
heap = []

for num in data:
    if num == 0 and heap:
        print(-1 * heapq.heappop(heap))
    elif num == 0 and not heap:
        print(0)
    else:
        heapq.heappush(heap, -num)

