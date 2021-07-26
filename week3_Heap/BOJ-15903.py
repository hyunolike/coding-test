# 15903 카드 합체 놀이 

#문제풀이 :   minheap /treenode / root /의 이해

import sys
input = lambda:sys.stdin.readline().strip()
import heapq
a=0
ans = 0
arr = []
N,M = map(int,input().split())
arr = list(map(int,input().split()))

heapq.heapify(arr)

for i in range(M):
  
    a = heapq.heappop(arr) + heapq.heappop(arr)
    for j in range(2):
        heapq.heappush(arr,a)

for k in arr:
    ans = ans+k

print(ans)