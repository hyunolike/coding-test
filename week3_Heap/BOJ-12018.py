#12018 yonsei toto

#문제 풀이 : 1.조건세부화  2. 마일리지,수강원하는 학생수 , 최대 수용가능인원수 고려
#  3.최소값을 추구하기 때문에 minheap 사용 ->이때 그리디 방식으로 차근차근접근


import sys
input = lambda:sys.stdin.readline().strip()
import heapq

Min = []
ans = 0

N,M = map(int,input().split())

for i in range(N):
    
    person_apply , class_max= map(int,input().split())
    arr = list(map(int,input().split()))
    
    
    if class_max > person_apply:
        if M >0:
            M = M -1
            ans = ans+1
        else:
            continue
    else:
        heapq.heapify(arr)
        for i in range(abs(class_max-person_apply)):
            heapq.heappop(arr)
        heapq.heappush(Min,heapq.heappop(arr))
        

while Min:
    temp = heapq.heappop(Min)
    if M >= temp:
        ans += 1
        M -= temp
    else:
        break

print(ans)