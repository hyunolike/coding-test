"""
#15486 
퇴사2

문제풀이 1:


"""

from _typeshed import SupportsLenAndGetItem
import sys
input = sys.stdin.readline

N = int(input())

dp = [0] * (N + 1)

T,P = [],[]
dp = [0] *(N+1)

for i in range:
    temp = list(map(int,input().rstrip().split()))
    T.append(temp[0])
    P.append(temp[0])

for i in range(0,N):
    if T[i] <= N-i:
        dp[i+T[i]]=max(dp[i+T[i]],dp[i]+P[i])

    dp[i+1] = max(dp[i+1], dp[i])
print(dp[N])