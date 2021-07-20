import sys
from collections import deque

input = sys.stdin.readline
n, t = map(int, input().split())
turns = deque(map(int, input().split()))
queue = list(deque() for _ in range(n+1))
cards = set()
result = list()

while turns:
    # 내 큐에 연산카드가 있는 경우 vs. 없는 경우
    turn = turns.popleft()
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


'''
while True:

    if queue[내차례]에 연산카드가 있나?
        있으면 수행. 없으면 continue
        
    card = cards.popleft()
    if next:
        pass
    elif release:
        privateCards.remove(card[2])
    else acquire:
        if privateCard에 있으면: -> 못 가져옴
            queue[내차례].append(카드)
        else: private에 없으면 -> 가져올 수 있음
            queue[내차례].append(ac의 숫자만) -> 굳이 필요있나??
            privateCards.append(카드숫자, 내 turn)
    result.append(card[0])
            
'''


