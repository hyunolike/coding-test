import heapq
import sys

input = lambda : sys.stdin.readline()

n = int(input())
heap = []

for _ in range(n):
    # print(heap)
    num = int(input())

    if num != 0:
        heapq.heappush(heap, num)

    elif num == 0 and heap:
        print(heapq.heappop(heap))
    else:
        print(0)