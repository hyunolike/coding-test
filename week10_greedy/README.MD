# [10주] [Greedy] 발표자료
1. [1826 연료 채우기](#1-1826-연료-채우기)

## 1. [1825 연료 채우기](https://www.acmicpc.net/problem/1826)
![2021-09-12](https://user-images.githubusercontent.com/69501435/132987359-4449b02b-ca68-4408-a88a-9f1ede275445.png)



### 1.1 자료구조
1. heap ( heapq.heap() 우선순위 큐 )

### 1.2 풀이과정
1. 현재 갈 수 있는 곳 중에서 기름을 가장 많이 채울 수 있는곳을 안지나고 최소의 루트로 목적지에 도달하는 법은 존재 하지 않는다. 이것이 핵심이다.
2. 즉 지금 위치에서 갈 수 있는 곳을 우선순위 큐에 넣는데 기준을 가장 기름을 많이주는 즉 - fuel을 key로 줬다 (-fuel을 기준으로 오름차순은 fuel이 큰거부터 우선순위큐로 저장된다)
3. 그래서 돌다가 만약 기름의 양이 가야하는 거리보다 커지면 루프를 탈출하고 출력 해줄 수 있도록 하였다.

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

(현재 갈 수 있는 곳 중에서 기름을 가장 많이 채울 수 있는곳을 안지나고 최소의 루트로 목적지에 도달하는 법은 존재 하지 않는다. 의 증명)
![KakaoTalk_20210912_213708724](https://user-images.githubusercontent.com/69501435/132987848-16fb03fc-05be-43fb-9b97-1b7365ae8f70.jpg)
