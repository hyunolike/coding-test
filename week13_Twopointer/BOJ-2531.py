"""

수) 2531 회전 초밥
투포인터
문제풀이 1:
"""

import sys

input = sys.stdin.readline

N, D, K, C = map(int, input().split())

arr = []

for _ in range(N):
    arr.append(int(input().rstrip()))

dish = [0] * (D + 1)
dish[C] = 1
sum = 1
total = 1


for index in arr[0:K:]:
    
    if dish[index] == 0:
        sum += 1
        total += 1
    dish[index] += 1

for i in range(N):
    st = arr[i % N]
  
    dish[st] -= 1

    if dish[st] == 0:
        sum -= 1

    end = arr[(i + K) % N]
   
    dish[end] += 1
   
    if dish[end] == 1:
        sum += 1

    total = max(total, sum)

print(total)
