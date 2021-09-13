# 10 Week Greedy

1. [1931 회의실 배정](#1-1931-회의실-배정)
2. [13164 행복 유치원](#2-13164-행복-유치원)
3. [1946 신입사원](#3-1946-신입사원)
4. [1339 단어 수학](#4-1339-단어-수학)
5. [17609 회문](#5-17609-회문)
6. [1715 카드 정렬하기](#6-1715-카드-정렬하기)
7. [1826 연료 채우기](#7-1826-연료-채우기)
8. [1911 흙길 보수하기](#8-1911-흙길-보수하기)
9. [1105 팔](#9-1105-팔)
10. [12904 A와 B](#10-12904-A와-B)

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

## 3. [1946 신입사원](https://www.acmicpc.net/problem/1946)
![image](https://user-images.githubusercontent.com/44918665/132843416-348f88df-10ca-4df7-a91e-31423fbe9242.png)

### 3.1. 문제유형
- 그리디, 정렬

### 3.2. 해결과정
- 그리디 문제지만 지원자가 10만명이므로 2중 for문으로 접근 시 10^10 연산 횟수가 필요하다.
- 따라서 O(n^2)이하의 복잡도로 문제를 해결해야 한다.
- 힌트는 서류나 면접점수 둘 중 하나로 정렬하면, 1명은 무조건 합격이라는 것을 알 수 있다.
- 이를 활용하여 서류로 정렬 후 합격자보다 면접점수가 높은 지원자를 카운트한다.
- 이전 합격자보다 면접점수가 높은 지원자가 나오면 면접 점수를 갱신한다.

### 3.3. 소스코드
```python
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    apply = [list(map(int,input().split())) for _ in range(n)]
    apply = sorted(apply)
    answer = 1
    end = apply[0][1]

    for i in range(1, n):
        if end > apply[i][1]:
            end = apply[i][1]
            answer += 1

    print(answer)
```

## 4. [1339 단어 수학](https://www.acmicpc.net/problem/1339)
![image](https://user-images.githubusercontent.com/44918665/132843862-3b1d5bcc-281c-4c34-93fc-2b47d8ba21e0.png)

### 4.1. 문제유형
- 그리디, 브루트포스

### 4.2. 해결과정
1. 좋은 접근 방법은 자리수를 생각하는 것이었다.
2. ABC, BCA인 경우 A와 B중 어디에 더 큰 수를 배정할 지 결정하기 쉽기 때문
3. 따라서 알파벳자릿수를 10의 제곱수를 활용해 알파벳별 합계를 해시맵으로 저장한다.

### 4.3. 소스코드
```python
from collections import defaultdict
n = int(input())
numbers = [list(map(str, input())) for _ in range(n)]

hash=defaultdict(int)
for num in numbers:
    for i in range(len(num)):
        hash[num[i]]+=10**(len(num)-i-1)
hash = sorted(hash.items(), key=lambda x:x[1], reverse=True)

hash_map={}
value = 9
for alpha, _ in hash:
    hash_map[alpha]=value
    value-=1

answer=[]
for num in numbers:
    ans=''
    for alpha in num:
        ans+=str(hash_map[alpha])
    answer.append(int(ans))
print(sum(answer))
```

## 5. [17609 회문](https://www.acmicpc.net/problem/17609)
![image](https://user-images.githubusercontent.com/44918665/133080087-a8c9b951-ea27-438a-8aba-d780ddc3179c.png)

### 5.1. 유형파악
- Greedy
- 그리디 유형은 **정렬과 세트**로 출제된다
- 바로 문제 **유형을 파악하기 어렵다면 그리디**를 의심해볼 것
- 그래도 파악이 어렵다면 DP, Graph 알고리즘을 고려할 것
- 📌 그리디로 해법을 찾을 때는 항상 **정당한 해법인지 의심**해봐야 한다.

### 5.2. 해결과정
1. 문자를 최대 하나 삭제할 수 있으므로 그리디 유형임을 파악.
2. 단, 모든 문자열을 검토할 경우 시간초과 발생.
3. 따라서 유사 회문은 투 포인터 방식으로 구현.
4. 투 포인터로 양 끝에서 같은지 탐색 후, 다를 경우 check_pseudo() 호출.
5. check_pseudo는 왼쪽 삭제, 오른쪽 삭제 2번 호출
6. 왼쪽, 오른쪽 호출된 값 중 하나라도 True라면 1. 아니라면 2 반환

### 5.3. 소스코드
```python
# val == val[::-1]로 바로 체크 시 시간초과 발생
# 유사 회문 검사 시 시간초과, 고로 투 포인터로 구현
# 시간복잡도가 낮은 이유는, 다 비교하지 않더라도 중간에 return할 수 있기 때문

def check_pseudo(val, l, r):
    while l<r:
        # 회문 체크
        if val[l]==val[r]:
            l+=1
            r-=1
        else:
            return False
    return True

def check_answer(val, l, r):
    if val == val[::-1]:
        # 일단 회문체크
        return 0
    else:
        # 유사회문체크
        while l<r:
            if val[l]==val[r]:
                l+=1
                r-=1
            else:
                case1=check_pseudo(val, l+1, r)
                case2=check_pseudo(val, l, r-1)
                if case1 or case2:
                    return 1
                else:
                    return 2

cases = int(input())
for _ in range(cases):
    val = input()
    l, r = 0, len(val)-1
    print(check_answer(val, l, r))
```

## 6. [1715 카드 정렬하기](https://www.acmicpc.net/problem/1715)
![image](https://user-images.githubusercontent.com/44918665/133080830-9e56fa6d-a58b-4bc6-8926-13b44207c864.png)

### 6.1. 유형파악
- 그리디, 정렬, 우선순위 큐
- 📌 정렬과 함께 출제된 그리디 문제.
- 정렬 후, 가장 작은 것부터 더해서 삽입해줘야 하므로 그리디 파악.
- 단, 계산한 값을 넣은 뒤 다시 정렬해야 하므로 리스트 구현 시 시간 초과 발생.
- 따라서 삽입 시 정렬된 상태를 유지해주는 우선순위 큐(힙 자료구조) 사용

### 6.2 해결과정
1. 비교 횟수가 최소가 되려면 작은 것부터 합쳐나가야 한다.
2. 정렬을 수행한 뒤 2개를 꺼내 더하고 다시 넣어준다.
3. 다시 넣어준 결과는 정렬을 유지한 상태여야 한다.
4. 힙 자료구조에 값이 1개가 남을때까지 반복한다

### 6.3. 소스코드
```Python
import heapq
import sys
input = sys.stdin.readline

n = int(input())
data = list(int(input().strip()) for _ in range(n))
total = 0
heapq.heapify(data)
while len(data) != 1:
    a = heapq.heappop(data)
    b = heapq.heappop(data)
    c = a+b
    heapq.heappush(data,c)
    total += c
print(total)
```
