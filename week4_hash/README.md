# 문제풀이

## [12906 새로운 하노이 탑](https://www.acmicpc.net/problem/12906)
![image](https://user-images.githubusercontent.com/44918665/128094901-3afb562e-3f60-4c8c-919d-e7fa19d1c3e4.png)

### 📌문제유형
- set, map
- bfs
- queue

### 📌자료구조
1. q (queue) : 방문할 하노이 탑을 담는 Queue 자료구조
2. visited (set) : 이미 방문한 하노이 탑을 담는 Set 자료구조
3. count (int) : 이동횟수를 저장한 

### 📌해결과정
1. queue에 각 막대별 처음 원판 상태와 이동횟수를 tuple로 저장한다.
2. q가 존재할 동안 다음 loop를 반복한다.
3. q를 꺼낸 후 A,B,C 막대 상태를 조합해 방문상태를 의미하는 문자열을 생성한다.
4. A막대에는 A만, B막대에는 B만, C막대에는 C만 존재하면 이동횟수 출력 후 종료한다.
5. 방문하지 않은 상태라면 아래의 하노이 탑 과정을 수행한다.
6. A막대 원판이 존재한다면, A의 마지막 원판을 b로 이동한 경우, c로 이동한 경우를 q에 저장
7. B막대 원판이 존재한다면, B의 마지막 원판을 c로 이동한 경우, a로 이동한 경우를 q에 저장
8. C막대 원판이 존재한다면, C의 마지막 원판을 b로 이동한 경우, a로 이동한 경우를 q에 저장

```Python
from collections import deque

visited = set()
q = deque()

a = input().split()
s1 = a[-1] if len(a)>1 else ''
a = input().split()
s2 = a[-1] if len(a)>1 else ''
a = input().split()
s3 = a[-1] if len(a)>1 else ''

q.append((s1, s2, s3, 0))

while q:
    a, b, c, count = q.popleft()
    cont_str = a + '/' + b + '/' + c

    if a=='A'*len(a) and b=='B'*len(b) and c=='C'*len(c):
        print(count)
        break

    if cont_str not in visited:
        visited.add(cont_str)

        if len(a)>0:
            q.append((a[:-1], b+a[-1], c, count+1))
            q.append((a[:-1], b, c+a[-1], count+1))
        if len(b)>0:
            q.append((a, b[:-1], c+b[-1], count+1))
            q.append((a+b[-1], b[:-1], c, count+1))
        if len(c)>0:
            q.append((a, b+c[-1], c[:-1], count+1))
            q.append((a+c[-1], b, c[:-1], count+1))

```

## [13414 수강신청](https://www.acmicpc.net/problem/13414)
![image](https://user-images.githubusercontent.com/44918665/128093704-31eaa8da-7c3e-4490-8698-440e04efc7e0.png)
![image](https://user-images.githubusercontent.com/44918665/128093726-c7b0f105-54a0-4453-8d95-81ed352b1f1b.png)

### 📌문제유형
- set, map
1. 처음에 수강신청 대기열을 떠올리며 Queue로 문제를 해결하려고 시도했다. 
2. 하지만 시간초과로 통과하지 못했고 그 이유는 다음과 같다.
3. 시간제한 1초, 입력 최대길이가 500,000이므로 Queue 연산과정에 소요되는 Overhead가 크다.

### 📌자료구조
- success (dictionary) (key:학번, value:순서번호): 학번과 순서를 저장한 딕셔너리
- order (int) : 수강신청 순서번호를 의미하는 변수
- cnt (int) : 수강정원을 count하는 변수

### 📌해결과정
1. 수강인원 k, 클릭 대기목록 수 l을 입력받는다.
2. 대기목록을 입력 받으며 딕셔너리에 key는 입력받은 학번, value는 순서번호 order를 저장한다. 
3. 입력이 끝난 후 딕셔너리를 order에 따라 정렬한다.
4. 작은 order 순으로 학번을 출력하고, cnt 개수가 수강정원 k에 도달하면 종료한다.

```Python
import sys
import operator

k, l = map(int, input().split())
success = dict()
order = 1

for _ in range(l):
    student = sys.stdin.readline().strip()
    success[student] = order
    order += 1

success = sorted(success.items(), key = operator.itemgetter(1))

cnt = 0
for key, value in success:
    if cnt == k:
        break
    print(key)
    cnt+=1
```

## [4195 친구 네트워크](https://www.acmicpc.net/problem/4195)

![image](https://user-images.githubusercontent.com/44918665/127806849-d560dcb7-45ec-477d-8ffa-2c7df6a64ee9.png)


### 📌문제유형
- Disjoint set(Union find), dictionary(set/map)

### 📌자료구조
parent (dictionary) : 친구 관계를 저장하는 dictionary
number (dictionary) : 친구 관계 그래프의 개수를 저장하는 dictionary

### 📌함수
1. getParent(x): x의 부모노드를 반환하는 재귀 함수
2. unionParent(x, y): x, y의 부모노드를 찾아 병합하는 함수

### 📌해결과정
1. 입력받은 x, y 친구를 그래프 그룹에 추가하고, 개수를 증가시킨다.
2. x, y의 부모노드를 받아온 뒤 한 부모 노드를 갖도록 합친다.
3. 합쳐진 부모 노드의 그래프 총 개수를 출력한다.

```Python
import sys

def getParent(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = getParent(parent[x])
        return parent[x]

def unionParent(x, y):
    a = getParent(x)
    b = getParent(y)
    
    if a != b: 
        parent[b] = parent[a]
        number[a] += number[b]

n = int(input())

for _ in range(n):
    parent = dict()
    number = dict()

    f = int(input())

    for _ in range(f):
        x, y = sys.stdin.readline().strip().split()

        if x not in parent:
            parent[x] = x
            number[x] = 1
        if y not in parent:
            parent[y] = y
            number[y] = 1
        
        unionParent(x, y)
        print(number[getParent(x)])
```


## [1302 베스트셀러](https://www.acmicpc.net/problem/1302)
![image](https://user-images.githubusercontent.com/44918665/127806860-5ee2083b-4a38-4d5b-9215-dd4c0172e225.png)

### 📌풀이 과정
1. dictionary에 책 이름을 저장하고, 개수를 카운트한다.
2. dictionary의 values가 최대값인 key를 반환한다.

```Python
import operator

n = int(input())

best = dict()
for _ in range(n):
    book = input()
    if book in best.keys():
        best[book] += 1
    else:
        best[book] = 1
    
result = [k for k,v in best.items() if v == max(best.values())]
result.sort()
print(result[0])
```
