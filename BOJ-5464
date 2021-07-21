# 주차장

from collections import deque
# 0번째부터 삭제를해야되는 방식인거같으면 무조건 deque활용
# 그이유 : 리스트큐 - pop,insert = O(N)
# 디큐 : pop,insert = O(1)
# 큐 클래스 = pop,insert = O(1)
N,M = map(int,input().split())
place = []  #자리비용을위한 리스트
cost = []  #무게당 비용을위한 리스트
order = deque()  # 전체주문을 받은 디큐
wait = deque()  # 자리가 꽉찼을때 쓰는 스페어 디큐
que = deque(0 for _ in range(N))  # 자리에 차가있는지 없는지를 판뱔해주는 디큐
ans = 0 # 최종 비용을 나타내는 결과값

for i in range(N):
    place.append(int(input().strip()))

for j in range(M):
    cost.append(int(input().strip()))

for p in range(M*2):
    order.append(int(input().strip()))
# 입력받기

while order: #주문을 다 받으면 종료하는 방식
    
#가장 중요한것 1 : 주문이 차를 넣는건지 빼는 건지 인식 
#넣을때는 = 자리표시   뺄때는 =값계산 / 자리 표시
#중요한것 2 : 넣을때 =자리가 다찼을때는 wait 큐에 넣어주기
#    뺄때 = 자리가 비어있을때 바로 차를 넣어주기(사실 언제넣는거는 상관없는듯)

    if order[0] >0:
        if 0 not in que:
            wait.append(order.popleft())
            continue
        else:
            if wait:
                k = list(filter(lambda x: que[x]==0, range(len(que))))
                que[k[0]] = wait.popleft()           
            else:
                 k = list(filter(lambda x: que[x]==0, range(len(que))))
                 que[k[0]] = order.popleft()
        
    elif order[0] < 0:
        if 0 in que and wait:
            k = list(filter(lambda x: que[x]==0, range(len(que))))
            que[k[0]] = wait.popleft()        
        a = abs(order.popleft())
        b = que.index(a)
        ans = ans + cost[a-1]*place[b]
        que[b] = 0

print(ans)
