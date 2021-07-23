#금) 1927 최소 힙 

#시간 줄이기 - > import sys/ readline
#그 이외에는 간단 minheap 사용
import sys
import heapq
input = lambda:sys.stdin.readline().strip()
ans = []

N = int(input().strip())

for i in range(N):
    A = int(input().strip())

    if A > 0:
        heapq.heappush(ans,A)
    elif A == 0:
        if ans:
            print(heapq.heappop(ans))
        else:
            print("0")