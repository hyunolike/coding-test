"""
#1463 - 1로 만들기
전형적인 dp 문제

문제풀이 : 1: top->down / bottom -> up 두가지의 재귀 or 반복문을 구성할 생각을 가진상태
2: 탑다운시 반례 생성
3: 보틈 업으로 모든 수 탐색하면서 for 문진행


"""

import sys
input = sys.stdin.readline

N = int(input())

dp = [0] * (N + 1)

for i in range(2, N + 1):
   
    dp[i] = dp[i - 1] + 1

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if i % 2 == 0:  
        dp[i] = min(dp[i], dp[i // 2] + 1)

print(dp[N])