#311 : https://programmers.co.kr/learn/courses/30/lessons/42891
food_times=list(map(int, input().split()))
k=int(input())
sec, flag = 0, True
length=len(food_times)

while sec<k:
    food_index=sec%length
    sec+=1
    if food_times[food_index]:
        food_times[food_index]-=1
        print(food_times)
    elif not food_times[food_index]:
        while not food_times[food_index]:
            food_index=(food_index+1)%length
        food_times[food_index]-=1

if not sum(food_times):
    print(-1)
else:
    food_index=(food_index+1)%length
    while not food_times[food_index]:
        food_index=(food_index+1)%length

# another solution
import heapq

def solution(food_times,k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times)<=k:
        return -1
    
    # 시간이 작은 음식부터 빼야 하므로 우선순위 큐를 이용
    q=[]
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i+1))
    
    sum_value=0 # 먹기 위해 사용한 시간
    previous=0 # 직전에 다 먹은 음식 시간

    length = len(food_times) # 남은 음식의 개수

    # sum_value + (현재의 음식 시간 - 이전 음식 시간)*현재 음식 개수와 k 비교
    while sum_value+((q[0][0]-previous)*length) <= k:
        now=heapq.heappop(q)[0]
        sum_value+=(now-previous)*length
        length-=1 # 다 먹은 음식 제외
        previous=now # 이전 음식 시간 재설정
        
    
    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    result = sorted(q, key=lambda x:x[1]) # 음식의 번호 기준 정렬
    return result[(k-sum_value)%length][1]
