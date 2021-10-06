# Two Pointer

1. [22114 창영이와 점프](#1-22114-창영이와-점프)
2. [7453 합이 0인 네 정수](#2-7453-합이-0인-네-정수)
3. 16161 가장 긴 증가하는 팰린드롬 부분수열
4. [20922 겹치는 건 싫어](#4-20922-겹치는-건-싫어)
5. [2003 수들의 합 2](#5-2003-수들의-합-2)
6. [1806 부분합](#6-1806-부분합)
7. [22862 가장 긴 짝수 연속한 부분 수열(large)](#7-22862-가장-긴-짝수-연속한-부분-수열(large))
8. [22945 팀 빌딩](#8-22945-팀-빌딩)
9. [2531 회전 초밥](#9-2531-회전-초밥)
10. [2230 수 고르기](#10-2230-수-고르기)

## 1. [22114 창영이와 점프](https://www.acmicpc.net/problem/22114)
![image](https://user-images.githubusercontent.com/44918665/135942246-1b2554eb-c7ff-4dbb-bc63-bd5598c76491.png)
![image](https://user-images.githubusercontent.com/44918665/135942302-28c36f8a-599a-49a1-bb42-f0a4ce2fa60f.png)
![image](https://user-images.githubusercontent.com/44918665/135942321-0098edd3-0f9f-4753-9280-944c53e2f458.png)

### 1.1. 문제유형
- 두 포인터

### 1.2. 해결과정
1. 거리가 k 이하면 r, cnt를 증가시킨다.
2. 거리가 k 이상이면 jump하고 r, cnt를 증가시킨다.
3. jump를 이미 했다면 l++, cnt--를 반복하며 점프한 구간을 배제한다.
4. jump한 구간을 삭제하고 새롭게 r, cnt를 증가시킨다.
5. loop마다 answer에 cnt 최대값을 누적한다.

### 1.3. 소스코드
```python
import sys
input = sys.stdin.readline

n,k=map(int, input().split())
brick=list(map(int, input().split()))
l, r = 0, 0
answer, cnt = 1,1
jump=1
while True:
    if l >= n-1 or r >= n-1:
        break
    if brick[r]<=k:
        cnt += 1
        r += 1
    elif brick[r]>k:
        if jump:
            jump -= 1
            cnt += 1
            r += 1
        else:
            while brick[l]<=k:
                l += 1
                cnt -= 1
            if brick[l]>k:
                l += 1
                cnt -= 1
            r += 1
            cnt += 1
    answer = max(answer, cnt)
print(answer)
```

## 2. [7453 합이 0인 네 정수](https://www.acmicpc.net/problem/7453)
![image](https://user-images.githubusercontent.com/44918665/135942811-701f2b92-f3fc-45d4-9963-d1928034736f.png)
![image](https://user-images.githubusercontent.com/44918665/135942834-54e993aa-7dc3-498e-a8e9-397f42cb36b5.png)

### 2.1. 문제유형
- 두 포인터

### 2.2. 해결과정
1. sum(a,b,c,d) = 0이면 sum(a,b) + sum(c,d) = 0이다.
2. 따라서 a+b값을 구한 후, -(c+d)과 같은 쌍의 개수를 찾는다.

### 2.3. 소스코드
```python
import sys
input = sys.stdin.readline

n=int(input())
A,B,C,D=[],[],[],[]
for _ in range(n):
    a,b,c,d = map(int,input().split())
    A.append(a); B.append(b); C.append(c); D.append(d)

answer = 0
AB,CD = {},{}
for a in A:
    for b in B:
        # 딕셔너리 get: key에 해당하는 value 리턴, 없을 시 None
        # get(key, default): 만약 리턴 시 None이 아닌 default 반환
        AB[a+b] = AB.get(a+b, 0)+1
for c in C:
    for d in D:
        # 현재 -(c,d)에 해당하는 (a,b)가 있다면 카운트
        answer += AB.get(-(c+d), 0)
print(answer)
```

## 3. 16161 가장 긴 증가하는 팰린드롬 부분수열

## 4. [20922 겹치는 건 싫어](https://www.acmicpc.net/20922)
![image](https://user-images.githubusercontent.com/44918665/135946000-386b7e86-c999-4532-821c-1aeab2544eca.png)
![image](https://user-images.githubusercontent.com/44918665/135946019-12b5f435-9d72-4e9c-8c83-ea0e90a56e89.png)

### 4.1. 문제유형
- 두 포인터

### 4.2. 해결과정
1. 중복된 개수를 카운트하는 check[0] * 100001배열을 선언한다.
2. check[a[r]] < k라면 r++, cnt++, check[a[r]]++
3. k보다 작다면, check[a[r]]>=k일 동안 check[a[l]],l++,cnt--
4. 3번 후 다시 r++, cnt++, check[a[r]]++
5. loop마다 answer에 최대값을 누적해나간다.

### 4.3. 소스코드
```python
import sys
input = sys.stdin.readline

n,k=map(int,input().split())
a=list(map(int,input().split()))
l,r=0,0
answer,cnt=0,0
check=[0]*100001

while True:
    if l>=n or r>=n:
        break
    if check[a[r]]<k:
        check[a[r]]+=1
        cnt+=1
        r+=1
    else:
        while check[a[r]]>=k:
            check[a[l]]-=1
            l+=1
            cnt-=1
        check[a[r]]+=1
        cnt+=1
        r+=1
    answer = max(answer, cnt)
print(answer)
```

## 5. [2003 수들의 합 2](https:/www.acmicpc.net/problem/2003)
![image](https://user-images.githubusercontent.com/44918665/136126212-2c501993-ac0c-4b26-ab84-bdecf30b88ae.png)

### 5.1. 문제유형
- 두 포인터

### 5.2. 해결과정
1. total+a[r], r++를 반복한다.
2. total >= m이라면 total>=m일 동안 total-a[l], l++ 수행
3. l >= n이거나 r >= n이면 종료한다.

### 5.3. 소스코드
```python
# version1
n, m=map(int,input().split())
a=list(map(int,input().split()))
l,r=0,0
answer=0
total=0

while True:
    if l>=n or r>=n:
        break
    total += a[r]
    r+=1
    while total>=m:
        if total==m:
            answer+=1
        total-=a[l]
        l+=1
print(answer)

## version2
n, m = map(int, input().split())
a = list(map(int, input().split()))
answer = 0

# m보다 커지면 left를 하나 증가, 작으면 right 하나 증가
left,total=0,0
for i in range(len(a)):
    total+=a[i]
    while total>=m:
        if total==m:
            answer += 1
        total -= a[left]
        left+=1
print(answer)
```

## 6. [1806 부분합](https://www.acmicpc.net/1806)
![image](https://user-images.githubusercontent.com/44918665/136126816-7651c57e-51d1-4bdb-b2c3-89fa5c00d76e.png)

### 6.1. 문제유형
- 두 포인터

### 6.2. 해결과정
1. total+=s[r], length++, r++를 수행한다.
2. total >= m이라면, answer=min(answer, length)를 수행하고 total-=s[l], length--, l++ 수행
3. 만약 answer값이 초기값 그대로라면 answer=0

### 6.3. 소스코드
```pythonn,m=map(int,input().split())
s=list(map(int,input().split()))
answer=1e8
l,r=0,0
total=0
length=0
while True:
    if l>=n or r>=n:
        break
    total+=s[r]
    length+=1
    r+=1
    while total >= m:
        if total >= m:
            answer = min(answer, length)
        total -= s[l]
        length-=1
        l+=1
if answer==1e8:
    answer=0
print(answer)
```

## 7. [22862 가장 긴 짝수 연속한 부분 수열(large)](https://www.acmicpc.net/22862)
![image](https://user-images.githubusercontent.com/44918665/136127110-68104bd2-6f16-4564-93e7-d9c311d7f00c.png)
![image](https://user-images.githubusercontent.com/44918665/136127127-b9f8046e-eadc-4a9b-86ca-3e1a1e4fc954.png)

### 7.1. 문제유형
- 두 포인터

### 7.2. 해결과정
1. s[r]%2==0이라면 cnt++, r++를 수행한다.
2. s[r]%2==1이라면 홀수이므로, 삭제 가능한지 불가능한 지 if 분기.
3. 삭제가 가능하다면 r++, del_cnt--
4. 삭제가 불가능하다면 while s[l]%2==0일동안 cnt--,l++
5. l을 증가시키며 홀수에 도달했다면 cnt--,l++
6. 홀수인 것을 추가한다. cnt++, r++
7. 1-6과정 수행 후 answer=max(answer,cnt)

### 7.3. 소스코드
```python
n,k=map(int,input().split())
s=list(map(int,input().split()))
answer,cnt=0,0
del_cnt=k
l,r=0,0

while True:
    if l>=n or r>=n:
        break
    if s[r]%2==0: #짝수
        cnt += 1
        r+=1
    else: #홀수
        if del_cnt: # 삭제 가능
            r+=1
            del_cnt-=1
        else: # 삭제 불가능
            while s[l]%2==0: #짝수일동안
                cnt-=1
                l+=1
            if s[l]%2==1: # 홀수인것삭제
                cnt-=1
                l+=1
            cnt+=1 # 홀수인것추가
            r+=1
    answer=max(answer,cnt)
print(answer)
```

## 8. [22945 팀 빌딩](https://www.acmicpc.net/problem/22945)
![image](https://user-images.githubusercontent.com/44918665/136135379-5b742302-1c16-41e8-a541-e8c5954c7ebe.png)
![image](https://user-images.githubusercontent.com/44918665/136135402-f483b95d-124d-4b42-876f-3b04eff05e52.png)

### 8.1. 문제유형
- 두 포인터

### 8.2. 해결과정
1. 최대가 되려면 두 포인터 간 거리가 최대값, 두 포인터 값이 최대값이어야한다.
2. 따라서 l,r=0,n-1부터 값을 계산해나간다.
3. dev[l] > dev[r]라면 r--, 반대라면 l++를 반복하며 능력치 계산.
4. l >= r이라면 1-3 loop를 종료한다.

### 8.3. 소스코드
```python
n=int(input())
dev=list(map(int,input().split()))
answer,total=0,0
l,r=0,n-1

while True:
    if l>=r:
        break
    people=r-l-1
    ability=min(dev[l],dev[r])
    total=people*ability
    answer=max(answer,total)
    
    if dev[l]>dev[r]:
        r-=1
    else:
        l+=1
print(answer)
```

## 9. 2531 회전 초밥
![image](https://user-images.githubusercontent.com/44918665/136140473-f8c03311-faef-4058-ba95-7b8f1dc4a51c.png)
![image](https://user-images.githubusercontent.com/44918665/136140499-08c2cf10-ebce-4181-9c83-908c1a897331.png)

### 9.1. 문제유형
- 두 포인터

### 9.2. 해결과정
1. 스시판이 돌아가므로 원순열을 고려한 idx=i%n, 최대값은 n+k-1
2. 용량이 k인 접시 위에 하나씩 스시 추가하며 cnt++
3. 접시가 꽉 찼을 때, 쿠폰 c가 접시에 없다면 answer=max(answer,cnt+1)
4. 쿠폰 c가 접시에 있다면 answer=max(answer,cnt)
5. 3,4번 후 가장 먼저 들어온 스시 제거. 제거한 스시가 접시에 또 있다면 pass. 없다면 cnt--
6. 추가할 스시가 접시에 없다면 추가 후 cnt++

### 9.3. 소스코드
```python
import sys
input = sys.stdin.readline
from collections import deque

n,d,k,c=map(int,input().split())
susi=list(int(input()) for _ in range(n))
answer,cnt=0,0
q=deque()

for i in range(n+k):
    idx=i%n
    if len(q)==k:
        if c not in q:
            answer=max(answer,cnt+1)
        else:
            answer=max(answer,cnt)
        remov=q.popleft()
        if remov not in q:
            cnt-=1
    if susi[idx] not in q:
        cnt+=1
    q.append(susi[idx])
print(answer)
```

## 10. 2230 수 고르기
![image](https://user-images.githubusercontent.com/44918665/136143369-8e5eaae6-13e1-4226-8943-973b8cfb3144.png)
![image](https://user-images.githubusercontent.com/44918665/136143382-52ced501-1499-45eb-8af3-91f0428fe6ce.png)

### 10.1. 문제유형
- 두 포인터
- 정렬

### 10.2. 해결과정
1. l,r 선택 시 가장 차이가 작은 두 값을 골라야 하므로 정렬한다.
2. l,r=0,1 시작 후 diff를 계산한 후 m보다 큰 지 판단한다.
3. diff >= m 이라면, answer=min(answer,diff), l++
4. diff < m 이라면, r++

### 10.3. 소스코드
```python
import sys
input = sys.stdin.readline

n,m=map(int,input().split())
a=list(int(input()) for _ in range(n))
a.sort()
answer=2e9
l,r=0,1

while True:
    if l>=n or r>=n:
        break
    diff=a[r]-a[l]
    if diff>=m:
        answer=min(answer,diff)
        l+=1
    else:
        r+=1
print(answer)
```
