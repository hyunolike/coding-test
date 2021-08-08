# 2005 나무자르기

#문제풀이: 1.전형적인 이진탐색
# 2. pypy3로 해야 시간초과가 안남 그이유 = 재귀가 많을경우 pypy3 < python 3이다

import sys
input = sys.stdin.readline
N,M =map(int,input().rstrip().split())
arr = list(map(int,input().rstrip().split()))


start = 0
end = max(arr)


while start <= end:

    mid = (start+end) //2
    count = 0
    for i in range(N):
        if arr[i]>mid:
            count += arr[i] - mid
    

    if count >= M:
        temp = mid
        start = mid+1
    else:
        end = mid-1

print(temp)
