# 시간 초과 발생 ㅠ,ㅠ

import sys
from collections import defaultdict

input = lambda : sys.stdin.readline().rstrip()

n ,m = map(int, input().split())

Pokemon = defaultdict(int)

for i in range(n):
    Pokemon_name = input()

    Pokemon[Pokemon_name] = i+1

# print(Pokemon)

def get_key(val):
    for key, value in Pokemon.items():
        if val == value:
            return key

for _ in range(m):
    problem = input()
    if problem.isalpha():
        print(Pokemon[problem])
    else:
        result = int(problem)
        print(get_key(result))

# 시간 초과 개선

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dict = {}

for i in range(1, n + 1):
    a = input().rstrip()
    dict[i] = a
    dict[a] = i

for i in range(m):
    quest = input().rstrip()
    if quest.isdigit():
        print(dict[int(quest)])
    else:
        print(dict[quest])