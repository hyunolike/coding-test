import sys
from collections import deque

input = sys.stdin.readline

n, t = map(int, input().split())
turns = deque(map(int, input().split()))
queue = list(deque() for _ in range(n+1))  # 이전에 사용하지 않은 카드가 있으면 저장
cards = set()  # 공용공간에 없는 숫자카드들
result = list()

while turns:
    turn = turns.popleft()
    # 내 큐에 연산카드가 있는 경우 vs. 없는 경우
    # card = [id, 연산, (숫자)]
    card = queue[turn].popleft() if queue[turn] else input().rstrip().split()

    if card[1] == 'next':
        pass
    elif card[1] == 'release':
        cards = cards - {card[2]}
    else:  # acquire
        if card[2] in cards:  # 카드가 공용공간에 x(가져올 수 x)
            queue[turn].append(card)
        else:  # 카드를 가져올 수 o
            cards.add(card[2])

    result.append(card[0])

print('\n'.join(map(str, result)))
