## [1.14719 빗물 ](https://www.acmicpc.net/problem/14719)

![1231awsd](https://user-images.githubusercontent.com/87264787/132486556-ff0075d1-15d8-4403-89bf-2d1461aa075f.png)

### 1.1 풀이 과정

1. 빗물이 담길수 있는 상황 분석 -> (왼>오 + 왼,오>해당블록) or (왼 < 오 + 왼,오 >해당블럭)

1. 양쪽끝은 빗물이 담길수 없는 구조이므로 1~W-1 까지의 블록의 높이를 비교 = for 반복문 사용



### 1.2 자료구조

1.  구현



### 1.3 소스 코드

```python

#14719 빗물

"""
문제풀이 : 주어진 문제에서 파악해야될 문제 해결방법은 높이의 따른
물이 고이는 것을 분석해야한다

구현 순서

1.패턴파악
패턴1. 왼<오 ㅇ
패턴2. 오>왼 ㅇ
패턴3. 왼=오  x
2.탐색 위치
처음부터 or 큰것부터

따라서 해당 블록에서 왼쪽,오른쪽 기준 자신보다 크면
빗물이 담긴다. 
담기는 빗물의 양은 = 둘중 최댓값의 최소 - 자신의 블록 높이
"""

import sys
input =sys.stdin.readline

H,W = map(int,input().rstrip().split())
arr = list(map(int,input().rstrip().split()))
ans = 0

for i in range(1,W-1):
    L = max(arr[:i])
    R = max(arr[i+1:])
    m = min(L,R)

    if L > arr[i] and R > arr[i]:
        ans += m - arr[i]

print(ans)


```


### 1.4 한줄평

- 문제를 푸는데 필요한 조건 파악