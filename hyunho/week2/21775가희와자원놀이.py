# 기존 코드로는 시간초과 발생
# 그래서 sys 라이브러리사용해서 입력 시간 단축하니 성공 :)

import sys
from collections import deque

input = sys.stdin.readline
n, t = map(int, input().split())
arr = deque(map(int, input().split()))

acquired = {}
card_on_hand = [None]*(n+1)
cards = [deque(input().split()) for _ in range(t)]
j = 0

for i in arr:
    if card_on_hand[i] == None:
        if cards[j][1] == 'acquire':
            if cards[j][2] not in acquired:
                acquired[cards[j][2]] = None
            else:
                card_on_hand[i] = j
        elif cards[j][1] == 'release':
            acquired.pop(cards[j][2], None)
        print(cards[j][0])
        j += 1
    else:
        print(cards[card_on_hand[i]][0])
        if cards[card_on_hand[i]][2] not in acquired:
            acquired[cards[card_on_hand[i]][2]] = None
            card_on_hand[i] = None




