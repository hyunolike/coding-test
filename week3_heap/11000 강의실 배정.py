import heapq
import sys

n = int(input())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

sheap = []
theap = []
for d in data:
    heapq.heappush(sheap, (d[0], d[1]))

while sheap:
    lect = heapq.heappop(sheap)
    if not theap:
        heapq.heappush(theap, (lect[1], lect[0]))
    else:
        if theap[0][0] <= lect[0]:
            heapq.heappop(theap)
            heapq.heappush(theap, (lect[1], lect[0]))
        else:
            heapq.heappush(theap, (lect[1], lect[0]))

print(len(theap))
