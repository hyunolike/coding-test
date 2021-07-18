# 구현하기 어려워요 ㅠ,ㅠ

import sys

a ,b ,n = map(int, sys.stdin.readline().split())

orders = [] # 주문들
t_b = 0 # 상민 포장완료 시간
cnt_b = 0 # 상민 포장 개수
t_r = 0 # 지수 포장완료 시간
cnt_r = 0 # 지수 포장 개수
for _ in range(n):
    t, c, m = sys.stdin.readline().split()
    orders .append([int(t),c,int(m)])
wrap_orders = []

for t,c,m in orders:
    if c == 'B':
        t_b = max(t, t_b)
        for _ in range(m):
            wrap_orders.append([t_b, c])
            t_b += a
            cnt_b += 1
    elif c=='R':
        t_r = max(t, t_r)
        for _ in range(m):
            wrap_orders.append([t_r, c])
            t_r += b
            cnt_r += 1

sorted_wrap_orders = sorted(wrap_orders, key=lambda x : (x[0],x[1]))
SM = []
JS = []

for i in range(len(sorted_wrap_orders)):
    if sorted_wrap_orders[i][1] == 'B':
        SM.append(i+1)
    elif sorted_wrap_orders[i][1] == 'R':
        JS.append(i+1)

print(cnt_b)
for i in range(len(SM)):
    print(SM[i], end=" ")
print()
print(cnt_r)
for i in range(len(JS)):
    print(JS[i], end=" ")


