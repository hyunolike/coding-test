# 13414 수강신청

#문제풀이 : 1. 딕셔너리 이용 
# 2.항상 반복문 조건문 쓸때 범위 확인잘하기  <- 맨날 처음에 생각안함

import sys
input = sys.stdin.readline
ans =[]
apply = {}
N , M = map(int,input().split())

for i in range(M):
    a = input().rstrip()
    apply[a] = i


ans = sorted(apply.items() , key = lambda x: x[1])

for i in range(N):
    print(ans[i][0])
    if len(ans)-1 == i:
        break