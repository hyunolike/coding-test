import heapq
import sys

n = int(input())
heap = []
nums = [int(sys.stdin.readline().strip()) for _ in range(n)]

for num in nums:
    if num == 0 and not heap:
        print(0)
    elif num == 0 and heap:
        print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, num)
