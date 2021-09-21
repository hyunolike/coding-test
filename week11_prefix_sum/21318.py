import sys

n = int(sys.stdin.readline())

level = list(map(int,sys.stdin.readline().split()))

query = int(sys.stdin.readline())

mistake = [list(map(int,sys.stdin.readline().split())) for _ in range(query)]

stairs = [0]
cnt = 0
for i in range(n-1):
    if level[i]>level[i+1]:
        cnt+=1
        stairs.append(cnt)
    else:
        stairs.append(cnt)
stairs.append(cnt)
for i in mistake:
    print(stairs[i[1]-1] - stairs[i[0]-1])