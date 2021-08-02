#9322 철벽알고리즘

#문제포인트 : 위치 연결해주기 -> INDEX 생각 끝


import sys
input = sys.stdin.readline

N = int(input().rstrip())

for i in range(N):
    code = []
    ans = []
    A = int(input().rstrip())
    code1 = input().split()
    code2 = input().split()
    secret = input().split()

    for i in code1:
        code.append(code2.index(i))
    
    for j in code:
        ans.append(secret[j])
    
    for k in ans:
        print(k,end =" ")