#14241 슬라임합치기

#문제풀이 : 1.max heap 구현 2.조건 맞추기

#종료 조건 슬라임 1개 .

import heapq
import sys
input = sys.stdin.readline
ans = 0
slimes = []

N = int(input().rstrip())
slime = list(map(int, input().split()))

for j in slime:
    heapq.heappush(slimes,(-j,j))



while len(slimes) > 1:
    temp1 = heapq.heappop(slimes)[1]
    temp2 = heapq.heappop(slimes)[1]
    a = temp1 + temp2

    heapq.heappush(slimes,(-a,a))
    ans = ans + temp1*temp2
    
print(ans)