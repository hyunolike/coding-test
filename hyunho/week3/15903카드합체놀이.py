import heapq
import sys

input = lambda : sys.stdin.readline()

n, m = map(int, input().split())
cards = list(map(int, input().split()))
heap = []

for card in cards:
   heapq.heappush(heap, card)

for _ in range(m):
    x = heapq.heappop(heap)
    y = heapq.heappop(heap)
    heapq.heappush(heap, x+y)
    heapq.heappush(heap, x+y)

print(sum(heap))