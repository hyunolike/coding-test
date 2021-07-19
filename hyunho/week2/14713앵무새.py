# 시간 초과 발생 ㅠ,ㅠ
# 테스트케이스는 통과

from collections import deque
import copy

arr = deque()
num = int(input())
arr = [deque(input().split()) for _ in range(num)]
result = input().split()

for r in result:
    for i in range(num):
        for j in copy.deepcopy(arr[i]):
            if r in j:
                arr[i].popleft()

count = 0

for i in range(num):
    if not arr[i]:
        count += 1
    elif arr[i]:
        continue

if count == 3:
    print("Possible")
else:
    print("Impossible")