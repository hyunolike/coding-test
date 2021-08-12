# DFS 깊이우선탐색 문제풀이

1. [1260 DFS와 BFS](#1-1260-DFS와-BFS)
2. 2667 단지번호붙이기
3. 1987 알파벳
4. 1012 유기농배추
5. 10026 적록색약
6. 11725 트리의 부모 찾기
7. 1707 이분 그래프
8. 4963 섬의 개수
9. 2573 빙산
10. 1068 트리
11. 1520 내리막길
12. 1937 욕심쟁이 판다

## 1. 1260 DFS와 BFS
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
