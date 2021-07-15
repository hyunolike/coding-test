from sys import stdin

n = int(stdin.readline())
towers = list(map(int, stdin.readline().split()))
result = [0]*n

for i in range(1, n):
    idx = i-1
    while True:
        if towers[i] <= towers[idx]:
            result[i] = idx+1
            break
        else:  # 수신 실패
            idx = result[idx]-1
            if idx == -1:
                break
print(*result)
