import sys
from collections import deque


def first(place, price, order):
    answer = 0
    queue = deque()
    order = deque(order)
    onoff = [0 for i in range(len(place))]

    while order:
        if order[0] > 0:
            queue.append(order.popleft())
            if 0 not in onoff:
                pass
            else:
                psPlace = list(filter(lambda x: onoff[x]==0, range(len(onoff))))
                onoff[psPlace[0]] = queue.popleft()
        else:
            n = abs(order.popleft())
            idx = onoff.index(n)
            answer += place[idx] * price[onoff[idx]-1]
            if queue:
                onoff[idx] = queue.popleft()
            else:
                onoff[idx] = 0
    print(answer)

n,m = map(int, input().split())
place = [int(sys.stdin.readline().strip()) for i in range(n)]
price = [int(sys.stdin.readline().strip()) for i in range(m)]
order = [int(sys.stdin.readline().strip()) for i in range(m*2)]
first(place, price, order)