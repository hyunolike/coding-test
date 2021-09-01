## [1.14888 연산자이동 ](https://www.acmicpc.net/problem/14888)

![ABCABC](https://user-images.githubusercontent.com/87264787/131652069-bdd23edf-edef-4a12-afa0-08c310635a8a.png)

### 1.1 풀이 과정

1. 모든 계산결과를 구해야 하나 생각 ->promising 조건생각

1. 어쩔수없이 모든 결과를 하나하나 비교해야 된다고 결론 ->완전 탐색 생각
 
1. DFS로 구현



### 1.2 자료구조

1.  DFS사용

1. 완전탐색



### 1.3 소스 코드

```python

#14888 연산자 끼워넣기

"""
문제풀이 

1: 처음에 완전탐색이 아닌 조건을 덧붙여서 중간에 promising을 해주면 좋다고 생각

2. promising여건이 잘안나와서 그냥 완전탐색으로 dfs 구현


"""

import sys
input = sys.stdin.readline

N = int(input().rstrip())

arr = list(map(int,input().rstrip().split()))

a,b,c,d = map(int,input().rstrip().split())

ans_min = -sys.maxsize
ans_max = sys.maxsize

def dfs(num, idx, add, sub, mul, div):
    global ans_min, ans_max
    if idx == N:  #종료조건
        ans_max = max(ans_max, num)
        ans_min = min(ans_min, num)
        return 
    #완전 탐색구현
    if add > 0:
        dfs(num + arr[idx], idx + 1, add - 1, sub, mul, div)
    if sub > 0:
        dfs(num - arr[idx], idx + 1, add, sub - 1, mul, div)
    if mul > 0:
        dfs(num * arr[idx], idx + 1, add, sub , mul -1, div)
    if div > 0:
        dfs(int(num / arr[idx]), idx + 1, add, sub, mul, div -1)



dfs(arr[0], 1, a, b, c, d)
print(ans_max)
print(ans_min)



```


### 1.4 한줄평

- 완전탐색 dfs