#1620 포켓몬 마스터

#문제풀이 :1 . 딕셔너리로 품

import sys
input = sys.stdin.readline

N, M= map(int,input().split())
dic = {}

for i in range(N):
    name = input().rstrip()
    dic[name] = str(i+1)
    dic[str(i+1)] = name

for j in range(M):
    print(dic[input().rstrip()])
    