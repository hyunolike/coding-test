#2002 추월

#문제포인트 : 1. 초월을 어떻게 구별할까
# -> 자기가 가진 순위 보다 뒤에있는것들이 더낮다면 그 해당차는 초월을 한것으로 간주

import sys
input = sys.stdin.readline

enter = {}
out = []
ans = 0

N = int(input().rstrip())

for i in range(N):
    car = input().rstrip()
    enter[car] = i

for j in range(N):
    out.append(input().rstrip())

for i in range(N):
    for j in range(i+1,N):
        if enter[out[i]] > enter[out[j]]:
            ans = ans+1
            break

print(ans)