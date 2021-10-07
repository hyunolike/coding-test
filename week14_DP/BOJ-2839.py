"""
#2839 - 설탕배달
DP

문제풀이 1: 노가다해서 안되면 dp로 풀어볼라했는데 풀려서 stop


코드가 많이 추함..
"""

import sys
input =sys.stdin.readline

N = int(input().rstrip())

temp = N%5
ans = 0

if N == 3:
    ans = 1
elif N == 4:
    ans = -1
elif N % 5 == 0:
    ans = N//5
elif N % 5 == 1: 
    a = N //5
    a = a-1
    ans = a+2

elif N % 5 == 2:
    a = N //5
    a = a -2
    if a < 0:
        ans = -1
    else:
        ans = a + 4
elif N % 5 == 3:    
    a = N//5
    ans = a+1
elif N % 5 == 4:
    a = N//5
    a = a-1
    if a<0:
        ans = -1
    else:
        ans = a + 3

print(ans)


