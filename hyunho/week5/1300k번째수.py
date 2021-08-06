# k번째 요소에 들어있는 숫자가 무엇인가

import sys
input = lambda : sys.stdin.readline()

n = int(input())
k = int(input())

left, right = 1, k

while left <= right:
    mid = left + (right-left) // 2

    temp = 0 # mid값보다 작은 수들의 개수

    for i in range(1, n+1):
        temp += min(mid // i, n)


    if temp >= k:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1
print(answer)
