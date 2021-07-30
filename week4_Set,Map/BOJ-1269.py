#1269 대칭차집합

#문제풀이1.set 함수 사용

import sys
input = sys.stdin.readline

N, M = map(int,input().split())
a = set(map(int,input().split()))
b = set(map(int,input().split()))

print(len(a-b)+len(b-a))