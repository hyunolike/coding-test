import sys
input=sys.stdin.readline

N, H = map(int, input().split())
cave = [int(input()) for _ in range(N)]

A = [0] * (H + 1)
B = [0] * (H + 1)
result = [0] * (H + 1)


for i in range(N):
    if i % 2 == 0:
        B[cave[i]] += 1
    else:
        A[H - cave[i] - 1] += 1


for i in range(H-1, -1, -1):
    A[i] += A[i + 1]
for i in range(1, H):
    B[i] += B[i - 1]


for i in range(0, H):
    result[i] = A[i] + B[i]

print(N - max(result), result.count(max(result)))