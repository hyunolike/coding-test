#금) 11000 강의실배정

#그리디 사용  -> 1. 종료시간 > 시작시간 ->큐 삽입 // 2.종료시간 < 시작시간  팝 -> 삽입
#이 유형은 강의실배정,회의시간 배정, 시간표, 시간관련 그리디 알고리즘 사용할때 자주쓰임
# 각 문제별로 세부사항 파악하는게 포인트

import sys
input = lambda:sys.stdin.readline().strip()
import heapq

arr = []

N = int(input().strip())
for i in range(N):
    arr.append(list(map(int,input().split())))   
arr.sort()

ans = []
heapq.heappush(ans,arr[0][1])

for i in range(1,N):


    if ans[0] > arr[i][0] :
        heapq.heappush(ans,arr[i][1])
    else:
        heapq.heappop(ans)
        heapq.heappush(ans,arr[i][1])


print(len(ans))