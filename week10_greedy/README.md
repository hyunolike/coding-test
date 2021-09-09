# 10 Week Greedy

1. [1931 회의실 배정](#1-1931-회의실-배정)
2. [13164 행복 유치원](#2-13164-행복-유치원)
3. [1946 신입사원](#3-1946-신입사원)
4. [1339 단어 수학](#4-1339-단어-수학)
5. [17609 회문](#5-17609-회문)
6. [1715 카드 정렬하기](#6-1715-카드-정렬하기)
7. [1826 연료 채우기](#7-1826-연료-채우기)
8. [1911 흙길 보수하기](#8-1911-흙길-보수하기)

## 1. [1931 회의실 배정](https://www.acmicpc.net/problem/)
![image](https://user-images.githubusercontent.com/44918665/132624543-7288c4ab-c8c9-4151-bd08-f49a360eb5fe.png)

### 1.1. 문제유형
- 그리디

### 1.2. 해결과정
- 해당 문제는 (종료시간, 시작시간)을 기준으로 정렬한 후 카운트해야한다.
1. 회의를 가장 많이하려면, 빨리 끝나는 회의 먼저 시작한다.
2. 끝나는 시간이 동일하다면, 시작 시간이 빠른 회의를 먼저 시작한다.
3. 현재 종료된 회의시간 <= 다음 회의 시작시간, 이라면 다음 회의를 시작하고 카운트한다.

### 1.3. 소스코드
```python
n = int(input())
rooms = [list(map(int,input().split())) for _ in range(n)]
rooms = sorted(rooms, key=lambda x: (x[1], x[0]))
answer = 0
end = 0

for s, e in rooms:
    if end <= s:
        answer+=1
        end = e

print(answer)
```

### 1.4. 노트필기
![image](https://user-images.githubusercontent.com/44918665/132624927-c98cfb0b-ea21-4884-bdf7-0a00f811a31e.png)

## 2. [13164 행복 유치원](https://www.acmicpc.net/problem/13164)
![image](https://user-images.githubusercontent.com/44918665/132624973-e8c4249a-174a-49dc-86bf-8269aae900bd.png)

## 2.1. 문제유형
- 그리디

### 2.2. 해결과정
- ⭐ 반드시 조를 나누지 않더라도 최소 '비용'은 구할 수 있다.
- ⭐ 최소 비용은 인접한 값들중에서 차이의 최소값을 우선적으로 묶는 것이다.
- 티셔츠 비용이 (조 안에서) 가장 큰 키 - 가장 작은 키이다.
- 조를 나누는 기준은 인접한 원생끼리 묶는다.
- 원생은 키 순으로 오름차순 정렬되어 있다.

### 2.3. 소스코드
```python
n, k = map(int, input().split())
childs = list(map(int,input().split()))
diff = []
for i in range(1, n):
    diff.append(childs[i]-childs[i-1])

diff.sort()
result=0
for i in range(n-k):
    result+=diff[i]
print(result)
```

### 2.4. 노트필기
![image](https://user-images.githubusercontent.com/44918665/132625224-8e646335-0e3e-4b4c-bf3e-11c692762c70.png)
