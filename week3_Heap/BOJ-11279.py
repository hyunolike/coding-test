#11279 최대힙

#문제풀이 : maxheap


import heapq
import sys
input = sys.stdin.readline
ans =[]

N = int(input().rstrip())

for i in range(N):
    A = int(input().rstrip())
    if A == 0:
        if ans:
            print(heapq.heappop(ans)[1])
        else:
            print(0)
    elif A>0:
        heapq.heappush(ans,(-A,A))
