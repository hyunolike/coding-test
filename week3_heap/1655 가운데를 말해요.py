import sys
import heapq

n = int(input())
data = list(int(sys.stdin.readline().strip()) for _ in range(n))
left = []
right = []

for num in data:
    if len(left) == len(right):
        heapq.heappush(left, (-num, num))
    else:
        heapq.heappush(right, (num, num))
    
    if left and right and left[0][1] > right[0][1]:
        l = heapq.heappop(left)[1]
        r = heapq.heappop(right)[1]
        heapq.heappush(left, (-r, r))
        heapq.heappush(right, (l, l))
    print(left[0][1])