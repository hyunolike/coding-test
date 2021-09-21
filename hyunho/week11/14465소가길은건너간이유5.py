import sys
input = sys.stdin.readline

N, K, B = map(int, input().split())
broken_list = [0 for _ in range(N+1)]

for _ in range(B):
    b = int(input())
    broken_list[b] = 1

for i in range(1, N+1):
    broken_list[i] += broken_list[i-1]

answer = B
for i in range(K, N+1):
    answer = min(answer, broken_list[i] - broken_list[i-K])

print(answer)
