#2632 피자판매

import collections
import sys


def get_prefix_sum(nums):
    prefix_sum = collections.defaultdict(int)
    N = len(nums)
    for k in range(1, N):
        left, right = 0, k
        count = 0
        p_sum = sum(nums[:k])
        while count < N:
            prefix_sum[p_sum] += 1
            count += 1
            p_sum -= nums[left]
            p_sum += nums[right]
            left, right = (left+1) % N, (right+1) % N

    prefix_sum[0] += 1
    prefix_sum[sum(nums)] += 1
    return prefix_sum


sell = int(sys.stdin.readline().rstrip())
N, M = map(int, sys.stdin.readline().split())
A, B = [], []
for i in range(N):
    A.append(int(sys.stdin.readline().rstrip()))
for i in range(M):
    B.append(int(sys.stdin.readline().rstrip()))

prefix_A, prefix_B = get_prefix_sum(A), get_prefix_sum(B)

count = 0
for key in prefix_A.keys():
    if sell-key in prefix_B:
        count += prefix_A[key] * prefix_B[sell-key]
print(count)