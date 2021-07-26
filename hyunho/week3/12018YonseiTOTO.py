import heapq
import sys

input = lambda : sys.stdin.readline()
ans = 0 # 결과
n, m = map(int, input().split())
temp = [] # 신청할 마일리지

for _ in range(n):
    p, l = map(int, input().split())
    mileages = list(map(int, input().split()))
    heapq.heapify(mileages)
    num = l-p
    # 수강인원 미달
    if num > 0:
        heapq.heappush(temp, 1)
    # 수강인원 미달이 아닌 경우
    else:
        for i in range(abs(num)): # 차이 만큼
            heapq.heappop(mileages) # 가장 작은 마일리지부터 빼주는거
        heapq.heappush(temp, heapq.heappop(mileages)) # 턱걸이 점수를 내가 신청할 마일리지에 넣는다.


while temp:
    mileage = heapq.heappop(temp)
    if m - mileage >= 0:
        ans += 1
        m -= mileage
    else:
        break

print(ans)