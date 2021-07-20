# 개선되기 전 코드

from collections import deque
import sys

n = int(input())
arr = deque()
for i in range(1,n+1):
    arr.append(i)

for i in range(len(arr)):
    if len(arr) != 1:
        arr.popleft()
        arr.append(arr[0])
        del arr[0]
        # print(arr)
    elif len(arr) == 1:
        print(arr[0])
        break

# 개선 된 후 코드 deque.rotate() 사용

from collections import deque
import sys

n = int(input())
arr = deque([i for i in range(1, n+1)])

while len(arr) > 1:
    arr.popleft()
    arr.rotate(-1)

print(arr[0])