# 문제풀이

## 1. [9375 패션왕 신해빈](https://www.acmicpc.net/problem/9375)
![image](https://user-images.githubusercontent.com/44918665/128104252-4b750df2-7947-4269-a066-2c06d786e84b.png)
### 1.1. 문제유형
- set, map

### 1.2. 자료구조
- data (dictionary) (key:의상종류, value:의상이름): 의상 종류와 이름을 저장하는 딕셔너리

### 1.3. 해결과정
1. 옷을 입을 수 있는 모든 경우의 수를 구하되, 알몸인 경우를 제외하는 것이 핵심이다.
2. 따라서 (의상종류별 개수+1)한 값을 누적해서 곱해나간 뒤 1을 감소시킨다.
```python
test = int(input())

for _ in range(test):
    data = dict()
    n = int(input())
    cnt = 1

    for _ in range(n):
        name, kind = input().split()
        if kind not in data.keys():
            name = [name]
            data[kind] = name
        else:
            data[kind].append(name)
    for k, v in data.items(): 
        cnt *= len(v)+1
    
    print(cnt-1)
```


## 2. [12906 새로운 하노이 탑](https://www.acmicpc.net/problem/12906)
![image](https://user-images.githubusercontent.com/44918665/128094901-3afb562e-3f60-4c8c-919d-e7fa19d1c3e4.png)

### 2.1. 문제유형
- set, map
- bfs
- queue

### 2.2. 자료구조
1. q (queue) : 방문할 하노이 탑을 담는 Queue 자료구조
2. visited (set) : 이미 방문한 하노이 탑을 담는 Set 자료구조
3. count (int) : 이동횟수를 저장한 

### 2.3. 해결과정
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

## 3. [13414 수강신청](https://www.acmicpc.net/problem/13414)
![image](https://user-images.githubusercontent.com/44918665/128093704-31eaa8da-7c3e-4490-8698-440e04efc7e0.png)
![image](https://user-images.githubusercontent.com/44918665/128093726-c7b0f105-54a0-4453-8d95-81ed352b1f1b.png)

### 3.1. 문제유형
- set, map
1. 처음에 수강신청 대기열을 떠올리며 Queue로 문제를 해결하려고 시도했다. 
2. 하지만 시간초과로 통과하지 못했고 그 이유는 다음과 같다.
3. 시간제한 1초, 입력 최대길이가 500,000이므로 Queue 연산과정에 소요되는 Overhead가 크다.

### 3.2. 자료구조
- success (dictionary) (key:학번, value:순서번호): 학번과 순서를 저장한 딕셔너리
- order (int) : 수강신청 순서번호를 의미하는 변수
- cnt (int) : 수강정원을 count하는 변수

### 3.3. 해결과정
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

## 4. [4195 친구 네트워크](https://www.acmicpc.net/problem/4195)

![image](https://user-images.githubusercontent.com/44918665/127806849-d560dcb7-45ec-477d-8ffa-2c7df6a64ee9.png)


### 4.1. 문제유형
- Disjoint set(Union find), dictionary(set/map)

### 4.2. 자료구조
parent (dictionary) : 친구 관계를 저장하는 dictionary
number (dictionary) : 친구 관계 그래프의 개수를 저장하는 dictionary

### 4.3. 함수
1. getParent(x): x의 부모노드를 반환하는 재귀 함수
2. unionParent(x, y): x, y의 부모노드를 찾아 병합하는 함수

### 4.4. 해결과정
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


## 4. [1302 베스트셀러](https://www.acmicpc.net/problem/1302)
![image](https://user-images.githubusercontent.com/44918665/127806860-5ee2083b-4a38-4d5b-9215-dd4c0172e225.png)

### 4.1. 해결과정
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

## [프로그래머스 해시 - 전화번호 목록](https://programmers.co.kr/learn/courses/30/lessons/42577)
![image](https://user-images.githubusercontent.com/44918665/132112708-5b17c69e-0077-4b7f-aa12-27015839a7ac.png)

### 1. 문제유형
- hash map

### 2. 해결과정
- 크게 3가지 풀이방법이 존재했다.
1. 2중 for문을 활용하는 방법
2. 문자열 내장함수 startswith를 사용한 방법
3. hash를 활용한 방법

- 결론적으로 1번 방법은 시간복잡도가 O(N^2)이므로 효율성 문제를 통과할 수 없다. 
- 따라서 2번과 3번을 활용한 풀이가 가능하다.

### 3. 소스코드
```python
def solution1(phone_book):
    answer = True
    phone_book = sorted(phone_book, key=len)
    
    for n1 in phone_book:
        for n2 in phone_book:
            if n1 == n2[:len(n1)] and n1 != n2:
                answer = False
                return answer
    
    return answer

def solution2(phone_book):
    phone_book.sort()
    
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    
    return True


from collections import defaultdict
def solution3(phone_book):
    hash_map = defaultdict(int)
    
    for p in phone_book:
        hash_map[p] += 1
    
    for phone_number in phone_book:
        tmp = ''
        for t in phone_number:
            tmp += t
            if tmp in hash_map.keys() and tmp != phone_number:
                return False
    
    return True
```

### 4. Dictionary vs List
- 3번째 풀이에서 tmp를 hash_map에 존재하는 지 탐색하는 과정에서 의문이 생겼다.
- 어쨋든 저장된 개수는 최대 100만개인데, List에서는 시간초과가 났다.
- https://www.jessicayung.com/python-lists-vs-dictionaries-the-space-time-tradeoff/

![image](https://user-images.githubusercontent.com/44918665/132113220-92d5df02-6589-4f05-99dc-0d51daab0757.png)
- Then why not always use dictionaries? Looking up entries in Python dictionaries is fast, but dicts use a lot of memory.* This is a classic example of a space-time tradeoff. Update: From Python 3.6, dictionaries don’t use that much space. So it’s not even a space-time tradeoff any more.) Why is looking up entries in a dictionary so much faster? It’s because of the way Python implements dictionaries using hash tables. Dictionaries are Python’s built-in mapping type and so have also been highly optimised. Sets are implemented in a similar way.
- 해당 링크의 글을 참고하자면, 기존 딕셔너리는 리스트에 비해 더 빠른 탐색이 가능하나 메모리 공간을 많이 차지하는 문제가 있었다. 따라서 space-time tradeoff 관계에 있었으나, Python 3.6 버전 업데이트 후로는 메모리 사용량도 감소하여 상충관계에서 벗어난 것으로 보인다. Dictionary는 List보다 탐색속도가 빠른 이유는 Hash Table로 구성된 자료구조이기 때문이다.

## 프로그래머스 해시 - 위장
![image](https://user-images.githubusercontent.com/44918665/132113824-e4783f8b-4c55-40e2-803e-3759d97624bf.png)

### 1. 문제유형
- hashmap

### 2. 해결과정
- 경우의 수 문제이므로 각 type별 의상 개수를 구한다.
- 각 type별 의상 개수 + 1을 곱한 값에서 -1 처리를 구한다.
- 의상 개수 + 1을 하는 이유는 해당 의상을 안 입는 경우가 있기 때문이다.
- 결과값에서 -1 처리를 하는 이유는 어떤 의상도 입지 않은 경우를 제거하기 위함이다.

### 3. 소스코드
``` python
from collections import defaultdict
def solution(clothes):
    answer = 1
    hashmap = defaultdict(list)
    
    for name, type in clothes:
        hashmap[type].append(name)
    
    for k, v in hashmap.items():
        answer *= len(v)+1
    
    return answer-1
```

## 프로그래머스 해시 - 베스트앨범
![image](https://user-images.githubusercontent.com/44918665/132327961-c601aee4-62ae-4b68-8794-03177f21f530.png)

### 1. 문제유형
- hashmap

### 2. 해결과정
1.⭐가장 많이 재생된 장르 순서를 구한다.
2. 장르별 인덱스, 재생횟수를 저장한 딕셔너리를 구한다.
3.⭐2번에서 구한 딕셔너리를 재생횟수를 기준으로 정렬한다.
4. 1번에서 구한 장르별 순서대로 3번에서 구한 인덱스를 2개씩 꺼낸다.

### 3. 소스코드
```python
from collections import defaultdict

def solution(genres, plays):
    answer = []
    gdict = defaultdict(int)
    pdict = defaultdict(list)
    
    for genre,play in zip(genres, plays):
        gdict[genre]+=play
    gdict = sorted(gdict.items(), key=lambda x: x[1], reverse=True)
    gdict = [genre for genre, plays in gdict]
    
    for i in range(len(genres)):
        pdict[genres[i]].append([i, plays[i]])
    
    for i in range(len(genres)):
        pdict[genres[i]] = sorted(pdict[genres[i]], key=lambda x: x[1], reverse=True)
    
    for genre in gdict:
        tmp = pdict[genre][:2]
        for idx, plays in tmp:
            answer.append(idx)
    
    return answer
```
### 4. 노트필기
![image](https://user-images.githubusercontent.com/44918665/132329017-34bd68fe-e0ab-4be0-9628-ec52e9d21365.png)

