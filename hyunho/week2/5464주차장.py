# 테스트케이스 2개 모두 실행이 되지만...
# 제출 시 런타임에러 발생 ㅠ,ㅠ 

from collections import deque

n, m = map(int, input().split())

n_list = deque() # 주차 공간 리스트
m_list = deque() # 차량 무게 리스트

sum_price = 0 # 총 수입
car_in = [] # 주차된 차량 리스트
car_out = deque()
car_list = deque()

n_list = [int(input()) for _ in range(n)]
m_list = [int(input()) for _ in range(m)]
number = 0

while number < m*2-1: # 해당 정수들을 입출입 만큼 반복 진행
    car_num = int(input()) # 양수, 음수 입력
    number += 1

    if len(car_in) < n and car_num > 0: # 주차 공간 만큼, 양수 일때

        if car_in.count(0) == 1: # 리스트 0 1개 존재하면 해당 0에 차량 주차를 해준다.
            index_0 = car_in.index(0)
            car_in[index_0] = m_list[car_num-1]
            sum_price += n_list[index_0] * m_list[car_num - 1]

        elif car_in.count(0) == 0: # 0이 없으면 뒤에 순차적으로 주차 된다.

            car_in.append(m_list[car_num-1])
            index_car = car_in.index(m_list[car_num-1])
            sum_price += n_list[index_car] * m_list[car_num-1]

        elif car_in.count(0) > 1:
            for i in car_in:
                if i == 0:
                    i = m_list[car_num-1]
                    sum_price += n_list[car_in.index(i)] * m_list[car_num-1]
                else:
                    continue

    elif car_num < 0: # 음수 일 경우, 나가는 차량
        abs_num = abs(car_num)
        index_num = car_in.index(m_list[abs_num-1])
        if len(car_out) > 0:
            car_in[index_num] = car_out.popleft()
            sum_price += n_list[index_num] * car_in[index_num]
        elif len(car_out) == 0:
            car_in[index_num] = 0

    elif car_num == 0:
        continue
    else:
        car_out.append(m_list[car_num-1])

print(sum_price)


