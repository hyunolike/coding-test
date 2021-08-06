# 9375 패션왕 신해빈

# 문제풀이 1:  가능한 경우의수 = 부분집합 -1 
# 나머지는 딕셔너리 + 리스트 구조로 한개의 종류에 여러개가 속하는 구조를 구현할때 사용

import sys
input = sys.stdin.readline

N = int(input().rstrip())

for i in range(N):
    cloth = {}
    ans = 1
    M = int(input().rstrip())
    for _ in range(M):
        name , gear = input().split()
        if gear in cloth.keys():
            cloth[gear].append(name)
        else:
            cloth[gear] = [name,""]
    for key in cloth.keys():
        ans = ans * len(cloth[key])
    print(ans -1 )
