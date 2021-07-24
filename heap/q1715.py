import sys
import heapq as heap

input = sys.stdin.readline

n = int(input())
bundle = [int(input()) for _ in range(n)]
ans = 0

heap.heapify(bundle)

while len(bundle) > 1:
    sum_val = heap.heappop(bundle) + heap.heappop(bundle)
    heap.heappush(bundle, sum_val)
    ans += sum_val

print(ans)

# 개선: heapify() 대신, heappush()로
