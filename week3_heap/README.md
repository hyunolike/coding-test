## [1. 12018 Yonsei TOTO](https://www.acmicpc.net/problem/12018)

![image](https://user-images.githubusercontent.com/44918665/127265598-4be16e2d-e350-4ca7-988a-f9b864f3c71e.png)

![image](https://user-images.githubusercontent.com/44918665/127265627-21013864-3f56-4556-be1f-798c1c4d5bb1.png)


### 1.1 자료구조

1. mylect (max heap) : 내 강의를 담을 힙 자료구조
2. milege (min heap) : 수강 신청한 마일리지 점수를 저장한 힙 자료구조

→ mylect가 max heap인 경우 : 마일리지를 초과할 경우 큰 마일리지가 소모되는 강의를 우선적으로 제거하기 위함

### 1.2 해결과정

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

## 2. [1655 가운데를 말해요](https://www.acmicpc.net/problem/1655)

### 2.1. 문제유형
- heap, 우선순위 큐
![image](https://user-images.githubusercontent.com/44918665/128122117-fcab72f3-eb84-4632-81cf-5dcb4e1b4916.png)

### 2.2. 자료구조
- left 최대힙의 첫 번째 수가 중간값이 된다.
1. left (max heap): 최소힙으로 오름차순 저장
2. right (min heap): 최대값으로 내림차순 저장

- 처음에 하나의 heap에 넣고 index로 중간값을 접근하는 실수를 범했다.
- heap의 경우 트리형태로 저장되기 때문에 len(heap)//2 or len(heap)//2-1로 인덱싱하는 순서와 heap에서 꺼내는 순서가 다르다.
- 따라서 max heap인 left, min heap인 right 2개의 자료구조가 필요하다.
### 2.3. 해결과정
1. left의 최대힙의 루트가 중간값이 되도록 left, right에 값을 나눠 담는다.
2. 길이가 같은 경우 left에 우선적으로 담고, 다른 경우 right에 담는다.
3. left의 루트(최대값)가 right의 루트(최소값)보다 클 경우 꺼내서 위치를 바꿔담는다.
4. 결과적으로 left heap에는 중간값부터 가장 작은값까지 내림차순으로 값이 저장된다.

```python
import sys
import heapq

n = int(input())
data = list(int(sys.stdin.readline().strip()) for _ in range(n))
left = []
right = []

for num in data:
    if len(left) == len(right):
        heapq.heappush(left, (-num, num))
    else:
        heapq.heappush(right, (num, num))
    
    if left and right and left[0][1] > right[0][1]:
        l = heapq.heappop(left)[1]
        r = heapq.heappop(right)[1]
        heapq.heappush(left, (-r, r))
        heapq.heappush(right, (l, l))
    print(left[0][1])
```
