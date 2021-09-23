# Divide_and_conquer

1. [1588 수열](#1-1588-수열)
2. [17829 222 풀링](#2-17829-222-풀링)
3. 2447 별 찍기 10
4. 2448 별 찍기 11
5. 2339 석판 자르기
6. 1074 Z
7. 2630 색종이 만들기
8. 4256 트리
9. 5904 moo 게임
10. 2374 같은수로 만들기

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
