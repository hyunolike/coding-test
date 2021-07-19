import sys
from collections import deque

def first(n, orders, cards):
    people = deque()
    all_cards = dict()
    people = [0 for i in range(500001)]
    
    for order in orders:
        if people[order]:
            card = people[order]
            if card[1]=='acquire':
                print(card[0])
                if card[2] not in all_cards.keys():
                    all_cards[card[2]] = order
                    people[order]=0
                else:
                    people[order]=card
                    pass
            else:
                print(card[0])
        else:
            card = cards.popleft()
            if card[1]=='acquire':
                print(card[0])
                if card[2] not in all_cards.keys():
                    all_cards[card[2]] = order
                    people[order]=0
                else:
                    people[order]=card
                    pass
            elif card[1]=='release':
                print(card[0])
                all_cards.pop(card[2])
            else:
                print(card[0])

n, t = map(int, input().split())
orders = list(map(int, input().split()))
cards = deque()
for i in range(t):
    tmp = sys.stdin.readline().strip().split()
    if len(tmp)==3:
        tmp[0]=int(tmp[0])
        tmp[2]=int(tmp[2])
    else:
        tmp[0] = int(tmp[0])
    cards.append(tmp)

first(n, orders, cards)