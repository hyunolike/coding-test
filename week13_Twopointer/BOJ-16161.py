# 16161 가장 긴 증가하는 팰린드롬 부분수열 / 20922 겹치는 건 싫어

"""
문제풀이 1: 목표 : 팰린드롬 수열의 탐색
"""

import sys
from typing import ChainMap
input = sys.stdin.readline

N =int(input().rstrip())
arr = list(input().rstrip().split())
ans = 0
comp = []
comp.append(arr[0])

def verify(arr1,arr2,n):
    if len(arr1) % 2 == 0:
        a = len(arr1)
        b = arr2[n:n+a]
        b.reverse()
        if arr1 == b:
            return True
        else:
            return False
    else:
        a = len(arr1)
        arr1.pop()
        b = arr2[n:n+a-2]
        b.reverse()
        if arr1 == b:
            return True
        else:
            return False


for i in range(1,N):
    if arr[i] > arr[i-1]:
        comp.append(arr[i])
    elif arr[i] < arr[i-1]:
        if len(comp) >= 2:
            if verify(comp,arr,i):
                ans = len(comp) + (len(comp)-1)/2
                comp = []
            else:
                comp = []
                comp.append(arr[i])
    elif arr[i] == arr[i-1]:
        if len(arr) >= 2 and verify(comp,arr,i):
            ans = (len(comp)) * 2
            comp = []
        else:
            ans = 2 
            comp = []

print(ans)

