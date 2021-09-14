from queue import PriorityQueue
import sys
input=sys.stdin.readline
N=int(input())
numbers=PriorityQueue()
for _ in range(N):
    numbers.put(int(input()))

temp=0

while numbers.qsize()!=1:
    a,b=numbers.get(),numbers.get()

    temp+=a+b

    numbers.put(a+b)



print(temp)


# import heapq
 
# n = int(input())
# q = list()
# for _ in range(n):
#     heapq.heappush(q, int((input())))
 
# if n == 1:
#     print(0)
#     exit()
 
# answer = 0
# while len(q) > 1:
#     val = heapq.heappop(q) + heapq.heappop(q)
#     answer += val
#     heapq.heappush(q, val)
 
# print(answer)
