## [1.2573 빙산 ](https://www.acmicpc.net/problem/2573)

![ice](https://user-images.githubusercontent.com/87264787/129874724-90c47164-fd9e-473f-a40d-8621635af4c9.png)

### 1.1 풀이 과정

1.  덩어리 갯수 = bfs or dfs 탐색(특히 상하좌우 탐색확률 높음) // 빙하 녹는이는것 // 이렇게 2가지 구현이 필요하다고 생각

1.  melted 함수를 통해 시간이 지나 빙하가 녹아서 카운트갯수를 조정해주는 것 구현

1.  count 함수를 통해 bfs탐색을하여 덩어리 갯수가 몇개인지판단 => 탐색2번일시 2개의 덩어리

1.  그이후 좌표계의 빙하가 있는 모든점에대해 mleted 함수를 적용해준다 (빙하가 줄어들거나 없어짐)

1. 이때 좌표게를 수정해준후 카운트 함수를 통해 갯수를 판단해준다 (이때 처음에 visited 함수가 이미 쓰여졌으므로 초기화 필요)





### 1.2 자료구조

1.  bfs/dfs = while,for문을 많이 사용할꺼같아서 bfs 채택

1.  단순 bfs가 아니라 특정조건 + bfs 문제이기 때문에 세부조건들을 더 많이 신경써 줘야된다..

### 1.3 소스 코드

```python


#2573 빙산
#bfs 특징 - > 좌표계에서 대각선 신경 x

#문제풀이 1:  첫번째로 좌표계를 통해 녹는거 구현
#2 . 그상황에서 빙산의 덩어리 판단하는 함수구현


import sys 
from collections import deque

#기본 선언문 + 입출력

input =sys.stdin.readline
N,M = map(int,input().rstrip().split())
ice = [list(map(int,input().rstrip().split())) for _ in range(N)]
visited = [[0]*M for _ in range(M)]
melt = deque()
year = 0

# 상하좌우 + melted 구현

dx = [-1, 1 , 0 ,0]
dy = [0, 0, -1, 1]

def melted(x,y):
    a = 0
    for i in range(4):
        nx =x + dx[i]
        ny =y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if ice[nx][ny] == 0:
                a += 1
    if ice[x][y] <= a:
        ice[x][y] = -1  #-1로 해주는 이유는 0으로할시 다음 녹은 빙하계산시 포함되기때문에 -1로 해준후
        melt.append((x,y))   # 뒤에 년도가 지날때 다시 0으로 수정해서 구현
    else:
        ice[x][y] -= a

def bfs(x,y):
    visited[x][y] = 1
    arr = deque()   #조금이라도 시간단축
    arr.append((x,y))

    while arr:
        a,b = arr.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 0 and ice[nx][ny] != 0:
                    visited[nx][ny] = visited[a][b] + 1
                    arr.append((nx, ny))

def count():
    cnt = 0
    for i in range(N):
        for j in range(M):
            if ice[i][j] != 0 and visited[i][j] == 0:
                bfs(i,j)
                cnt += 1
    return cnt

a = count()  #visited 함수 이미 한번사용

#print(a)

while a ==1:
#녹는것 구현
    for i in range(N):
        for j in range(M):
            if ice[i][j] != 0:
                melted(i,j)
#좌표계 수정
    while melt:
        l,r = melt.popleft()
        ice[l][r] = 0
# 초기화 + 년도 올려주기    
    visited = [[0]*M for _ in range(N)]
    year += 1
    a =count

if a ==0:
    year = 0

print(year)



```


### 1.4 한줄평

- 좌표계 + 상하좌우 = bfs,dfs 구조가 너무 알맞게 생기는 거 같음

- 조건이 많아질수록 함수구조를 알맞은 구조로 사용하는것이 구현하기 편함
