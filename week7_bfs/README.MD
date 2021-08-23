# [7주] [BFS] 발표자료
1. [2589 보물섬](#1-2589-보물섬)
2. [2665 미로만들기](#2-2665-미로만들기)

## 1. [2589 보물섬](https://www.acmicpc.net/problem/2589)
![2021-08-20 (1)](https://user-images.githubusercontent.com/69501435/130209810-926175a4-adbc-4877-a365-17f4f513ebc8.png)


### 1.1 자료구조
1. visited (list) : [방문한 곳인지 확인할 list]
2. stack (collections.deque()) : [dfs를 위한 큐(선입선출)]
3. 
### 1.2 풀이과정
1. arr을 순회 하며 L 을 발견하면 bfs로 가장 멀리 갈 수 있는 L 까지 접근하도록 한다.
2. 각각의 순회마다 갈 수 있는 곳 visited를 새로 만들어서 최대한 먼곳 까지 순회 할 수 있도록 한다.
3. 각각의 순회시에 막다른 길에 도착 하면 지금의 순회에서 나온 다른 깊이들과 비교하여 큰값을 선택한다.
4. 최종적인 max 값을 각각의 순회가 끝날때마다 비교하여 최신화 할 수 있도록 한다.

### 1.3 소스코드

```python
import sys
import collections

n, m = map(int,sys.stdin.readline().split())

arr = [list(sys.stdin.readline().strip()) for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]
real_max = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L':
            visited = [[1]*m for _ in range(n)]
            visited[i][j] = 0
            stack = collections.deque([[i,j,0]])
            max_len = 0
            while(len(stack)):
                this_turn = stack.popleft()
                this_row = this_turn[0]
                this_col = this_turn[1]
                count = 0
                for k in range(4):
                    row = this_row + dx[k]
                    col = this_col + dy[k]
                    if 0 <= row < n and 0 <= col < m and arr[row][col] =='L' and visited[row][col]:
                        visited[row][col] = 0
                        stack.append([row,col,this_turn[2]+1])
                        count += 1
                if count == 0 :
                   
                    max_len = max(max_len, this_turn[2]) 
            real_max = max(real_max, max_len)
print(real_max)  


```

## 2. [2665 미로만들기](https://www.acmicpc.net/problem/2665)
![2021-08-20 (2)](https://user-images.githubusercontent.com/69501435/130211047-733a57d2-212a-4b23-b3cf-a0c31220ee2a.png)

### 2.1 자료구조
1. dp (list) : [지금까지 몇개의 흑색칸을 지나왔는지 저장해놓는 list]
2. stack (collections.deque()) : [bfs를 돌 큐(선입선출)]
### 2.2 풀이과정
1. 처음 시작인 [0,0,0]을 넣고 stack이 빌 때까지 진행
2. 스택에서 popleft를 하고 나온 곳 기준으로 상하좌우의 dp속 값이 지금의 채울 수 있는 값보다 크게 되면 dp속 값을 변경하고 stack에 append할 수 있도록 한다.
3. 예로 dp에 이미 3이라는 값이 입력 되있는데 지금의 과정에서 그 칸을 1로 채울 수 있으면 stack에 append 그리고 dp값을 변경 한다.

### 2.3 소스코드

```python
import sys
import collections


   
n = int(sys.stdin.readline())

arr = [list(map(int,sys.stdin.readline().strip())) for _ in range(n)]

dp = [[n*n] * n for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

stack = collections.deque([[0,0,0]])

while(len(stack)):
    this_turn = stack.popleft()
    this_row = this_turn[0]
    this_col = this_turn[1]
    for i in range(4):
        row = this_row + dx[i]
        col = this_col + dy[i]
        if 0 <= row < n and 0 <= col < n :
            if arr[row][col] == 1:
                if dp[row][col] > this_turn[2]:
                    stack.append([row,col,this_turn[2]])
                    dp[row][col] = this_turn[2]
            else:
                if dp[row][col] > this_turn[2] + 1:
                    stack.append([row,col,this_turn[2]+1])
                    dp[row][col] = this_turn[2]+1
print(dp[n-1][n-1])

```
