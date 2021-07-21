from collections import deque
import sys

input = lambda : sys.stdin.readline()
num = int(input())
queue = deque()

for i in range(num):
    temp = list()
    temp = list(input().split())

    if temp[0] == "push":
        queue.append(temp[1])
    elif temp[0] == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif temp[0] == "size":
        print(len(queue))
    elif temp[0] == "empty":
        if len(queue) >= 1:
            print(0)
        else:
            print(1)
    elif temp[0] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif temp[0] == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)
