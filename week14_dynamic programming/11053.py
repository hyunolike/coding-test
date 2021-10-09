import sys


n = int(sys.stdin.readline())

arr = list(map(int,sys.stdin.readline().split()))

result = []
for i in range(n):
    result.append([])
    for j in range(2):
        result[i].append(0)

result[0][0] = 0
result[0][1] = 1

for i in range(1,n):
    small_idx = [j for j in range(i) if arr[j]<arr[i]] #지금 숫자보다 작은놈들

    if len(small_idx) == 0:
        max_val = [max(result[j]) for j in range(i)]
        max_val_real = max(max_val)
        result[i][0] = max_val_real
        result[i][1] = 1
    else:
        max_val = [result[j][1] for j in small_idx]
        max_val_real = max(max_val)
        result[i][0] = max_val_real
        result[i][1] = max_val_real+1

max_val = [max(result[j]) for j in range(n)]
print(max(max_val))
