import sys

n, m  = map(int,sys.stdin.readline().split())

arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

summation = [list(map(lambda x : int(x)-1,sys.stdin.readline().split())) for _ in range(m)]

result = []

for i in range(n):
    result.append([0])
    for j in range(n):
        result[i].append(result[i][j]+ arr[i][j])

for j in summation:
    cnt = 0
    for i in range(j[0],j[2]+1):
        cnt += result[i][j[3]+1]-result[i][j[1]]
    print(cnt)