# [10주] [Greedy] 발표자료
1. [1826 연료 채우기](#1-1826-연료-채우기)
2. [12904 A와 B](#2-12904-A와-B)
## 1. [1825 연료 채우기](https://www.acmicpc.net/problem/1826)
![2021-09-12](https://user-images.githubusercontent.com/69501435/132987359-4449b02b-ca68-4408-a88a-9f1ede275445.png)



### 1.1 자료구조
1. heap ( heapq.heap() 우선순위 큐 )

### 1.2 풀이과정
1. 현재 갈 수 있는 곳 중에서 기름을 가장 많이 채울 수 있는곳을 안지나고 최소의 루트로 목적지에 도달하는 법은 존재 하지 않는다. 이것이 핵심이다.
2. 즉 지금 위치에서 갈 수 있는 곳을 우선순위 큐에 넣는데 기준을 가장 기름을 많이주는 즉 - fuel을 key로 줬다 (-fuel을 기준으로 오름차순은 fuel이 큰거부터 우선순위큐로 저장된다)
3. 그래서 돌다가 만약 기름의 양이 가야하는 거리보다 커지면 루프를 탈출하고 출력 해줄 수 있도록 하였다.

### 1.3 소스코드

```python
import sys
import heapq

def sol(n,stations,l,p):
    stations.sort(reverse=True)
    heap = []

    count = 0

    while p<l:
        while stations and stations[-1][0] <= p:
            dist, fuel = stations.pop()
            heapq.heappush(heap, -fuel)
        if not heap:
            break
        p -=heapq.heappop(heap)
        count+=1
    if l<=p:
        return count
    return -1

n = int(sys.stdin.readline())

stations = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

goal, gas = map(int,sys.stdin.readline().split())

print(sol(n,stations,goal,gas))


```

(현재 갈 수 있는 곳 중에서 기름을 가장 많이 채울 수 있는곳을 안지나고 최소의 루트로 목적지에 도달하는 법은 존재 하지 않는다. 의 증명)
![KakaoTalk_20210912_213708724](https://user-images.githubusercontent.com/69501435/132987848-16fb03fc-05be-43fb-9b97-1b7365ae8f70.jpg)


## 2. [12904 A와 B](https://www.acmicpc.net/problem/12904)
![2021-09-15](https://user-images.githubusercontent.com/69501435/133377256-35b2406f-6513-4062-9862-ec61254442f8.png)


### 2.1 자료구조
1. alpha (dict()) : 지금 현재 있는 문자열의 'A'의 개수와 'B'의 개수를 저장 (S,T에 대한)

### 2.2 풀이과정
1. 우선 우리가 목표로 가야할 S의 'A', 'B'의 개수를 저장해두고
2. 우리가 변화시킬 T의 'A','B'의 개수를 저장시켜 둡니다.
3. 그리고 총 S의 문자열의 개수와 T의 문자열의 개수가 같아질때까지 for 문을 돌도록하며
4. 마지막 문자열에 따른 규칙을 적용합니다.
5. 'A' 일 경우 그저 T의 'A'의 개수를 1감소시키는 행위
6. 'B' 일 경우 T의 'B'의 개수를 감소 시킬뿐만 아니라 처음부터 지금 index전까지 swap하는 과정이 필요하다.
7. 이 반복문을 도는 도중에 만약 이번에 빼야할 알파벳이 뺄 수 없는 경우 즉 이미 alpha_s와 alpha_t의 개수가 같은 경우 만들 수 없으므로 out
8. 이 모든 과정을 거쳐서 나왔으면 각각 index별 원소 접근하여 맞는지 확인

### 2.3 소스코드

```python
import sys

lst = [list(sys.stdin.readline().strip()) for _ in range(2)]
alpha_s = dict()
alpha_s['A'] = lst[0].count('A')
alpha_s['B'] = lst[0].count('B')

alpha_t = dict()
alpha_t['A'] = lst[1].count('A')
alpha_t['B'] = lst[1].count('B')




for i in reversed(range(len(lst[0]), len(lst[1]))):
    if alpha_s[lst[1][i]] == alpha_t[lst[1][i]]:
        print(0)
        sys.exit()
    if lst[1][i] == 'A':
        alpha_t['A'] -= 1
    else:
        alpha_t['B'] -= 1
        for j in range(i//2):
            lst[1][j] ,lst[1][i-1-j]= lst[1][i-1-j],lst[1][j]
  
for i in range(len(lst[0])):
    if lst[0][i] != lst[1][i]:
        print(0)
        sys.exit()

print(1)


```
