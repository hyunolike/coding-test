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
12. [11977 Angry Cows](#12-11977-Angry-Cows)

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

### 1.4. 소스코드

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


### 2.4. 소스코드

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


### 3.4. 소스코드

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


### 4.4. 소스코드

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


### 5.4. 소스코드

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


### 6.4. 소스코드

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

### 7.4. 소스코드

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

### 8.4. 소스코드

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

## 9. [1654 랜선 자르기](https://www.acmicpc.net/problem/1654)
![image](https://user-images.githubusercontent.com/44918665/128784348-76ab94cc-4dce-4c12-a261-b3326befd825.png)

### 9.1. 문제유형
- 이분탐색, Binary Search

### 9.2. 자료구조
- lans (list): 보유한 랜선의 길이를 저장하는 리스트
- left, right (int): 랜선 최소길이, 최대길이
- mid (int): 지정한 랜선 길이. left, right의 중간값
- cnt (int): 잘라서 얻어낸 랜선 개수

### 9.3. 해결과정
- 최대 랜선 길이가 2^31-1이므로 이분탐색을 떠올렸다.
- 항상 n개의 랜선 개수를 만들 수 있으므로, 랜선 길이를 지정 후 n개가 되는지 테스트한다.
- 최대 범위가 2^31-1인 것을 깜빡해서 1차시도 때 오답으로 책정되었다.
1. left, right를 지정하되 right의 범위는 2^31-1을 포함하도록 설정한다.
2. mid 계산 후 cnt가 n을 만족하는 지 확인한다.
3. cnt가 n보다 작을 경우 너무 크게 잘랐으므로, right = mid-1
4. cnt가 n보다 크거나 작을 경우 너무 작게 잘랐으므로, answer=mid 저장 후 left = mid+1

### 9.4. 소스코드

```python
import sys

k, n = map(int, sys.stdin.readline().split())
lans = list(int(sys.stdin.readline()) for _ in range(k))
left, right, answer = 1, 21470000000, 0

while left <= right:
    mid = (left+right)//2
    cnt = 0

    for l in lans:
        cnt += l//mid
    
    if cnt < n: # 너무 크게 자름
        right = mid-1
    else: # 너무 작게 자름
        left = mid+1
        answer = mid
print(answer)
```

## 10. [1477 휴게소 세우기](https://www.acmicpc.net/problem/1477)
![image](https://user-images.githubusercontent.com/44918665/128801763-cafd179b-7360-4a9d-b4e1-92fad6aec864.png)

### 10.1. 문제유형
- 이분탐색

### 10.2. 자료구조
- distance (int): 도로 최대 길이
- conv (list): 휴게소 위치를 담은 리스트
- left, right (int): 휴게소가 없는 최대거리의 최소값(1), 최대값(distance-1)
- mid (int): 지정한 최대거리의 최소값. left, right의 중간값
- current (int): 현재 위치를 저장할 변수
- diff (int): 현재 위치 - 다음 휴게소 위치로 휴게소가 없는 거리
- cnt (int): 설치한 휴게소 개수

### 10.3. 해결과정
- ⭐ 놓친점) diff가 mid와 같은 경우 휴게소를 설치하지 않아야 한다. (따라서 diff-1을 mid로 나눈다.)
- ⭐ 아이디어) 휴게소가 없는 최대거리의 최소값을 지정하고, 휴게소를 설치를 완료한 뒤 m개인지 비교한다.
1. left, right로부터 mid를 계산 후, 설치할 휴게소 수를 구한다.
2. 반복문을 돌며 diff > current인 경우 휴게소를 설치한다.
3. 이 때 휴게소 수는 (diff-1)//mid 이다. (diff보다 작을 경우 설치 X, 큰 경우 필요한만큼 설치)
4. 휴게소 설치 개수가 m보다 크면, 너무 많이 설치했으므로 간격을 줄인다. right = mid-1
5. 휴게소 설치 개수가 m보다 작거나 같으면, 너무 적게 설치했으므로 간격을 늘린다. left = mid+1

### 10.4. 소스코드

```python
n, m, distance = map(int, input().split())
conv = list(map(int, input().split()))
conv.append(distance)
conv.sort()

left, right = 1, distance-1
answer = 0

while left<=right:
    mid = (left+right)//2
    current, cnt = 0, 0

    for position in conv:
        diff = position - current
        current = position
        if diff > mid: # 최대 거리보다 크므로 지어야함
            cnt += (diff-1)//mid
    if cnt > m: # m보다 많이 지음. 너무 가까이 지음
        left = mid+1
    else: # m보다 작거나 같게 지음. 너무 멀리 지음
        right = mid-1
        answer = mid 
print(answer)
```

## 11. [8983 사냥꾼](https://www.acmicpc.net/problem/8983)
![image](https://user-images.githubusercontent.com/44918665/128991303-6a701950-2377-449f-a636-7755ff7bc7d6.png)
![image](https://user-images.githubusercontent.com/44918665/128991352-611dea42-92c1-4fd1-91cc-c9d3467bce00.png)


### 11.1. 문제유형
- 이분탐색, 정렬

### 11.2. 자료구조
- m (int): 사대의 수
- n (int): 동물의 수
- l (int): 사대 사정거리
- gun (list): 사대 좌표를 담은 리스트
- animal (list): 동물 좌표를 담은 리스트
- cnt (int): 잡은 동물의 수
- s (int): 해당 동물을 잡을 수 있는 최소 사대 좌표
- e (int): 해당 동물을 잡을 수 있는 최대 사대 좌표
- left, right(int): 사대 좌표의 최소값(0), 최대값(m-1) 인덱스
- mid (int): 동물을 잡을 수 있는 사대 좌표값 (left+right)//2

### 11.3. 해결과정
- ⭐ 사대 거리를 고정하고 가능한 동물 수를 구하려고 하면 시간 복잡도가 높아진다. (n^2)
- ⭐ 따라서 동물을 고정하고, 잡을 수 있는 사대가 존재하는 지 확인하는 하는 것이 쉽다. (nlogn)
- ⭐ 동물을 잡을 수 있는 사대 좌표는 s = x+y-l (최소값) ~ e = x-y+l 이다. (l 최대 범위가 크기 때문)
- 사대 좌표를 담은 리스트를 이분탐색할 것이므로 정렬 후 수행한다.
1. x, y좌표별로 s, e를 계산한다.
2. left, right 지정 후 left<=right 동안 mid값이 s와 e 사이에 속하는 지 체크한다.
3. 반복문 조기 종료 조건은 y가 l보다 큰 경우이다. 이 경우 동물을 잡을 수 없다.
4. 해당 구간에 mid가 속한다면 cnt를 증가시킨 후 반복문을 탈출한다.
5. mid가 s보다 작다면 left = mid + 1
6. mid가 s보다 크다면 right = mid - 1

### 11.4. 소스코드

```python
import sys

m, n, l = map(int, input().split())
gun = list(map(int, sys.stdin.readline().split()))
animal = list(map(int, sys.stdin.readline().split()) for _ in range(n))
gun.sort()
cnt = 0

for x, y in animal:
    if (y>l):
        continue
    s = x+y-l
    e = x-y+l
    left, right = 0, m-1
    while left <= right:
        mid = (left+right)//2
        if gun[mid] >= s and gun[mid] <= e:
            cnt += 1
            break
        elif gun[mid] < e:
            left = mid + 1
        else:
            right = mid - 1
print(cnt)
```

## 12. 11977 Angry Cows
![image](https://user-images.githubusercontent.com/44918665/128991449-72097d53-154e-4647-8224-aaafb6eac62a.png)

### 12.1. 문제유형
- 이분탐색, 정렬, 브루트포스

### 12.2. 자료구조
- n (int): 건초의 수
- bay (list): 건초의 위치를 담은 리스트
- cur (int): 현재 건초의 위치 인덱스
- rad (int): 폭발 사정거리
- l (int): 옮겨 붙을 왼쪽 건초 좌표 인덱스
- r (int): 옮겨 붙을 오른쪽 건초 좌표 인덱스
- cnt (int): 폭발시켜 태운 건초의 최대값

### 12.3. 해결과정
- ⭐왼쪽으로 옮겨 붙는 경우와 오른쪽으로 옮겨 붙은 경우를 나누어 구했다.
- ⭐왼쪽으로 옮겨 붙을 때는 터뜨린 가장 왼쪽 건초 index까지 count한 후 rad를 증가시킨다.
- ⭐오른쪽으로 옮겨 붙을 때 역시, 터뜨린 가장 오른쪽 건초 index까지 count한 후 rad를 증가시킨다.
1. 0번째 건초부터 n-1번째 건초까지 아래 과정을 반복한다.
2. l을 현재위치-1로 설정 후왼쪽으로 불태운 건초 개수를 구하는 과정을 반복한다.
3. 반복 종료 조건은 l<0 (더 이상 건초 없음) or bay[cur]-bay[l]>rad (폭발 사정거리 밖)인 경우이다.
4. 반복 종료 조건이 아니라면 l>=0 and bay[cur]-bay[l]<=rad(폭발 사정거리 안 일 경우)동안 cnt 개수를 증가시킨다.
5. 4번 과정이 끝나면 현재 위치를 왼쪽 건초로 이동한 뒤 rad를 1증가시킨다.
6. 오른쪽 건초에 대해서도 2-5과정을 반복한다.

### 12.4. 소스코드

```python
n = int(input())
bay = list(int(input()) for _ in range(n))
bay.sort()

answer = 0

for i in range(n):
    cur, rad = i, 1
    cnt = 1
    l = cur-1

    while True:
        if l < 0 or bay[cur]-bay[l]>rad:
            break
        while l >=0 and bay[cur]-bay[l]<=rad:
            cnt += 1
            l -=1
        cur = l+1
        rad += 1
    
    cur, rad = i,1
    r = cur+1

    while True:
        if r >= n or bay[r]-bay[cur]>rad:
            break
        while r<n and bay[r]-bay[cur] <= rad:
            cnt += 1
            r += 1
        cur = r-1
        rad += 1
    
    answer = max(answer, cnt)
print(answer)
    
```
