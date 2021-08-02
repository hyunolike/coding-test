
#1302 베스트 셀러

#문제포인트 : 1.딕셔너리 성질 파악 2. 순서 정해주기


import sys
input = sys.stdin.readline

N = int(input().rstrip())
sell = {}
order = []

for i in range(N):
    book = input().rstrip()
    if book in sell:
        sell[book] += 1
    else:
        sell[book] = 1

for j in sell.keys():
    if sell[j] == max(sell.values()):
        order.append(j)

order.sort()
print(order[0])


