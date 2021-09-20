import sys
input = sys.stdin.readline

target = int(input())
m, n =map(int, input().split())
A = [int(input()) for _ in range(m)]
B = [int(input()) for _ in range(n)]

A_sum, B_sum = [0]*2000001, [0]*2000001
A_sum[0] = B_sum[0] = 1
A_len, B_len = len(A), len(B)

for i in range(A_len):
    s = 0

    for j in range(A_len):
        s += A[(i+j)%m]

        if s>target:
            break
        else:
            A_sum[s]+=1

for i in range(B_len):
    s = 0
    for j in range(B_len):
        s += B[(i+j)%n]
        if s>target:
            break
        else:
            B_sum[s]+=1

A_sum[sum(A)] = B_sum[sum(B)] = 1

ans=0
for i in range(target+1):
    ans += (A_sum[i]*B_sum[target-i])
print(ans)