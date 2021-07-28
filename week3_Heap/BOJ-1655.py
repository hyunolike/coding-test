import heapq
import sys
input = sys.stdin.readl
N = int(input().rstrip())

left = []
right = []

for i in range(N):
    num = int(input().rstrip())
    if i % 2:
        heapq.heappush(right, num)
    else:
        heapq.heappush(left,(-num,num))
    
    if right and left[0][1] > right[0]:
        temp1 = heapq.heappop(left)[1]
        temp2 = heapq.heappop(right)
        heapq.heappush(right, temp1)
        heapq.heappush(left, (-temp2,temp2))

   
    print(left[0][1])
