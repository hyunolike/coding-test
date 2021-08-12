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

