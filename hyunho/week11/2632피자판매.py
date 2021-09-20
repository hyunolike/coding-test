import sys

target = int(sys.stdin.readline().rstrip())
m, n = map(int, sys.stdin.readline().split())
left = [int(sys.stdin.readline().rstrip()) for _ in range(m)]
right = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

left_sum, right_sum = [0] * 2000001, [0] * 2000001
left_sum[0] = right_sum[0] = 1
left_len, right_len = len(left), len(right)
for i in range(left_len):
    s = 0
    
    for j in range(left_len):
        s += left[(i + j) % m]
        
        if s > target:
            break
        else:
            left_sum[s] += 1

for i in range(right_len):
    s = 0
    for j in range(right_len):
        s += right[(i + j) % n]
        if s > target:
            break
        else:
            right_sum[s] += 1

# 한 쪽에서 여러개의 합으로 하나의 target에 도달 하는 경우.(예외 처리)
left_sum[sum(left)] = right_sum[sum(right)] = 1


ans = 0
for i in range(target + 1):
    ans += (left_sum[i] * right_sum[target - i])
print(ans)
