# 9 Week Simulation

1. 2933 미네랄
2. 14719 빗물
3. 3190 뱀
4. 1713 후보추천하기
5. [13335 트럭](#5-13335-트럭)
6. 14499 주사위굴리기
7. 14503 로봇 청소기
8. 17140 이차원 배열과 연산
9. 16236 아기상어
10. 1244 스위치 켜고 끄기

## 5. [13335 트럭](https://www.acmicpc.net/problem/13335)
![image](https://user-images.githubusercontent.com/44918665/132179064-c884a6c0-b746-4fdc-83f3-c8189f2a933c.png)

### 5.1. 문제유형
- Simulation

### 5.2. 풀이과정
- 주어진 로직을 따라가며 그대로 구현하였다.
- 두 가지 조건을 체크하며, 트럭을 통과시켰다.
- 1. 다리가 꽉 차 있는가?
- 2. 다리의 무게가 버틸 수 있는가?
- 다리가 꽉 차 있지 않고, 트럭 무게를 감당할 수 있으면 트럭을 통과시킨다.
- 다리 위의 트럭 초를 증가시키며 1칸씩 전진시킨다.
- ⭐ 주의할 점은 다리를 완전히 통과할 때, 동시에 다음 트럭이 들어와야 하는 경우를 고려해야한다.
- 따라서 미리 트럭을 제거해주었으므로, 마지막 소스코드에 1초를 추가해주었다.

### 5.3. 소스코드
```python
from collections import deque

n, w, l = map(int, input().split())
trucks = deque(list(map(int, input().split())))
bridge = deque()
sec = 0
while trucks:
    sec += 1
    total = sum([weight for weight, _ in bridge])
    
    if total+trucks[0] <= l and len(bridge) < w:
        go = trucks.popleft()
        bridge.append([go, 1])
    for i in range(len(bridge)):
        bridge[i][1] += 1
    if bridge[0][1] == w+1:
        bridge.popleft()

while bridge:
    sec += 1
    for i in range(len(bridge)):
        bridge[i][1] += 1
    if bridge[0][1] == w+1:
        bridge.popleft()
# 1초를 추가하는 이유
# 맨 앞 트럭이 다음 트럭이 들어 올 수 있도록 미리 빠져나가므로, 1초 일찍 종료됨
print(sec+1)
```


