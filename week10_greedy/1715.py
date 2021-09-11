import sys
from queue import PriorityQueue
que = PriorityQueue()
n = int(sys.stdin.readline())

for _ in range(n):
    que.put(int(sys.stdin.readline()))

num = 0

while True:
    if que.qsize() == 1:
        break
    first = que.get()
    second = que.get()
    num += (first+second)
    que.put(first+second)
print(num)
