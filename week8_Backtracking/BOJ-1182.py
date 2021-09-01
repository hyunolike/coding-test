#1182 부분수열의 합

"""
문제풀이 1: 모든 경우 의수 다 다루기 위해 카운트기준 함수구현
2: pruning x

"""
import sys
input =sys.stdin.readline

n,s = map(int,input().split())
arr = list(map(int,input().split()))

ans = 0

def subset(a,total):
    global ans

    if a >= n:
        return
    total  = total + arr[a]
    #pruning 을 딱히 하지않음
    if total == s:
        ans += 1
    # 모든경우의수 포함
    subset(a + 1,total - arr[a])
    subset(a+1,total)

subset(0,0)
print(ans)