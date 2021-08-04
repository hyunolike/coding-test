
#4195 친구 네트워크

# 문제풀이 1: disjoint set 이용 -> union & find 함수이용


import sys
input = sys.stdin.readline

def find(x):   # x의 루트노드 반환
    if x == parent[x]:
        return x           # 자신이 루트이면 루트 반환
    a = find(parent[x])
    parent[x] = a
    return parent[x]       #자신이 루트노드가 아닐경우 재귀를 통해 루트노드 반환

def union(x,y):         # x,y가 서로다른 루트를 가졌을때 x를 루트로 하여 합쳐줌
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x  #x를 루트
        number[x] = number[x] + number[y]  #루트에 딸린 자식의 갯수를 따로 카운팅해줌



N = int(input().rstrip())

for i in range(N):
    parent = {}
    number ={}
    M = int(input().rstrip())

    for j in range(M):
        x,y = input().split()
        if x not in parent:
            parent[x] = x
            number[x] =1
        if y not in parent:
            parent[y] = y
            number[y] =1
# 처음 나올시 자기자신을 루트로 설정해주기 + 카운팅 설정
        union(x,y)
        print(number[parent[x]])
# 위에 x를 루트노드로 설정하여 합쳤으므로 루트노드의 속한 갯수를 출력시 답



