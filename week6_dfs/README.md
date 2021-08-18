# DFS 깊이우선탐색 문제풀이

1. [1260 DFS와 BFS](#1-1260-DFS와-BFS)
2. [2667 단지번호붙이기](#2-2667-단지번호붙이기)
3. [1987 알파벳](#3-1987-알파벳)
4. [1012 유기농배추](#4-1012-유기농배추)
5. [10026 적록색약](#5-10026-적록색약)
6. [11725 트리의 부모 찾기](#6-11725-트리의-부모-찾기)
7. [1707 이분 그래프](#7-1707-이분-그래프)
8. [4963 섬의 개수](#8-4963-섬의-개수)
9. [2573 빙산](#9-2573-빙산)
10. [1068 트리](#10-1068-트리)
11. [1520 내리막길](#11-1520-내리막길)
12. [1937 욕심쟁이 판다](#12-1937-욕심쟁이-판다)

## 1. [1260 DFS와 BFS](https://www.acmicpc.net/problem/1260)
![image](https://user-images.githubusercontent.com/44918665/129136707-44d99800-7866-4823-9fae-5dd0982b07c8.png)

### 1.1. 문제유형
- DFS, BFS

### 1.2. 자료구조
- graph (2d list): 노드의 간선 연결 정보를 담은 리스트
- visited (list): 노드 방문 정보를 담은 리스트
- queue (deque): bfs 구현을 위한 큐 자료구조

### 1.3. 해결과정
- ⭐DFS는 재귀, 스택을 사용해서 구현한다. (재귀도 구현과정에서 Stack을 사용함)
- ⭐BFS는 큐 자료구조를 사용해서 구현한다.

### 1.4. 소스코드

```python
from collections import deque

def dfs(v):
    visited[v] = 1
    print(v, end=' ')
    for i in range(1, n+1):
        if graph[v][i] == 1 and visited[i] ==0:
            dfs(i)

def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = 1

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in range(1, n+1):
            if graph[v][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i]=1

n, m, v = map(int, input().split())
graph = [[0]*(n+1) for i in range(n+1)]
visited = [0]*(n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

dfs(v)
visited = [0]*(n+1)
print()
bfs(v)
```

## 2. [2667 단지번호붙이기](https://www.acmicpc.net/problem/2667)
![image](https://user-images.githubusercontent.com/44918665/129139685-661bb533-b9ff-4733-8c36-acf5732336e1.png)

### 2.1. 문제유형
- 그래프

### 2.2. 자료구조
- graph (2d list): 아파트 단지 정보를 저장하는 2차원 리스트
- visited (2d list): 방문한 아파트 위치를 저장하는 2차원 리스트
- cnt (int): 아파트 단지 수를 count하는 변수
- search (function):
    - i (int): x좌표
    - j (int): y좌표
    - (i,j)를 방문한 뒤 graph 좌표를 0으로, visited 좌표를 1로 변경 후 cnt를 1증가시키는 함수
    - (i,j)를 방문한 뒤 (i,j) 기준으로 동, 서, 남, 북에 대해 search 함수를 수행한다.
    - i, j가 그래프 최소, 최대 범위를 벗어나거나, graph 값이 0인 곳을 만날 때 종료

### 2.3. 해결과정
1. 한 좌표씩 방문한 곳인지, 그래프가 연결된 곳인지 확인한다.
2. 만약 방문하지 않았고, graph값이 존재한다면 search 함수를 호출한다.
3. search 함수 결과로 count 된 cnt값을 answer에 저장하고, cnt값을 초기화한다.

### 2.4. 소스코드

```python
n = int(input())
graph = list(list(map(int, input())) for _ in range(n))
visited = [[0]*n for _ in range(n)]
answer = []
cnt = 0

def search(i, j):
    global cnt
    if i<0 or j>=n or i>=n or j<0 or graph[i][j]==0:
        return
    graph[i][j]=0
    visited[i][j]=1
    cnt += 1
    
    search(i+1, j)
    search(i, j+1)
    search(i-1, j)
    search(i, j-1)

for i in range(n):
    for j in range(n):
        if visited[i][j]==0 and graph[i][j]==1:
            search(i,j)
            answer.append(cnt)
            cnt = 0

print(len(answer))
for i in sorted(answer):
    print(i)
```

## 3. [1987 알파벳](https://www.acmicpc.net/problem/1987)
![image](https://user-images.githubusercontent.com/44918665/129364411-0e76af2c-1ae0-4c3c-a6e3-a772a2dbb335.png)

### 3.1. 문제유형
- DFS, BFS

### 3.2. 자료구조
- BFS
- nx, ny (int): 이동한 위치 좌표
- answer (int): 최대로 방문할 수 있는 칸 수
- q (int): 방문한 칸 정보인 x,y, 알파벳을 저장하는 set
- dx, dy (int): 맵 상에서 상,하,좌,우 좌표이동을 위한 리스트
- alphas (int): 현재 방문한 알파벳들을 이어붙인 문자열
- BFS (fucntion)
    - x, y (int): x,y 좌표
    - x, y로부터 방문 가능한 칸을 BFS 탐색을 수행하는 함수

### 3.3. 해결과정
- BFS
1. (0,0)부터 BFS탐색을 시작한다.
2. q에 현재 위치 정보 (x, y, board[x][y])를 저장한다.
3. q가 차 있을 동안 아래 과정을 반복한다.
4. q에 들어 있는 x,y, alphabets을 꺼낸다.
5. 현재 위치를 기준으로 상하좌우를 탐색한다.
6. 만약 지도 범위 안이고, 방문하지 않은 알파벳이라면 q에 좌표와 방문문자열 정보를 추가한다.
7. answer 값을 alphabets + 1로 갱신한다.

### 3.4. 소스코드

```python
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def BFS(x, y):
    global answer
    q = set([(x, y, board[x][y])])

    while q:
        x, y, alphas = q.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if ((0 <= nx < R) and (0 <= ny < C)) and (board[nx][ny] not in alphas):
                q.add((nx,ny,alphas + board[nx][ny]))
                answer = max(answer, len(alphabets)+1)

R, C = map(int, input().split())
board = [list(map(str, input())) for _ in range(R)]


answer = 1
BFS(0, 0)
print(answer)
```


## 4. [1012 유기농배추](https://www.acmicpc.net/problem/1012)
![image](https://user-images.githubusercontent.com/44918665/129364316-64350288-a2dc-40e9-a0c9-59e78819c9f8.png)
![image](https://user-images.githubusercontent.com/44918665/129364365-439f2ad2-6e15-430a-85b6-80bad8abc01a.png)

### 4.1. 문제유형
- DFS, BFS

### 4.2. 자료구조
- dx, dy (List): 상하좌우 이동을 위한 리스트
- queue (Deque): BFS 탐색을 위한 queue
- x, y (int): 현재 위치 좌표
- nx, ny (int): 이동한 위치 좌표
- field (2d-list): 배추좌표를 저장하는 2차원 리스트
- BFS (function):
    - x, y (int): 위치 좌표 
    - 현재 위치를 기준으로 연결된 배추에 대해 BFS 탐색을 수행하는 함수

### 4.3. 해결과정
- BFS
1. 전체 field를 탐색하며 각각의 i,j에 대해 다음 조건을 만족하는 지 체크한다.
2. 현재 i,j 좌표에 배추가 심어져 있는가(field[i][j]==1)
3. 위 조건을 만족하면 BFS를 수행하고, cnt를 1 증가시킨다.
4. BFS 함수는 현재 위치 x,y를 기준으로 상하좌우에 대해 다음 조건을 체크한다.
5. 만약 field 범위 안이고 배추가 심어져 있다면(1), 해당 좌표를 queue에 넣는다.
6. 그리고 해당 좌표 값에는 1이 아닌 2(이미 방문한 표시)로 변경한다.

### 4.4. 소스코드

```python
from collections import deque

t = int(input())

def BFS(x,y):
    dx=[-1,0,1,0]
    dy=[0,-1,0,1]
    queue=deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<m:
                if field[nx][ny]==1:
                    queue.append((nx,ny))
                    field[nx][ny]=2

for _ in range(t):
    m,n,k = map(int, input().split())
    field=[[0]*m for _ in range(n)]
    cnt = 0

    for _ in range(k):
        x,y = map(int, input().split())
        field[y][x]=1
    
    for i in range(n):
        for j in range(m):
            if field[i][j]==1:
                BFS(i,j)
                cnt+=1
    print(cnt)
```

## 11. [1520 내리막길](https://www.acmicpc.net/problem/1520)
![image](https://user-images.githubusercontent.com/44918665/129852841-e9bb5fdb-b2ea-4d87-a882-a77228bb46ff.png)
![image](https://user-images.githubusercontent.com/44918665/129852984-01f155e6-68a8-462c-9320-131edc566603.png)

### 11.1. 문제유형
- 다이나믹 프로그래밍(DP)
- 깊이우선탐색 (DFS)

### 11.2. 자료구조
- x, y (int): 지도 상 위치를 표시하는 변수
- visited (2d-list): 방문여부와 발견한 경로 수를 저장하는 map

### 11.3. 해결과정
1. ⭐DFS와 DP 개념을 모두 알아야 시간초과 테스트를 통과할 수 있었다.
2. ⭐**방문한 위치 표시 + 현재까지 찾은 경로의 수**를 저장하기 위한 visited 지도를 생성한다.
3. ⭐최대 재귀횟수를 증가시켜주기 위해 **sys의 setrecursionlimit 함수**를 사용했다.
4. (0,0)에서부터 동서남북을 탐색 후 지도 내 범위에 있으며 현 위치보다 낮은 칸을 방문한다.
5. 만약 방문한 칸이 이미 방문한 위치라면 visited의 현 위치에 저장된 값을 반환한다.
6. 만약 방문한 칸이 최종 목적지라면 1을 반환한다.
7. 3,4에 해당하지 않으면 동서남북을 탐색 후 현 위치보다 낮은 칸에 대해 DFS 탐색을 수행한다.
8. 현재 visited 위치에 DFS 탐색 결과를 더해준 뒤 visited 현재 위치를 반환한다.

- 결국 해당 위치가 목적지에 도달할 수 있는 경로라면 숫자가 증가한다.
- DFS(0,0)에서부터 시작하므로, 도달 가능한 경로의 수가 visited의 (0,0)에 저장된다.

### 11.4. 소스코드

```python
import sys
sys.setrecursionlimit(10 ** 8)

def DFS(x, y):
    if x==m-1 and y==n-1:
        return 1
    if visited[x][y] != -1:
        return visited[x][y]
    visited[x][y]=0

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    for i in range(4):
        a = x + dx[i]
        b = y + dy[i]

        if 0<=a<m and 0<=b<n and graph[a][b]<graph[x][y]:
            visited[x][y] += DFS(a, b)
        
    return visited[x][y]

if __name__=="__main__":
    m, n = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(m)]
    visited = [[-1]*n for _ in range(m)]
    print(DFS(0, 0))
    for a in visited:
        print(a)
```

