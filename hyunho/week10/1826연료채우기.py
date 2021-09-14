import heapq
import sys

n = int(input())
station = [list(map(int, input().split())) for _ in range(n)]
pos = []

station = sorted(station, key = lambda x : -x[0])
# print(station)

destination, now = map(int, input().split())
used = 0

while now < destination:
    while station and station[-1][0] <= now:
        heapq.heappush(pos, -station[-1][1])
        station.pop()

    if not pos:
        print(-1)
        sys.exit(0)

    now -= heapq.heappop(pos)
    used += 1

print(used)

