#14719 빗물

"""
문제풀이 : 주어진 문제에서 파악해야될 문제 해결방법은 높이의 따른
물이 고이는 것을 분석해야한다

구현 순서

1.패턴파악
패턴1. 왼<오 ㅇ
패턴2. 오>왼 ㅇ
패턴3. 왼=오  x
2.탐색 위치
처음부터 or 큰것부터

따라서 해당 블록에서 왼쪽,오른쪽 기준 자신보다 크면
빗물이 담긴다. 
담기는 빗물의 양은 = 둘중 최댓값의 최소 - 자신의 블록 높이
"""

import sys
input =sys.stdin.readline

H,W = map(int,input().rstrip().split())
arr = list(map(int,input().rstrip().split()))
ans = 0

for i in range(1,W-1):
    L = max(arr[:i])
    R = max(arr[i+1:])
    m = min(L,R)

    if L > arr[i] and R > arr[i]:
        ans += m - arr[i]

print(ans)