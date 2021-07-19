from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
available, fee = n, 0

spaces = [int(stdin.readline()) for _ in range(n)]
weights = [int(stdin.readline()) for _ in range(m)]
cars = deque([int(stdin.readline()) for _ in range(2*m)])
lots = [0 for _ in range(n)]
queue = deque()

while cars:
    top = cars.popleft()
    if top > 0:  # in
        if available == 0:  # full
            queue.append(top)
            continue
        for i in range(n):  # 주차 성공
            if lots[i] == 0:
                lots[i] = top
                available -= 1
                break
    else:  # out
        idx = lots.index(top*-1)
        fee += weights[-1*top-1]*spaces[idx]
        available += 1
        lots[idx] = 0

        if queue:  # queue에 대기하는 차가 있으면 맨 앞으로 넣기
            cars.insert(0, queue.popleft())

print(fee)



