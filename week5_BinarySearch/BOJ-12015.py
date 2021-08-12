#12015 가장 긴 증가하는 부분

#문제풀이 1: LIS 활용  +
# 나무위키 : 설명 :https://namu.wiki/w/%EC%B5%9C%EC%9E%A5%20%EC%A6%9D%EA%B0%80%20%EB%B6%80%EB%B6%84%20%EC%88%98%EC%97%B4#rfn-1

import sys
input = sys.stdin.readline
from bisect import bisect_left

N = int(input().rstrip())
arr = list(map(int,input().rstrip().split()))
ans = [0]

for i in arr:
    if ans[-1] < i:
        ans.append(i)
    else:
        ans[bisect_left(arr,i)] = i

print(len(ans)-1)