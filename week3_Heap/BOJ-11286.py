#11286 최대힙 

#문제풀이 1.minheap사용 필수 라고 생각
#2. 힙안에서 음수양수를 구별하기는 매우 복잡하기때문에 양수,음수 큐따로 구현
#3 따로구현할때 음수의경우 maxheap로 해줘야 조건 완성가능
#4 나머지는 요구조건 채워주면 끝
import heapq
import sys
input = sys.stdin.readline
plus = []
minu =[]


N = int(input().rstrip())

for i in range(N):
    A = int(input().rstrip())
    if A > 0:
        heapq.heappush(plus,A)
    elif A < 0 :
        heapq.heappush(minu,(-A,A))
    else:
        if plus and not minu:
            print(heapq.heappop(plus))
        elif not plus and minu:
            print(heapq.heappop(minu)[1])
        elif not plus and not minu:
            print(0)
        else:
            temp1 = heapq.heappop(plus)
            temp2 = heapq.heappop(minu)[1]
            if abs(temp1) == abs(temp2):
                 print(temp2)
                 heapq.heappush(plus,temp1)
            elif abs(temp1) > abs(temp2):
                 print(temp2)
                 heapq.heappush(plus,temp1)
            elif abs(temp1) < abs(temp2):
                print(temp1)
                heapq.heappush(minu,(-temp2,temp2))