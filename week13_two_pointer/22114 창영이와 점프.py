import sys
input = sys.stdin.readline

n, k = map(int, input().split())
brick = list(map(int, input().split()))
idx = 0
answer = 1

for j in range(len(brick)):
    chance = True
    lcnt = 1
    for i in range(j, len(brick)):
        if k < brick[i] and not chance:
            idx = i
            break
        elif k < brick[i] and chance:
            chance = False
            lcnt += 1
        elif k >= brick[i]:
            lcnt += 1
    
    answer = max(answer, lcnt)

print(answer)