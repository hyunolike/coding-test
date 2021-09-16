import sys
input = sys.stdin.readline

n,k,q,m = map(int, input().split())

sleep = [0]*(n+3)
check = [0]*(n+3)

for i in map(int, input().split()):
    sleep[i] = 1
for i in map(int, input().split()):
    if sleep[i]: 
        continue
    for j in range(i, n+3, i):
        if not sleep[j]:
            check[j] = 1

prefix = [check[0]]
for i in range(1, n+3):
    prefix.append(prefix[-1]+check[i]) # 각 번호 i까지 출석한 얘들 합 구하기

for _ in range(m):
    s, e = map(int, input().split()) # s부터 e까지 결석한 얘들
    print(e-s+1 - (prefix[e]-prefix[s-1])) # 전체 - (s부터 e까지 출석한 얘들)