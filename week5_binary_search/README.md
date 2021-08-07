# 문제풀이
## 1. [2343 기타 레슨](https://www.acmicpc.net/problem/2343)
![image](https://user-images.githubusercontent.com/44918665/128294339-b305744a-e92d-4e5d-b229-71afe96410c3.png)
### 1.1. 문제유형
- Binary Search
### 1.2. 자료구조
- cnt (int) : 블루레이 개수
- file (int) : 레슨을 저장한 파일 크기
- mid (int) : 블루레이 크기
- left (int) : 가장 작은 블루레이 크기
- right (int) : 가장 큰 블루레이 크기
### 1.3. 해결과정
- 가장 작은 블루레이 크기는 max(lesson), 최대 크기는 sum(lesson)이다.
- 주어진 m개의 블루레이에 강의를 저장하되, 블루레이 크기는 작을수록 좋다.
- 따라서 블루레이의 크기를 찾는 이분탐색 문제로 해결할 수 있다.

1. left는 max(lesson), right는 sum(lesson)로 설정한다.
2. left <= right일 동안 아래 과정을 반복한다.
3. 블루레이 크기를 중간값인 (left + right)//2로 지정한다.
4. 만약 파일 크기가 중간값을 넘어서면 cnt를 증가시키고 file에 영상을 저장한다.
5. 파일 크기가 아직 중간값보다 작다면 file에 영상을 더 추가한다.
6. 반복이 끝난 후 file에 영상이 남아있다면 cnt를 증가시킨다.
7. 최종 cnt가 m보다 크다면, 블루레이 크기가 작은 것이므로 left = mid+1
8. 최종 cnt가 m보다 작거나 같다면, 블루레이 크기가 큰 것이므로 answer에 중간값 저장 후 right = mid-1
9. 최종 answer를 출력한다.

```python
n, m = map(int, input().split())
lesson = list(map(int, input().split()))
left, right = max(lesson), sum(lesson)
answer = left

while left <= right:
    cnt = 0
    file = 0
    mid = (left + right)//2

    for l in lesson:  
        if file+l > mid:
            cnt += 1
            file = l
        else:
            file += l
    if file:
        cnt+=1
    
    if cnt>m:
        left = mid+1
    else:
        answer = mid
        right = mid-1
print(answer)
```

## 2. [2110 공유기 설치](https://www.acmicpc.net/problem/2110)
![image](https://user-images.githubusercontent.com/44918665/128295606-440b3701-3008-47eb-9208-af5bbb95b3dc.png)
### 2.1. 문제유형
- Binary Search
### 2.2. 자료구조
- cnt (int): 공유기 개수
- left (int): 최소 거리 == 1
- right (int): 최대 거리 == (마지막 집 좌표 - 첫 번째 집 좌표)
- mid (int): 공유기 간 거리 == (left + right) // 2
- wifi (int): 공유기가 설치된 집 좌표
### 2.3. 해결과정
- 집 좌표 최대 크기가 10억이므로, 순차탐색이 아닌 이분탐색을 떠올려볼 것
- 공유기 간 최대거리를 찾는 것이 목적이므로 이분탐색 활용할 것
1. left <= right일 동안 아래 과정을 반복하며 중간값이 최대가 되는 값은 탐색한다.
2. 중간값 mid = (left+right)//2로, 최초 공유기 개수는 1, 최초 공유기 위치는 house[0]으로 설정한다.
3. 반복문을 돌며 2번째 집부터 마지막 집까지 아래 조건을 체크한다.
4. i번째 집 좌표가 이전 공유기 위치로부터 + 최대거리(중간값 mid)을 넘어서면 새로운 공유기를 설치하고, 공유기 개수를 증가시킨다.
5. 반복문 종료 후, 공유기 개수가 c보다 작다면 최대거리가 긴 것이므로 right = mid - 1
6. 공유기 개수가 c보다 크다면 최대거리가 짧은 것이므로 answer에 최대거리 저장 후 left = mid + 1
7. answer를 출력한다.
```python
import sys

n,c = map(int, input().split())
house = list(int(sys.stdin.readline()) for _ in range(n))
house.sort()

left = 1
right = house[-1]-house[0]
answer = 0

while left <= right:
    mid = (left+right)//2
    cnt = 1
    wifi = house[0]

    for i in range(1, n):
        if house[i] >= wifi + mid:
            cnt += 1
            wifi = house[i]
    
    if cnt < c:
        right = mid - 1
    else:
        left = mid + 1
        answer = mid
print(answer)
```

## 3. [1072 게임](https://www.acmicpc.net/problem/1072)
![image](https://user-images.githubusercontent.com/44918665/128458629-e7473b16-6ef6-4120-ab90-fbcca66a5f03.png)

### 3.1. 문제유형
- Binary Search
### 3.2. 자료구조
1. 중요한 점은 y/x * 100과 같이 실수형으로 계산 후 int로 바꿔줄 시 정확하지 않을 수 있다.
2. 따라서 실수형 계산이 아닌, y * 100//x처럼 정수형 계산으로 바꿔 승률을 계산해야 한다.
- z (int): 초기 승리한 게임 수 y/전체 게임 수 x * 100
- target (int): 승리한 경기수를 이분탐색하며 계산한 승률
- left (int): 더해나갈 승리한 횟수의 최소값
- right (int): 더해나갈 승리한 횟수의 최대값
- mid (int): (left+right)//2 == 중간값으로 실제 더할 승리한 횟수
### 3.3. 해결과정
1. 승리한 게임 수를 찾는 게 핵심이며, 범위는 0부터 x(10 ** 9)까지이다.
2. 따라서 1부터 적용할 경우 10억 번 연산이 필요하므로 이분탐색을 사용한다.
3. x,y에 mid를 더한 후 승률을 계산한다.
4. 승률이 초기 승률값과 같다면 left = mid+1
5. 승률이 초기 승률값보다 크다면 answer=mid 후 right = mid-1
6. 3-5를 left <= right일 동안 반복한다.
7. 반복이 끝난 후 승률이 초기값과 같다면 -1을, 아니라면 answer를 출력한다.
```python
x, y = map(int, input().split())
left, right = 0, x
answer = 0
z = y*100//x

while left<=right:
    mid = (left+right)//2
    game = x + mid
    win = y + mid
    target = win*100//game

    if z == target:
        left = mid + 1
    else:
        answer = mid
        right = mid - 1

x, y = x+answer, y+answer
result = y*100//x
if result == z:
    print(-1)
else: 
    print(answer)
```
## 4. [1300 K번째 수](https://www.acmicpc.net/problem/1300)
![image](https://user-images.githubusercontent.com/44918665/128458651-bc87c60f-b462-4537-a8a7-1e8a33ed2acb.png)
### 4.1. 문제유형
- Binary Search
### 4.2. 자료구조
- left (int): 각 행의 최소값 인덱스 == 1
- right (int): 각 행의 최대값 인덱스 == n
- mid (int): (left+right)//2 == 중간값으로 탐색해 나갈 값
### 4.3. 해결과정
- 핵심 아이디어는 행별로 mid값보다 작은 값의 개수를 세는 것이다.
- 각 행의 값은 i의 배수이며 작은 값들의 개수는 최대 n, 최소 mid // i이다.
1. left <= right 동안 mid를 계산 후 n행에 대해 mid보다 작은 개수를 구한다.
2. mid보다 작은 개수가 k와 같거나 크면 answer = mid 후 right = mid - 1 (더 작은 좌측탐색)
3. mid보다 작은 개수가 k보다 클 경우 left = mid + 1 (더 큰 우측탐색)
4. 반복문 종료후 answer를 출력한다.
```python
n = int(input())
k = int(input())
cnt, answer = 0, 0
left, right = 1, k

while left <= right:
    mid = (left + right)//2
    cnt = 0
    for i in range(1, n+1):
        cnt += min(mid // i, n)
    if cnt >= k:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1
print(answer)

```
