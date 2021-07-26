import sys
import heapq as heap

input = sys.stdin.readline

n = int(input())
score = 0
slimes = list(map(int, input().split()))
for e in slimes:  # minheap으로
    e *= -1

heap.heapify(slimes)

while len(slimes) > 1:
    a, b = heap.heappop(slimes), heap.heappop(slimes)
    heap.heappush(slimes, a+b)
    score += (a*b)

print(score)

'''
maxheap사용 
'''