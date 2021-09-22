import sys
input = sys.stdin.readline

N = int(input())
t = list(map(int, input().split()))
p_sum = [0] * N
mistakes = [0] * 100005

for i in range(N-1):
	if t[i] > t[i+1]:
		p_sum[i] = p_sum[i-1] + 1
		mistakes[i+1] = 1
	else:
		p_sum[i] = p_sum[i-1]
if N > 1:
	p_sum[-1] = p_sum[-2]
p_sum = [0] + p_sum
Q = int(input())

for _ in range(Q):
	a, b = map(int, input().split())
	if a == b:
		print(0)
		continue
	else:
		ret = p_sum[b] - p_sum[a-1]
		if mistakes[b]:
			ret -= 1
	print(ret)
