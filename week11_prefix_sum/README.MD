# [11주] [Prefix] 발표자료
1. [5549 행성 탐사](#1-5549-행성-탐사)

## 1. [5549 행성 탐사](https://www.acmicpc.net/problem/5549)
![2021-09-22 (3)](https://user-images.githubusercontent.com/69501435/134311763-6e62fce4-6718-4142-a800-3c598271d3c2.png)


### 1.1 자료구조
1. prefix(누적합의 2차원 version)

### 1.2 풀이과정
1. 우선 행별로 (J의 갯수, I의 갯수, O의 갯수)의 누적합을 구하고
2. 그 행별로 된 누적합을 열별로 확장시킨다.
3. 예)JO  ---- (1,0,0) (1,0,1) ---- (1,0,0) (1,0,1)
4.    IO  ---- (0,1,0) (0,1,1) ---- (1,1,0) (1,1,2)
5. 이런식으로 만들고 나면 만들어진 리스트는 왼쪽위 0,0기준으로 각 i,j 까지 만들어지는 직사각형에 포함된 J,I,O의 갯수가 된다.
6. 그 후에는 (i,j) ~ (l,m) 까지의 직사각형의 합은 
7. (l,m)까지 직사각형의합 - (i-1,m)까지 직사각형의합 - (l,j-1)까지 직사각형의 합 + (i-1,j-1)까지 직사각형의 합이 된다.
8. (밑에 증명 참고)
 

### 1.3 소스코드

```python
import sys
import heapq

def sol(n,stations,l,p):
    stations.sort(reverse=True)
    heap = []

    count = 0

    while p<l:
        while stations and stations[-1][0] <= p:
            dist, fuel = stations.pop()
            heapq.heappush(heap, -fuel)
        if not heap:
            break
        p -=heapq.heappop(heap)
        count+=1
    if l<=p:
        return count
    return -1

n = int(sys.stdin.readline())

stations = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

goal, gas = map(int,sys.stdin.readline().split())

print(sol(n,stations,goal,gas))


```



![KakaoTalk_20210922_175119085](https://user-images.githubusercontent.com/69501435/134313153-38d0545c-1d60-4b7e-83e1-16db5543c9bc.jpg)
