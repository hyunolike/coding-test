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