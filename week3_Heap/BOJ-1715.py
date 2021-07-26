#  / 1715 카드 정렬하기

#문제풀이 :  1.힙사용해서 최소값 항상 0 번째 오게 설정
#2 따라서 최소값을 찾아서 더해주면 구현완료

import sys
input = lambda:sys.stdin.readline().strip()
import heapq

ans =0
temp =0
arr=[]
N = int(input().rstrip())
for i in range(N):
    arr.append(int(input().rstrip()))


heapq.heapify(arr)


if len(arr) == 1:
    print(0)
else:
    while(len(arr) > 1):
        a = heapq.heappop(arr) 
        b =heapq.heappop(arr)
        ans +=  a + b
        heapq.heappush(arr,a+b)
    print(ans)


