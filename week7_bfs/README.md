# 7주차 BFS

1. 7562 나이트의 이동
2. 16234 인구이동
3. [2589 보물섬](#3.-2589-보물섬)
4. [2665 미로만들기](#4.-2665-미로만들기)
5. 18352 특정 거리의 도시 찾기
6. 18405 경쟁적 전염
7. 2644 촌수계산
8. 17135 캐슬 디펜스
9. 2583 영역구하기
10. 2206 벽 부수고 이동하기
11. 2606 바이러스
12. 14502 연구소

## [3. 2589 보물섬](https://www.acmicpc.net/problem/2589)
![image](https://user-images.githubusercontent.com/44918665/130240132-bad6758e-b96a-45fb-aa26-452165579b11.png)

### 3.1. 문제유형
- BFS

### 3.2. 자료구조
- dist (int): 출발한 육지부터 도착한 육지까지의 거리를 저장한 변수
- answer (int): dist의 최대값을 계속해서 갱신해나가는 변수
- graph (2d-list): 지도 정보를 저장한 2차원 리스트
- dx, dy (list): 상하좌우 이동 정보를 저장한 리스트
- Q (deque): BFS 구현을 위한 큐 자료구조
- visited (2d-list): graph 지도에 대해 방문한 여부와 좌표별 이동한 거리를 저장하는 변수

### 3.3. 해결과정
- ⭐육지인 곳에서부터 BFS를 돌며 dist를 측정하고, 최대값을 answer에 갱신해나간다.
1. 전체 좌표에 대해 BFS 탐색 수행을 수행
2. 해당 좌표가 L(육지)라면 큐에 해당 좌표를 넣고, visited를 생성 후 방문 처리
3. Q에 원소가 존재한다면 꺼내서 상하좌우 탐색을 수행
4. 상하좌우 중 지도내에 있는 육지이면서 방문하지 않은 곳이 있다면 Q에 추가
5. visited 다음 위치에 현재 visited + 1 처리 (방문한 거리를 1 증가시킴)
6. 현재 dist와 visited 다음 위치를 비교한 뒤 큰 값을 저장한다.

### 3.4. 소스코드
```python
from collections import deque

if __name__=="__main__":
    # L은 육지, W는 바다
    n,m = map(int, input().split())
    graph=[list(map(str, input())) for _ in range(n)]

    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    answer = 0

    for i in range(n):
        for j in range(m):
            dist = 0
            if graph[i][j]=='L':
                Q=deque()
                Q.append([i, j])
                visited = [[0]*m for _ in range(n)]
                visited[i][j] = 1

                while Q:
                    a, b = Q.popleft()
                    for k in range(4):
                        x = a+dx[k]
                        y = b+dy[k]
                        if 0<=x<n and 0<=y<m:
                            if graph[x][y]=='L' and visited[x][y]==0:
                                visited[x][y]=visited[a][b]+1
                                dist = max(dist, visited[x][y]-1)
                                Q.append([x, y])
            if dist !=0:
                answer = max(answer, dist)
    print(answer)

```

## [4. 2665 미로만들기](https://www.acmicpc.net/problem/2665)
![image](https://user-images.githubusercontent.com/44918665/130240213-3b7d775e-17d3-4360-ae85-246d2e222a38.png)

### 4.1. 문제유형
- BFS

### 4.2. 자료구조
- visited (2d list): 현재까지 변경한 검은방의 수를 저장한 2차원리스트
- dx, dy (list): 상하좌우 탐색 수행을 위한 리스트
- Q (deque): BFS 구현을 위한 큐 자료구조

### 4.3. 해결과정
- ⭐지도 내 범위에 있으며, 방문하지 않은 곳을 BFS 탐색을 수행한다.
- ⭐흰 방을 만나면 우선 방문하고(큐 맨 앞 삽입), 검은 방을 만나면 visited값을 1증가 시킨 뒤 큐 맨 뒤에 삽입한다.
- 위 과정을 거치고 나면 목적지에 흰 방을 최대한 많이 방문한 경로가 저장된다.

### 4.4. 소스코드
```python
from collections import deque

if __name__=="__main__":
    n=int(input())
    graph=[list(map(int, input())) for _ in range(n)]

    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    visited = [[-1]*n for _ in range(n)]
    Q=deque()
    Q.append([0, 0])
    visited[0][0]=0

    while Q:
        a, b = Q.popleft()
        for i in range(4):
            x = a+dx[i]
            y = b+dy[i]

            if 0<=x<n and 0<=y<n and visited[x][y]==-1:
                if graph[x][y]==0:
                    visited[x][y]=visited[a][b]+1
                    Q.append([x,y])
                else:
                    visited[x][y]=visited[a][b]
                    Q.appendleft([x,y])
    print(visited[n-1][n-1])
```
