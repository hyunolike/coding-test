import sys

n, k, q, m = map(int,sys.stdin.readline().split())

sleep = list(map(int,sys.stdin.readline().split()))

code = list(map(int,sys.stdin.readline().split()))

distance = [list(map(int,sys.stdin.readline().split())) for _ in range(m)]

chulseok = [0]*(n+3)

for i in code:
    if i in sleep:
        continue
    idx = 1
    while True:
        if idx*i in sleep:
            idx+=1
            continue
        try:
            chulseok[idx*i] = 1
            idx+=1
        except:
            break

for i in distance:
    count = 0
    
    for j in range(i[0],i[1]+1):
        if chulseok[j] == 0:
            count+=1
    print(count)