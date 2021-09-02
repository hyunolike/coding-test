import sys
import collections
h, w = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))

idx = 0

count = 0

stack = collections.deque([])

while idx < w:
    stack.append(arr[idx])
    idx += 1
    while idx < w and stack:
        compare = stack.popleft()
        if compare <= arr[idx]:
            value = min(compare,arr[idx])
            while stack:
                count += (value - stack.pop())
        else:
            stack.appendleft(compare)
            stack.append(arr[idx])
            idx+=1

while stack:
    compare = stack.pop()
    while stack:
        possible = stack.pop()
        if possible < compare:
         
            count += (compare - possible)
        else:

            stack.append(possible)
            break
print(count)