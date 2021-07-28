# Week3 Heap 발표자료
- 12018 Yonsei TOTO

## [1. 12018 Yonsei TOTO](https://www.acmicpc.net/problem/12018)

![image](https://user-images.githubusercontent.com/44918665/127265598-4be16e2d-e350-4ca7-988a-f9b864f3c71e.png)

![image](https://user-images.githubusercontent.com/44918665/127265627-21013864-3f56-4556-be1f-798c1c4d5bb1.png)


### 1.1 자료구조

1. mylect (max heap) : 내 강의를 담을 힙 자료구조
2. milege (min heap) : 수강 신청한 마일리지 점수를 저장한 힙 자료구조

→ mylect가 max heap인 경우 : 마일리지를 초과할 경우 큰 마일리지가 소모되는 강의를 우선적으로 제거하기 위함

### 1.2 풀이 과정

1. 신청인원(P)과 수강인원(L) 차이를 구해 마일리지와 함께 heap에 저장한다.

    - heap은 마일리지를 최소로 사용하므로 min heap을 기준으로 한다.

2. P-L이 0보다 작은 경우 마일리지는 1을 필요로 한다.

3. P-L이 0보다 크거나 같은 경우, P-L이 0이 될 때까지 milege를 꺼내면서 1씩 감소시킨다.

    - P-L이 0이 되면 마일리지에서 pop한 값을 mylect에 저장한다.

4. mylect에 담긴 마일리지 합이 m보다 클 경우 하나씩 pop해나간다.

5. 최종적으로 mylect에 남은 강의 수를 출력한다.

### 1.3 소스 코드

```python
import heapq

n,m = map(int, input().split())
mylect = []
present = []
for _ in range(n):
    p, l = map(int, input().split())
    milege = list(map(int, input().split()))
    heapq.heapify(milege)
    heapq.heappush(present, [p-l, milege])

while present:
    data = heapq.heappop(present)
    if data[0]<0:
        heapq.heappush(mylect, -1)
    else:
        while data[0]!=0:
            heapq.heappop(data[1])
            data[0] -= 1
        heapq.heappush(mylect, -1 * heapq.heappop(data[1]))
while -1*sum(mylect) > m:
    heapq.heappop(mylect)
print(len(mylect))
```
