## [1.16234 인구이동 ](https://www.acmicpc.net/problem/16234)

![trans](https://user-images.githubusercontent.com/87264787/130758929-3647a5dd-671d-4db4-be42-09035472a52b.png)

### 1.1 풀이 과정

1.  다른 좌표계 문제랑 비교해봤을때 가장 큰 차이점 및 포인트는 국경선 개방을 어떻게 구현할지가 포인트

1. 국경선 개방 = 각방향 탐색 --> 조건확인 --> 인구이동 유무/인구수 계산 --> 다음 각방향 탐색

1. 그이후에는 인구이동이 일어날때까지 WHILE문 반복하면 문제해결 완료



### 1.2 자료구조

1.  BFS를 사용 -> 큐 사용

1. 문제풀이 하는데에는 인자가 필요없어서 따로 함수 구현안하고 그냥 풀이

1. people = 좌표계  / visited = 방문했는지 안햇는지 / transfer = 인구수 계산 / arr = bfs구현

### 1.3 소스 코드

```python

import sys
input = sys.stdin.readline
from collections import deque  # 시간단축위해 디큐 사용

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]   
#좌표계 이동 구현

N, L, R = map(int, input().split())
people = []
transfer = []
ans = 0
for _ in range(N):
    people.append(list(map(int, input().split())))
# 좌표계 입력받기

while True:  # 인구이동이 없을때 까지 함수 반복
    Merge = False
    visited = [[False]*(N) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                arr = deque([i,j])
                visited[i][j] = True
                sum = arr[i][j]
                transfer = [[i,j]]
                # 모든 좌표에 대해 실행

                while arr:
                    x,y = arr.popleft()
                    for k in range(4):
                        nx = x+dx[k]
                        ny = y+dy[k]
                        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]: 
                            # 이동 및 조건확인
                            if L <= abs(arr[x][y]-arr[nx][ny]) <= R: # 인구이동 조건
                                visited[nx][ny] = True
                                arr.append([nx, ny])  # 다음 방향 넣어놓기
                                transfer.append([nx,ny]) #인구이동을 해야되는것들의 갯수
                                sum += arr[nx][ny]
                if len(transfer) > 1:  #인구이동을 하는 나라가 1개이하일경우 == 인구이동x
                    Merge = True
                    for x,y in transfer:
                        people[x][y] = sum // len(transfer)  #좌표게 updated
    
    if Merge:
        ans += 1
    else:
        break
                        
print(ans)



```


### 1.4 한줄평

- transfer 과 visited를 합쳐서 구현 할수도 있지만 2차원 이상부터는 따로 구현하는게 맞는듯

- 조건에 따라서 추가로 배열이나 큐를 집어넣어서 세부조건을 충족시킬수 있다는것을 생각해두자