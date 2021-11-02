나동빈님의 '이것이 코딩테스트다.'를 참고하여 필요한 부분만 따로 정리하였습니다.

## 복수의 특정 값 삭제하기

    1. Python에서 리스트 삭제 시 복잡도는 O(N)이다.
    2. 삭제 후 리스트 원소 위치를 조정하기 때문이다.
    3. 따라서 여러 개 값은 삭제한다면, 복잡도는 O(N*logN)이다.

> 리스트 컴프리헨션을 활용해 O(N)으로 모든 특정값을 삭제할 수 있다.

```python
a=[1,2,3,4,5,5,5]
remove_set={3,5}

result = [i for i in a if i not in remove_set]
print(result)
```

## 튜플 자료형

### 튜플 자료형의 특징과 시간복잡도

    1. 튜플은 그래프 알고리즘 구현 시 자주 사용된다.
    2. 다익스트라 최단 경로 알고리즘처럼 최단 경로를 찾아주는 알고리즘
    3. 다익스트라 알고리즘의 경우 우선순위 큐를 사용하며, 한 번 들어간 값을 변경되지 않는다.

### 튜플의 장점, 관례

    1. 튜플은 리스트에 비해 공간을 적게 사용한다.
    2. 다익스트라에서 (비용, 노드번호)의 형태로 묶어서 사용하는 것이 관례이다.
    3. 튜플은 서로 성질이 다를 때 주로 사용한다. ex) 비용 vs 노드 번호

## 딕셔너리 자료형

    1. key-value 관계를 이용해 데이터 검색, 수정 복잡도가 O(1)이다.
    2. 해시 테이블을 사용해 리스트보다 훨씬 빠르게 동작한다.

> 사전 자료형에 특정한 원소가 있는지 원소 in 사전 형태로 검색할 수 있다.

```python
data=dict()
data['사과']='Apple'
data['바나나']='Banana'
data['코코넛']='Coconut'

if '사과' in data:
    print("'사과'가 존재합니다.")
```

## SET 자료형
리스트, 튜플은 순서가 존재했기에 인덱싱을 통해 접근할 수 있다. Set 자료형은 값만 존재한다.

    1. 중복을 허용하지 않는다.
    2. 순서가 없다.
    3. set은 |(합), &(교), -(차) 연산이 가능하다.

> set은 특정 데이터가 이미 등장한 적이 있는지 체크할 때 매우 효과적이다.

```python
a=set([1,2,3,4,5])
b=set([3,4,5,6,7])

print(a|b) # 합집합
print(a&b) # 교집합
print(a-b) # 차집합
```

### set 내장함수
add(), remove()는 모두 시간복잡도가 O(1)이다.

    1. add(): 1개 값 추가
    2. update(): 여러 개 값 한번에 추가
    3. remove(): 값 삭제

## 조건부 표현식
if ~ else를 한 줄에 적을 수 있다.
```python
score = 85

if score >= 80: result = "Success"
else: result = "Fail"


result = "Success" if score >= 80 else "Fail"
print(result)
```

리스트에서 특정값을 삭제할 경우 유용하다.
```python
a=[1,2,3,4,5,5,5]
remove_set={3,5}

result=[]
for i in a:
    if i not in remove_set:
        result.append(i)

print(result)
```

하지만 조건부 표현식을 사용하면 다음과 같이 줄일 수 있다.
```python
a=[1,2,3,4,5,5,5]
remove_set={3,5}

result=[i for i in a if i not in remove_set]
print(result)
```

## 중첩 반복문
> 2중 for문의 경우 플로이드 워셜 알고리즘, DP에서 많이 사용된다.

## 함수

1. 함수 내부에서 외부 변수를 변경할 경우 global 키워드로 지정한다.

```python
a=0

def func():
    global a
    a += 1

for i in range(10):
    func()
print(a)
```
2. 람다 표현식을 사용하면 함수를 한 줄에 정의할 수 있다.

```python
print((lambda a, b: a+b)(3, 7))
```

## 주요 라이브러리

    1. itertools: combinations, permutations 라이브러리 제공
    2. heapq: 우선순위 큐 기능을 구현하기 위한 heap
    3. bisect: 이진탐색 기능 제공
    4. collections: deque, Counter, defaultdict 등 제공

## 주요 함수

1. eval() 함수
```python
result=eval("3(3+5)*7")
print(result)
```

2. sorted() 함수
```python
result=sorted([9,1,8,5,4])
print(result)
result=sorted([9,1,8,5,4], reverse=True)
print(result)
result=sorted([('홍길동',35), ('이순신',75), ('아무개',50)], key=lambda x:x[1], reverse=True)
```

3. permutations
```python
from itertools import permutations

data=['A','B','C']
result=list(permutations(data,3))
print(result)
```

4. combinations

```python
from itertools import combinations

data=['A','B','C']
result=list(combinations(data,2))
print(result)
```

5. heapq
- heapq는 다익스트라 최단 경로 알고리즘에 사용된다.
- 또한, 우선순위 기능이 필요한 경우 사용된다.

    1. heapq.heappush(): 원소 삽입
    2. heapq.heappop(): 원소 Pop

```python
import heapq # python 기준 default는 최소힙이다.

def heapsort(iterable):
    h=[]
    result=[]
    # 원소 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 원소 꺼내서 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result=heapsort([1,3,5,7,9,2,4,6,8,0])

def max_heapsort(iterable):
    h=[]
    result=[]
    # 원소 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    # 힙에 삽입된 원소 꺼내서 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

print(result)
```

6. bisect
- bisect_left(), bisect_right() 모두 들어갈 인덱스를 반환한다.
- right_index - left_index: 범위값
    1. bisect_left(a, x): 왼쪽 인덱스 반환
    2. bisect_right(a, x): 오른쪽 인덱스 반환

```python
from bisect import bisect_left, bisect_right

a=[1,2,4,4,8]
x=4

print(bisect_left(a,x)) # 2
print(bisect_right(a,x)) # 4
```

> 정렬된 리스트에서 특정 범위에 속하는 원소 개수 구하기 효과적이다. 
- ex) right_index-left_index

```python
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터 개수 구하기
def count_by_range(a, left_value, right_value):
    right_index=bisect_right(a, right_value)
    left_index=bisect_left(a, left_value)
    return right_index-left_index
```

7. deque

    1. deque.popleft(): 왼쪽 pop
    2. deque.pop(): 오른쪽 pop
    3. deque.append(): 오른쪽 삽입
    4. deque.appendleft(): 왼쪽 삽입
> deque는 앞뒤 원소 추가, 삭제 모두 복잡도가 O(1)이다.

8. Counter
- collections 라이브러리의 Counter는 등장 횟수를 세는 기능을 한다.

```python
from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue']) # blue가 등장한 횟수 출력
print(counter['green']) # green이 등장한 횟수 출력
print(dict(counter)) # 딕셔너리로 변환: {'red':2, 'blue':3, 'green':1}
```

> 리스트와 같은 iterable 객체가 주어졌을 때, 객체 내 원소가 몇 번 등장했는지 카운트한다.
> Counter함수 사용 후, 딕셔너리로 변환할 수 있다.

