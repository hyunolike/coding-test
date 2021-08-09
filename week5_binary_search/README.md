# 문제풀이
1. [2343 기타레슨](#1-2343-기타레슨)
2. [2110 공유기 설치](#2-2110-공유기-설치)
3. [1072 게임](#3-1072-게임)
4. [1300 K번째 수](#4-1300-K번째-수)
5. [2805 나무 자르기](#5-2805-나무-자르기)
6. [2470 두 용액](#6-2470-두-용액)
7. [12015 가장 긴 증가하는 부분 수열2](#7-12015-가장-긴-증가하는-부분-수열2)
8. [17393 다이나믹 롤러](#8-17393-다이나믹-롤러)
9. [1654 랜선 자르기](#9-1654-랜선-자르기)
10. [1477 휴게소 세우기](#10-1477-휴게소-세우기)
11. [8983 사냥꾼](#11-8983-사냥꾼)
12. [11977 Angry cows](#12-11977-Angry-cows)

## 1. [2343 기타레슨](https://www.acmicpc.net/problem/2343)
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

## 5. [2805 나무 자르기](https://www.acmicpc.net/problem/2805)
![image](https://user-images.githubusercontent.com/44918665/128623621-b0a3e464-f9c5-4d99-b20c-fac48eac98f1.png)


### 5.1. 문제유형
- Binary Search

### 5.2. 자료구조
- left (int): 가장 작은 트리의 높이
- right (int): 가장 높은 트리의 높이
- mid (int): 트리의 중간 높이

### 5.3. 해결과정
- ⭐ **실수한 점) 트리의 높이가 최대여야 나무를 가장 적게 가져간다.**
- 따라서, 자른 나무 길이가 M보다 작을 경우 right의 크기를 감소시킨다.
- 반대로 자른 나무 길이가 M보다 클 경우, left 크기를 증가시켜 나무를 절약한다.
- ⭐ **list(tree-mid for tree in trees if tree-mid>0)으로 계산한 뒤, sum 계산 시 시간 초과가 발생했다.**
- 따라서 바로 sum(tree-mid for tree in trees if tree-mid>0)으로 계산해주니 바로 통과했다.

1. left, right로부터 mid를 계산 후 자른 나무 길이를 계산한다.
2. 자른 나무 길이가 m보다 작으면 right = mid-1로 높이를 낮춘다.
3. 자른 나무 길이가 m보다 크면 left = mid+1로 높이를 높이고 answer = mid를 저장한다.

```python
n, m = map(int, input().split())
trees = list(map(int, input().split()))

left, right = 1, max(trees)
answer = 0

while left <= right:
    mid = (left+right)//2
    cuts = sum(tree-mid for tree in trees if tree-mid>0)

    if cuts < m:
        right = mid-1
    else:
        left = mid+1
        answer = mid

print(answer)
```

## 6. [2470 두 용액](https://www.acmicpc.net/problem/2470)
![image](https://user-images.githubusercontent.com/44918665/128623641-01916bb6-d509-4331-a54e-c49691b9644d.png)


### 6.1. 문제유형
- Binary Search
- Two Pointer

### 6.2. 자료구조
- l (int): 첫 번째 원소 인덱스
- r (int): 마지막 원소 인덱스
- flag (boolean): 탐색 여부를 결정하는 변수

### 6.3. 해결과정
- 시작하기 전, 정렬을 수행한다.
1. 만약 첫 번째 값과 마지막 값이 모두 양수라면, 가장 작은 두 값을 출력한다.
2. 만약 첫 번째 값과 마지막 값이 모두 음수라면, 가장 큰 두 값을 출력한다.
3. 만약 첫 번째 값과 마지막 값의 부호가 다르다면, 탐색을 수행한다.
4. 탐색과정은 flag and l < r동안 반복한다.
5. sum의 절대값이 answer 값보다 작다면 answer에 sum을 저장하고, a,b = l,r를 저장한다.
6. sum이 0보다 작다면 용해값을 키우기 위해 왼쪽값을 증가시킨다.
7. sum이 0보다 크다면 용해값을 감소시키기 위해 오른쪽값을 감소시킨다.

```python
n = int(input())
liq = list(map(int, input().split()))
liq.sort()
l, r = 0, n-1
flag = False
a, b, answer = 0, 0, 1000000001

if liq[l]<0 and liq[r]<0:
    print(liq[-2], liq[-1])
    exit()
elif liq[l]>0 and liq[r] >0:
    print(liq[0], liq[1])
    exit()
else:
    flag=True

while flag and l<r:    
    sum = liq[l]+liq[r]
    if abs(sum) < answer:
        answer = abs(sum)
        a = l
        b = r
    if sum < 0:
        l += 1
    else:
        r -= 1
    
print(liq[a], liq[b])
```

## 7. [12015 가장 긴 증가하는 부분 수열2](https://www.acmicpc.net/problem/12015)
![image](https://user-images.githubusercontent.com/44918665/128661023-e4d6b00d-be07-4c6f-a30d-4c9cb176da21.png)


### 7.1. 문제유형
- Binary Search, DP

### 7.2. 자료구조
- lis (list): 최장 부분 순열을 저장하는 리스트
- a (int): n개의 입력값을 저장하는 리스트

### 7.3. 해결과정
1. 입력받은 값을 a에서 하나씩 꺼낸다.
2. lis가 비어 있으면 꺼낸 값을 추가한다.
3. 비어있지 않고, lis[-1] < num이면 꺼낸 값을 추가한다.
4. 꺼낸 값이 lis의 마지막 값보다 작으면 이분탐색으로 들어갈 index를 찾고 덮어씌운다.
5. 반복이 끝나면 lis의 길이를 출력한다.

```python
import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
lis = []

for num in a:
    if not lis:
        lis.append(num)
        continue
    if lis[-1] < num:
        lis.append(num)    
    else:
        index = bisect_left(lis, num)
        lis[index] = num
print(len(lis))
```

## 8. [17393 다이나믹 롤러](https://www.acmicpc.net/problem/17393)
![image](https://user-images.githubusercontent.com/44918665/128661428-d281a5cf-1d6e-4ab8-bdfb-cefc6242d47a.png)


### 8.1. 문제유형
- Binary Search

### 8.2. 자료구조
- ink (list): 잉크를 저장하는 리스트
- vis (list): 점도를 저장하는 리스트
- answer (list): 각 자리에서 최대 칠할 수 있는 타일 수를 저장하는 리스트
- pos (int): 현재 타일 위치의 잉크값
- l (int): 현재 위치의 바로 앞 타일 위치를 저장
- r (int): 타일의 가장 끝 위치를 저장
- mid (int): l,r의 중간값
- res (int): 현재 위치에서 칠할 수 있는 최대 타일 위치

### 8.3. 해결과정
- 아이디어는 현재 위치 ink값보다 작은값들 중 최대값의 위치를 찾는다.
- 현재 위치 + 1 부터 ink값보다 작은 최대값 위치까지의 값을 카운트한다.
- 이 거리가 현재 위치에서부터 칠할 수 있는 타일 수가 된다.

1. i=0부터 n-1까지 반복문을 돌며 각 자리에서 칠할 수 있는 타일 수를 카운트한다.
2. 현재 위치 i를 기준으로 l,r을 정의한 후 l <= r일 동알 반복문을 돌며 타일 수를 카운트한다.
3. 현재 잉크값보다 mid의 점도가 크다면 칠할 수 없다. r = mid-1
4. 현재 잉크값보다 mid의 점도가 작거나 같다면 칠할 수 있다. l = mid+1, res = mid 저장
5. 반복문이 끝난 후, i+1부터 res까지의 타일 수를 count한다. = res - (i+1) + 1
6. 각 위치별 칠할 수 있는 타일 개수를 출력한다.

```python
import sys

n = int(input())
ink = list(map(int, sys.stdin.readline().split()))
vis = list(map(int, sys.stdin.readline().split()))
answer = []

for i in range(n):
    pos = ink[i]
    l, r = i+1, n-1
    res = i

    while l <= r:
        mid = (l+r)//2
        if pos < vis[mid]:
            r = mid-1
        else:
            l = mid+1
            res = mid
    answer.append(str(res-(i+1)+1))
print(' '.join(answer))
```
