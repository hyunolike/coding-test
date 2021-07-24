import heapq
import sys

input = lambda : sys.stdin.readline()

n = int(input())

cards = []
cards_sum = []
result = 0

for _ in range(n):
    heapq.heappush(cards, int(input()))

while cards:
    if len(cards) == 1:
        break
    x = heapq.heappop(cards)
    y = heapq.heappop(cards)
    heapq.heappush(cards_sum, x+y)
    heapq.heappush(cards, x+y)

print(sum(cards_sum))