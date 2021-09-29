# Divide_and_conquer

1. [1588 수열](#1-1588-수열)
2. [17829 222 풀링](#2-17829-222-풀링)
3. [2447 별 찍기 10](#3-2447-별-찍기-10)
4. [2448 별 찍기 11](#4-2448-별-찍기-11)
5. 2339 석판 자르기
6. [1074 Z](#6-1074-Z)
7. [2630 색종이 만들기](#7-2630-색종이-만들기)
8. [4256 트리](#8-4256-트리)
9. 5904 moo 게임
10. [2374 같은수로 만들기](#10-2374-같은수로-만들기)

## 1. [1588 수열](https://www.acmicpc.net/problem/1588)
![image](https://user-images.githubusercontent.com/44918665/134519475-35939059-20f0-4c39-87d9-e4928ab590d4.png)

### 1.1. 문제유형
- 분할 정복
- 재귀

### 1.2. 풀이과정
1. 치환을 반복하는 과정을 재귀로 구현하되 3가지 경우를 고려한다.
2. 종료조건 : start ~ end가 범위를 벗어난 경우
3. start ~ end가 해당 범위를 포함하는 경우
4. start ~ end가 특정 구간으로, 전부 구할 필요가 없는 경우
5. 4번의 경우 sec초마다 치환 수행시마다 start, end값을 start-length//3*i, end-length//3*i로 줄여나간다.
6. 5번이 끝난 결과에서 각각 1의 개수, 2의 개수, 3의 개수를 더해나간다.

### 1.3. 소스코드
```python
def get_count(x, sec, start, end):
    length = 3**sec # x 변환한 길이 계산 
    # 종료 조건: 범위 안에 수가 없으면 0리턴
    if length <= start or end < 0:
        return [0, 0, 0]
    
    # 구간이 전체 범위를 포함하는 경우
    # <= : 아직 변환이 완료된 것이 아닐 수 있음
    if start <= 0 and length-1 <= end:
        answer = [0, 0, 0]
        answer[x-1] += 1 # 시작값 + 1
        for i in range(sec): # sec초만큼 변환
            temp = answer[:]
            answer[0] = temp[0]+temp[1]*2
            answer[1] = temp[0]+temp[1]+temp[2]*2
            answer[2] = temp[0]+temp[2]
        return answer # length 전부를 계산해서 반환

    # 구간을 전부 계산할 필요가 없는 경우 [특정 구간으로 주어짐]
    changed = ((1, 3, 2), (2, 1, 1), (2, 3, 2)) # 1,2,3 변환
    answer = [0, 0, 0]
    for i in range(3): # sec-1 : 1번 변환 수행
        part = get_count(changed[x-1][i], sec-1, start-length/3*i, end-length/3*i)
        for j in range(3):
            answer[j] += part[j]
    
    return answer

x=int(input())
start=int(input())
end=int(input())
n=int(input())
print(' '.join(map(str, get_count(x, n, start, end))))
```

### 1.4. 노트필기
![image](https://user-images.githubusercontent.com/44918665/134519682-92653aa7-0bf4-4a4c-a943-180b13255bf1.png)

## 2. [17829 222 풀링](https://www.acmicpc.net/problem/17829)
![image](https://user-images.githubusercontent.com/44918665/134519326-4ccc44f6-ee0f-4b93-8057-021c79fbcd0c.png)
![image](https://user-images.githubusercontent.com/44918665/134519370-29aa42fa-e81a-4614-a5d2-953d2ffa291a.png)

### 2.1. 문제유형
- 분할 정복

### 2.2. 해결과정
1. length를 절반으로 줄인 2차원 배열 생성한다.
2. (0,0)부터 2칸씩 건너 뛰며 줄인 2차원 배열에 값을 채워넣는다.
3. 채워 넣는 값을 (0,0)부터 아래, 오른, 대각 방향값 중 2번째 큰 값이다.
4. 최종적으로 1x1 배열이 남으면 출력한다.
5. 해당 문제는 O(logn)로 복잡도가 감소한다.

### 2.3. 소스코드
```python
import math

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

def pooling(graph):
    length = len(graph)
    l = length//2
    res = [[0]*l for _ in range(l)]
    nx = 0
    for x in range(0, length, 2):
        ny = 0
        for y in range(0, length, 2):
            window = [graph[x][y], graph[x+1][y], graph[x][y+1], graph[x+1][y+1]]
            window.sort(reverse=True)
            res[nx][ny] = window[1]
            ny += 1
        nx += 1
    
    return res

def solve():
    answer = graph

    for _ in range(int(math.log2(n))):
        answer = pooling(answer)
    
    return answer[0][0]

print(solve())
```

## 3. 2447 별 찍기 10
![image](https://user-images.githubusercontent.com/44918665/134821686-f2458ee9-f3b4-400e-98b6-2b9fc95e21bf.png)
![image](https://user-images.githubusercontent.com/44918665/134821691-504d1d69-06ba-4e84-9029-430ec0887f8b.png)

### 3.1. 문제유형
- 분할정복, 재귀

### 3.2. 해결과정
1. 최소 단위(3x3)를 설정하고 반복해서 찍어나간다.
2. 첫 행과 마지막 행은 찍히는 구조가 같다.
3. 가운데 행은 최소 단위 + 공백 + 최소단위로 구성된다.

### 3.3. 소스코드
```python
import sys
sys.setrecursionlimit(10**6)


def print_star(length):
    if length == 1:
        return ['*']
    
    stars = print_star(length//3)
    tmp = []

    for s in stars:
        tmp.append(s*3)
    for s in stars:
        tmp.append(s+' '*(length//3)+s)
    for s in stars:
        tmp.append(s*3)
    
    return tmp

n = int(input())
for s in print_star(n):
    print(s)
```

## 4. 2448 별 찍기 11
![image](https://user-images.githubusercontent.com/44918665/134824593-342475e5-93ab-4ffb-a0a6-64d246ff152b.png)

### 4.1. 문제유형
- 분할정복, 재귀

### 4.2. 해결과정
1. n = 3*2^k이므로 별을 찍기 위해 k를 계산해야한다.
2. k를 계산한 후 3^k만큼 삼각형을 찍는다.

### 4.3. 소스코드
```python
n=int(input())
star = ['  *  ', ' * * ', '*****']
n = n//3

cnt = 0
while n > 1:
    n = n//2
    cnt += 1

def print_star(star):
    length = len(star)
    for i in range(length):
        star.append(star[i] + ' ' + star[i])
        star[i] = ' '*length + star[i] + ' '*length
    
    return star

for i in range(cnt):
    star = print_star(star)

for s in star:
    print(s)
```

## 6. [1074 Z](https://www.acmicpc.net/problem/1074)
![image](https://user-images.githubusercontent.com/44918665/135071511-375c29a0-0d63-43e0-8871-fd49a88595b9.png)
![image](https://user-images.githubusercontent.com/44918665/135071594-1d258418-e08f-4170-b9f3-81527e3de2c6.png)

### 6.1. 문제유형
- 분할 정복, 재귀

### 6.2. 해결과정
- 배열을 선언한 뒤 0부터 적어나갔더니 메모리 초과 발생
- 배열 대신 딕셔너리를 사용했으나, 시간초과 발생
- 해당 문제는 하나씩 카운트하지 않고 어느 사분면에 속하는 지를 빨리 파악해야했다.

### 6.3. 소스코드
```python
# 시간초과 or 메모리 초과
# def visit(length, x, y):
#     global answer
#     if length > 2:
#         visit(length//2, x, y)
#         visit(length//2, x, y+length//2)
#         visit(length//2, x+length//2, y)
#         visit(length//2, x+length//2, y+length//2)
#     else:
#         res[(x,y)] = answer; answer+=1
#         res[(x,y+1)] = answer; answer+=1
#         res[(x+1,y)] = answer; answer+=1
#         res[(x+1,y+1)] = answer; answer+=1

n, r, c = map(int, input().split())
answer = 0

while n > 1:
    size = (2**n) // 2
    if r < size and c < size:
        pass
    elif r < size and c >= size:
        answer += size ** 2
        c -= size
    elif r >= size and c < size:
        answer += size ** 2 * 2
        r -= size
    elif r >= size and c >= size:
        answer += size ** 2 * 3
        r -= size
        c -= size
    n -= 1

if r==0 and c==0:
    print(answer)
elif r==0 and c==1:
    print(answer+1)
elif r==1 and c==0:
    print(answer+2)
elif r==1 and c==1:
    print(answer+3)
```

## 7. [2630 색종이 만들기](https://www.acmicpc.net/problem)
![image](https://user-images.githubusercontent.com/44918665/135072177-d52ed04a-e85f-44b2-858c-82f9b0787323.png)
![image](https://user-images.githubusercontent.com/44918665/135072242-4354ce94-8328-42a4-aed3-f7a08d9b0c05.png)

### 7.1. 문제유형
- 분할정복, 재귀

### 7.2. 해결과정
1. length를 제곱한 값과 절단한 색종이 1 개수로 비교하던 중 더 좋은 방법을 찾았다.
2. 분할 기준이 되는 (x,y)값 색종이 색깔을 기록한다.
3. 기록한 색깔부터 색종이를 탐색하며 다른 값을 만날 경우 분할한다.
4. 만약 다른 색깔을 만나지 않았다면 for문을 빠져나온 뒤 0이면 0개수 증가, 1이면 1개수 증가
5. 최종적으로 0과 1의 개수를 출력한다.

### 7.3. 소스코드
```python
import sys
input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
answer = []

def check(x, y, length):
    color = paper[x][y]
    for i in range(x, x+length):
        for j in range(y, y+length):
            if color != paper[i][j]:
                length = length//2
                check(x, y, length)
                check(x, y+length, length)
                check(x+length, y, length)
                check(x+length, y+length, length)
                return 0
    if color == 0:
        answer.append(0)
    else:
        answer.append(1)

check(0,0,n)
print(answer.count(0))
print(answer.count(1))
```

## 8. [4256 트리](https://www.acmicpc.net/problem/4256)
![image](https://user-images.githubusercontent.com/44918665/135073469-df6d27be-1610-41fc-bd00-5dace64ea45a.png)
![image](https://user-images.githubusercontent.com/44918665/135073555-14b815f7-8cda-4ac6-9555-fc0d9670839a.png)
![image](https://user-images.githubusercontent.com/44918665/135073585-d37776c1-2bc6-483d-b279-7e2f5c438503.png)

### 8.1. 문제유형
- 분할정복, 재귀, 트리

### 8.2. 해결과정
- 아래 소스코드는 블로그를 참고하여 해결했다.
![image](https://user-images.githubusercontent.com/44918665/135073748-149aa2ea-442b-4936-bf61-1a79dc02f074.png)
- 인사이트는 전위순회 노드를 기준으로 중위순회 시, 왼쪽서브트리와 오른쪽서브트리로 나뉜다는 것이다.
- 따라서 왼쪽서브트리를 start~ i까지, 오른쪽서브트리를 i+1~ end까지 재귀적으로 탐색한다.
- 후위 순회 결과를 출력할 것이므로 마지막에 preorder 노드를 출력한다.

### 8.3. 소스코드
- https://jjangsungwon.tistory.com/94
```python
import sys
input = sys.stdin.readline

def solve(root, start, end):
    for i in range(start, end):
        if inorder[i] == preorder[root]:
            solve(root+1, start, i)
            solve(root+i+1-start, i+1, end)
            print(preorder[root], end=" ")

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    solve(0, 0, n)
    print("")
```

## 10. [2374 같은 수로 만들기](https://www.acmicpc.net/problem/2374)
![image](https://user-images.githubusercontent.com/44918665/135258873-52ee9f21-ef94-42d2-bd15-e19b7d28bc75.png)

### 10.1. 문제유형
- 분할정복
- 자료구조
- 그리디 알고리즘
- 스택

### 10.2. 해결과정
1. 값을 1개씩 입력받으며 현재까지의 가장 큰 값의 차이를 저장한다.
2. stack이 비어있다면 구한 차이값을 삽입한다.
3. stack이 차 있고, top 값이 입력받은 값보다 작다면 그 차이를 최종값 cnt에 더하고 pop 후 입력값 삽입
4. stack이 차 있고, top 값이 입력받은 값보다 크다면 차이는 더하지 않고, stack을 pop하고 입력값 삽입
5. stack에 들어 있는 값을 하나씩 꺼내고, 최종값 cnt에 최대값과 꺼낸 값의 차를 더해 나간다.

### 10.3. 소스코드
```python
import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
stack = []

max_num = 0

for i in range(n):
    t = int(input())
    max_num = max(max_num, t)
    if not stack:
        stack.append(t)
    else:
        if stack[-1] < t:
            cnt += t - stack[-1]
            stack.pop()
            stack.append(t)
        elif stack[-1] > t:
            stack.pop()
            stack.append(t)
    
while stack:
    num = stack[-1]
    stack.pop()
    cnt += max_num - num
    
print(cnt)
```
