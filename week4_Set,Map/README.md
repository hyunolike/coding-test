# Week3 Heap 발표자료

## [1.4195 친구 네트워크](https://www.acmicpc.net/problem/4195)

![pa1](https://user-images.githubusercontent.com/87264787/128143720-95f786dc-5609-4f4f-a459-965352606fca.png)

### 1.1 풀이 과정

1. 이 문제는 친구들이 서로 연결됬을때 연결된 총 친구의 수 를 구하는 문제이다
    이때  이를 트리구조로 생각 하면 좋을것 같다
    
![aa123](https://user-images.githubusercontent.com/87264787/128143749-17001089-8198-49a8-bee9-a81c037d0ce8.png)

2. 이 문제에서는 단순히 친구관계만 따지므로 두 트리중 하나를 다른트리의 서브트리로 넣어주면 해결

3. 이러한 것을 disjoint set의 union,find 구조를 이용 하여 구현

4. 이때 카운트도 딕셔너리로 구현하여 답 도출

### 1.2 자료구조

1.  union(x,y) 는 y의 트리를 x의 서브트리로 넣어주는 함수
    이때 x,y트리의 depth를 고려하지 않는 union함수 이므로 시간초과시 path comprehension 방식사용

2.  find(x) 는 x의 루트노드를 반환 하는 함수



### 1.3 소스 코드

```python

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
        parent[y] = x  # 다른조건 따지지 않고 x를 루트로 설정

        number[x] = number[x] + number[y]  #루트에 딸린 자식의 갯수를 따로 카운팅해줌
#tree_size 함수도 ok

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


```
