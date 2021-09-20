# Prefix Sum

1. [20438 출석체크](#1-20438-출석체크)
2. [2015 수들의 합4](#2-2015-수들의-합4)
3. [11660 구간 합 구하기 4](#3-11660-구간-합-구하기-4)
4. [3020 개똥벌레](#4-3020-개똥벌레)
5. [21758 꿀 따기](#5-21758-꿀-따기)
6. [2632 피자 판매](#6-2632-피자-판매)
7. [14465 소가 길을 건너간 이유5](#7-14465-소가-길을-건너간-이유5)
8. [5549 행성 탐사](#8-5549-행성-탐사)
9. [20159 동작 그만. 밑장 빼기냐?](#9-20159-동작-그만-밑장-빼기냐)
10. [21318 피아노 체조](#10-21318-피아노-체조)

## 1. [20438 출석체크](https://www.acmicpc.net/problem/20438)
![image](https://user-images.githubusercontent.com/44918665/133621713-e4afe803-b4fc-4845-8403-d1935b5891ef.png)

### 1.1. 문제유형
- 누적합
- 원소별 합계를 구한 후 S[i] - S[i-1]을 활용해 문제를 풀어나간다.

### 1.2. 해결과정
1. 전체 학생 수만큼 배열을 선언한다.
2. 조는 학생을 체크한다.
3. 출석 번호를 체크한다.
4. 0번째부터 n+3까지 출석한 학생들의 누적합을 구한다.
5. 구간 학생 수 - (누적합[구간 마지막값] - 누적합[구간 시작값])

### 1.3. 소스코드
```python
import sys
input = sys.stdin.readline

n,k,q,m = map(int, input().split())

sleep = [0]*(n+3)
check = [0]*(n+3)

for i in map(int, input().split()):
    sleep[i] = 1
for i in map(int, input().split()):
    if sleep[i]: 
        continue
    for j in range(i, n+3, i):
        if not sleep[j]:
            check[j] = 1

prefix = [check[0]]
for i in range(1, n+3):
    prefix.append(prefix[-1]+check[i]) # 각 번호 i까지 출석한 얘들 합 구하기

for _ in range(m):
    s, e = map(int, input().split()) # s부터 e까지 결석한 얘들
    print(e-s+1 - (prefix[e]-prefix[s-1])) # 전체 - (s부터 e까지 출석한 얘들)
```

## 2. [2015 수들의 합4](https://www.acmicpc.net/problem/2015)
![image](https://user-images.githubusercontent.com/44918665/133623056-7bb7ca32-bbd0-47ff-afe9-253a3b90047e.png)

### 2.1. 문제유형
- 누적합
- 각 원소별 누적합을 구하고 S[i]-S[i-1] 이용해 문제를 해결해나간다.

### 2.2. 해결과정
1. 누적합을 계산한다.
2. 누적합 == k인 개수를 카운트한다.
  - 부분 누적합 == k를 함께 찾아 카운트한다.
  - S[i] - S[i-1] = k과 S[i] - k = S[i-1]임을 활용한다.
  - 누적합을 계산하며 S[i] - k를 했을 때 값이 존재하는 경우를 카운트해나간다.

### 2.3. 소스코드
```python
from collections import defaultdict

n, k = map(int, input().split())
nums = list(map(int, input().split()))

cnt = 0
prefix = defaultdict(int)

for i in range(1, len(nums)):
    nums[i] += nums[i-1]

for i in range(len(nums)):
    if nums[i] == k: # 누적합이 k인 경우 카운트
        cnt += 1
    cnt += prefix[nums[i]-k]
    prefix[nums[i]] += 1 # 누적합이 nums[i]가 되는 경우

print(cnt)
```

## 3. [11660 구간 합 구하기 5](https://www.acmicpc.net/problem/11660)
![image](https://user-images.githubusercontent.com/44918665/133878264-73f4a440-5019-4f4e-a8ea-adb41a15e681.png)

### 3.1. 문제유형
- 누적합

### 3.2. 풀이과정
1. 매 번 2중 for문을 계산할 시 시간초과가 발생할 것이다.
2. 따라서 미리 누적합을 계산해 놓고, 구간별로 뽑아 리턴한다.
3. 이 때, col 인덱스번호가 0이라면 종료값의 누적합을 덧셈한다.
4. 시작 인덱스가 0이 아니라면 종료값 - 시작값을 덧셈한다.
5. python 시간 초과 발생 -> pypy3로 통과

### 3.3. 소스코드
```python
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

nums = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(1, n):
        nums[i][j] += nums[i][j-1]

for _ in range(k):
    xy = list(map(int, input().split()))
    sx, sy = xy[0]-1, xy[1]-1
    ex, ey = xy[2]-1, xy[3]-1

    total = 0

    for i in range(sx, ex+1):
        if sy == 0:
            total += nums[i][ey]
        else:
            total += (nums[i][ey]-nums[i][sy-1])
    print(total)
```

## 4. [3020 개똥벌레](https://www.acmicpc.net/problem/3020)
![image](https://user-images.githubusercontent.com/44918665/133878432-3cdd6e5b-5340-48bd-879a-4cbe6881ba67.png)
![image](https://user-images.githubusercontent.com/44918665/133878423-4f632561-69f2-4316-9848-36f8f45d1bfb.png)


### 4.1. 문제유형
- 누적합

### 4.2. 풀이과정
1. 석순은 아래, 종유석은 위에 위치한다.
2. 석순 높이는 그대로 사용하되, 종유석 높이는 (전체 - 종유석) 높이를 사용한다.
3. 석순과 종유석을 정렬 후, 이분탐색을 이용해 들어갈 높이별 장애물개수를 찾는다.
4. 핵심은 석순/종유석 탐색에는 이분탐색, 전체 높이는 순차탐색을 활용한다

### 4.3. 소스코드
```python
import sys
input = sys.stdin.readline

def bs_search(height, cave):
    l, r = 0, len(cave)-1
    while l<=r:
        mid = (l+r)//2
        if cave[mid]<=height:
            l = mid+1
        else:
            r = mid-1
    
    return len(cave) - (r+1)

n, h = map(int, input().split())
top, bottom = [], []

for i in range(n):
    rock = int(input())
    if i%2 == 0:
        top.append(rock)
    else:
        bottom.append(rock)

top.sort()
bottom.sort()

rock_cnt, range_cnt = 1e10, 0

for i in range(1, h+1):
    top_cnt = bs_search(i-1, top)
    bottom_cnt = bs_search(h-i, bottom)
    cnt = top_cnt + bottom_cnt

    if cnt < rock_cnt:
        rock_cnt = cnt
        range_cnt = 1
    elif cnt == rock_cnt:
        range_cnt += 1
    else:
        pass
print(rock_cnt, range_cnt)
```

## 5. [21758 꿀 따기](https://www.acmicpc.net/problem/21758)
![image](https://user-images.githubusercontent.com/44918665/133971200-852a5388-7821-4ae1-8bc3-b1047086a552.png)
![image](https://user-images.githubusercontent.com/44918665/133971231-57c18997-0234-4d66-85e7-cb7128488a17.png)

### 5.1. 문제유형
- 누적합

### 5.2. 풀이과정
1. 누적합을 구한 후 꿀통의 위치를 기준으로 3가지 경우에 대해 각 10만번 연산을 수행하였다.
2. 첫 번째는 꿀통이 오른쪽에 있는 경우
    - 벌 한 마리는 가장 왼쪽에 위치
4. 두 번째는 꿀통이 왼쪽에 있는 경우
    - 벌 한마리는 가장 오른쪽에 위치
6. 세 번째는 꿀통이 중간에 있는 경우
    - 이 경우는 양 끝에 벌들이 위치한다.
8. 누적합만 계산해 놓으면 2,3,4를 loop를 돌며 계산할 수 있으므로 O(N)에 해결할 수 있다.

### 5.3. 소스코드
```python
from copy import deepcopy

n=int(input())
h=list(map(int, input().split()))
s = deepcopy(h)
answer=0

for i in range(1, n):
    s[i] += s[i-1]

for i in range(1, n-1): # 오른쪽
    answer = max(answer, 2*s[-1]-h[0]-h[i]-s[i])
for i in range(1, n-1): # 왼쪽
    answer = max(answer, s[-1]-h[-1]-h[i]+s[i-1])
for i in range(1, n-1): # 중간
    answer = max(answer, s[i]-h[0] + s[-1]-s[i-1]-h[-1])

print(answer)
```

## 6. [2632 피자판매](https://www.acmicpc.net/problem/2632)
![image](https://user-images.githubusercontent.com/44918665/133971771-696ff137-a1be-4fc2-94bf-c279c85d86d2.png)
![image](https://user-images.githubusercontent.com/44918665/133971799-ed803a13-ce7e-490d-8c45-c2c4220a5f4f.png)

### 6.1. 문제유형
- 누적합

### 6.2. 해결과정
1. 누적합 결과를 key-value dictionary에 저장 후 경우의 수를 카운트한다.
2. 두 피자의 0번째 누적합은 1이다. (한 쪽의 피자로만 줄 수 있는 경우 존재)
3. 피자는 원판이므로, 0번째부터 n-1번째까지 돌며 가능한 피자 조각 경우를 카운트한다.
4. A, B 피자 총합의 누적합 개수는 1개로 수정한다.
    - 원판을 돌며 중복된 개수 예외처리
5. A, B 개별로 피자 개수를 카운트 한 후, 합쳐서 target이 되는 경우를 카운트한다.
6. 이 때, 경우의 수이므로 가능한 A의 개수 * 가능한 B의 개수로 누적해나간다.
    - ex) 7을 만들 때, (A,B) = (4,3) 일 때, (4를 만드는 경우의 수)x(3을 만드는 경우의 수)로 계산되어야함

### 6.3. 소스코드
```python
import sys
input = sys.stdin.readline

target = int(input())
m, n =map(int, input().split())
A = [int(input()) for _ in range(m)]
B = [int(input()) for _ in range(n)]

A_sum, B_sum = [0]*2000001, [0]*2000001
A_sum[0] = B_sum[0] = 1
A_len, B_len = len(A), len(B)

for i in range(A_len):
    s = 0

    for j in range(A_len):
        s += A[(i+j)%m]

        if s>target:
            break
        else:
            A_sum[s]+=1

for i in range(B_len):
    s = 0
    for j in range(B_len):
        s += B[(i+j)%n]
        if s>target:
            break
        else:
            B_sum[s]+=1

A_sum[sum(A)] = B_sum[sum(B)] = 1

ans=0
for i in range(target+1):
    ans += (A_sum[i]*B_sum[target-i])
print(ans)
```

### 6.4. 노트필기
![KakaoTalk_20210920_162550061](https://user-images.githubusercontent.com/44918665/133972544-ffa9670d-4ced-4d09-b71d-6b7e7b52b279.png)

- 참고한 블로그
https://goodsosbva.tistory.com/81

## 9. 20159 동작 그만. 밑장 빼기냐?
