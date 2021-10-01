
# 20922 겹치는 건 싫어

"""
문제풀이 1: 목표 
"""

import sys
input =sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
num_list = list(map(int, input().split()))
arr = deque()
max_len = 0
num_cnt = {}

for i in range(N):
    arr.append(num_list[i])
    if num_list[i] not in num_cnt:
        num_cnt[num_list[i]] = 0
    num_cnt[num_list[i]] += 1

    if num_cnt[num_list[i]] > K:
        max_len = max(max_len, len(arr)-1)
        while True:
            a = arr.popleft()
            num_cnt[a] -= 1
            if num_list[i] == a:
                break

print(max(max_len, len(arr)))

""" for 문 + index,count = 시간초과
import sys
input =sys.stdin.readline

N,M = map(int,input().rstrip().split())
arr = list(input().rstrip().split())
ans = []
comp = []
comp.append(arr[0])

for i in range(1,N):
    
    a = arr[i]
    if comp.count(a) >= M:
        ans.append(len(comp))

        b = comp.index(a)
        comp = comp[b+1:]

    comp.append(arr[i])

print(max(ans))

"""