# 10 Week Greedy
그리디와 정렬 문제는 세트로 함께 출제된다.
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

## 7. [1826 연료 채우기](https://www.acmicpc.net/problem/1826)
![image](https://user-images.githubusercontent.com/44918665/133387520-b5e742eb-a281-474b-8606-a40e3abcf037.png)

### 7.1. 유형파악
1. Greedy
2. 그리디는 정렬과 같이 나올 확률이 높다.
3. 바로 문제 유형이 보이지 않는다면 그리디를 의심해 볼 것
4. DP, Graph 알고리즘과 함께 나오는 경우도 있다.
5. 그리디 문제는 항상 최적의 해를 구할 수 있는지 의심해봐야 한다.

### 7.2. 해결과정
1. 현재 연료로 도달할 수 있는 주유소를 추린다.
2. 추린 장소 중 가장 멀리 떨어진 주유소로 방문해본다.
3. 해당 주유소에서 주유 후 다시 1-2번을 거친다.
4. 만약 방문할 수 있는 장소가 없다면 -1을 출력한다.

### 7.3. 소스코드
```python
import heapq

n = int(input())
heap = []
for _ in range(n):
    heapq.heappush(heap, list(map(int, input().split())))
end, fuel = map(int, input().split())

cases=[]
cnt=0
while fuel < end:
    while heap and heap[0][0] <= fuel: # 연료로 도달할 수 있는 곳 체크
        place, f = heapq.heappop(heap)
        heapq.heappush(cases, [-1*f, place])
    
    if not cases:
        cnt = -1
        break
    
    f, place = heapq.heappop(cases) # 가장 멀리갈 수 있는 곳 체크
    fuel += -1*f
    cnt += 1

print(cnt)
```

## 8. [1911 흙길 보수하기](https://www.acmicpc.net/problem/1911)
![image](https://user-images.githubusercontent.com/44918665/133389046-a3a237f3-c0f3-40ec-82cd-1b799985c7cd.png)
![image](https://user-images.githubusercontent.com/44918665/133389082-83720be9-f9b2-40ef-9e53-167429421845.png)

### 8.1. 유형파악
1. 그리디
2. 그리디는 정렬과 함께 출제되는 경향
3. 문제 유형 파악이 어려울 시 그리디 의심할 것
4. 종종 DP, Graph 알고리즘과 함께 출제된다.

### 8.2. 해결과정
1. ⭐힌트와 예제를 유심히 볼 것
2. 널빤지는 시작위치를 포함하고, 종료위치는 상관이 없다.
3. 또한 널빤지가 종료 위치를 초과해서 다음 웅덩이를 덮을 수 있다.

### 8.3 소스코드
```python
n, l = map(int, input().split())
pool = [list(map(int, input().split())) for _ in range(n)]
pool.sort()
cnt = 0

for i in range(n):
    st, ed = pool[i]
    if (ed-st) % l != 0:
        length = (ed-st)//l + 1 ## 웅덩이를 다 덮지 못하는 경우 1개를 추가한다.
    else:
        length = (ed-st)//l ## 웅덩이가 딱 맞는 경우

    cnt += length
    new_ed = st + l*length

    if (i+1) < n:
        next_st = pool[i+1][0]
        if new_ed > next_st:    ## 널빤지가 웅덩이를 초과해서 다음 웅덩이까지 덮는 경우
            pool[i+1][0] = new_ed
print(cnt)
```

## 9. [1105 팔](https://www.acmicpc.net/problem/1105)
![image](https://user-images.githubusercontent.com/44918665/133390061-83356f29-7777-4439-b347-704a2c3d70fc.png)
![image](https://user-images.githubusercontent.com/44918665/133390019-cf9ed66b-8a4b-4948-b6f0-a37c86df54cd.png)

### 9.1. 유형파악
1. 그리디
2. 그리디 유형은 정렬과 함께 출제될 확률이 높다.
3. 문제 유형을 한 번에 파악하기 어려울 경우 그리디를 의심해볼 것
4. 종종 DP, Graph 알고리즘과 함께 출제된다.
5. 그리디는 반드시 최적의 해를 구할 수 있는 지 의심해봐야한다.

### 9.2. 해결과정
1. 주어진 l, r 사이에서 8을 가장 적게 포함하는 횟수를 구하는 문제이다.
2. 수의 범위가 20억이므로, 순차탐색으로 해결할 수 없다.
3. 8의 최소 개수만 세면 된다는 것에 초점을 맞춰 풀어야한다.
4. l과 r의 첫번째 자리수부터 비교하되 일치하면서 8이라면 개수를 카운트하고, 다르다면 stop한다.
    - 만약 자리수의 값이 다르다면, (8이 아닌 다른값으로 설정해버리면 개수가 0이된다.)
    - 바로 stop하는 이유는, 이미 앞 자리수가 다르므로 뒷자리는 다양한 값(0~9)을 가질 수 있다.

### 9.3. 소스코드
```python
l, r = map(str, input().split())

answer = 0

if len(l)!=len(r):
    print(0)
    exit(0)

for i in range(len(l)):
    if l[i]==r[i]:
        if l[i]=='8':
            answer += 1
    else:
        break
print(answer)
```

## 10. [12904 A와 B](https://www.acmicpc.net/problem/12904)
![image](https://user-images.githubusercontent.com/44918665/133392021-db52fd55-10dc-4f5f-acc7-58c4496f3cc7.png)
![image](https://user-images.githubusercontent.com/44918665/133392081-7f230626-4399-4868-8779-f0202cff45ca.png)

### 10.1. 유형파악
1. 문자열, 그리디, 구현
2. 그리디 + 정렬 유형이 많다는 걸 인지할 것
3. 문제 유형 파악이 어려울 시 그리디 고려할 것
4. DP, Graph와 함께 나오는 경우도 있음을 인지할 것
5. 그리디로 풀이할 시 반드시 최적의 해를 구할 수 있는지 고려할 것

### 10.2. 해결과정
1. 이 문제는 S -> T로 가는 경우의 수를 계산하면 어렵다.
2. S가 T가 될 수 있는 지 확인하는 걸 뒤집어서 접근하면 쉽다.
3. T가 S가 될 수 있는 지 규칙 1, 규칙 2를 뒤집어서 적용해서 해결했다.

### 10.3. 소스코드
```python
s = input()
t = input()
s, t = list(s), list(t)

for i in range(len(t)-1, -1, -1):
    if t==s:
        print(1)
        exit(0)
    elif t[i]=='A':
        t.pop()
    else:
        t.pop()
        t = t[::-1]
print(0)
```


