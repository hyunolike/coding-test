# [6주] [DFS] 발표자료
1. [1012 유기농 배추](#1-1012-유기농-배추)
2. [1987 알파벳](#2-1987-알파벳)
3. [10026 적록색약](#3-10026-적록색약)
4. [11725 트리의 부모 찾기](#4-11725-트리의-부모-찾기)
5. [1707 이분 그래프](#5-1707-이분-그래프)
## 1. [1012 유기농 배추](https://www.acmicpc.net/problem/1012)
![2021-08-18 (1)](https://user-images.githubusercontent.com/69501435/129834487-7c4b53bb-c48c-4453-8d81-bc1c0f9b57e6.png)

### 1.1 자료구조
1. stack(collections.deque()) : [dfs내에서 좌표를 담을 deque(stack)]
2. arr(list) : [edge들의 상태를 저장해둘 list]
3. ptr(list) : [dfs의 pop과정 후 갈 수 있는곳을 조사할 후보군 list]
### 1.2 풀이과정
1. count의 변수는 최종 답이 될 구역의 횟수이다.
2. arr을 순회하며 1을 만나면 그 좌표 기준으로 dfs를 실행한다.
3. dfs의 과정에서 한번 갔던곳은 다시 못가도록 1이었던 요소를 2로 바꿔준다.
4. n*m행렬을 모두 순회하고 나면 모든 구역의 개수 확인!

### 1.3 소스코드

```python
import sys
import collections
t=int(sys.stdin.readline())
result = []
for _ in range(t):
    m, n, k=map(int,(sys.stdin.readline().split()))
    
    arr = [[0]*m for _ in range(n)]
   
    for _ in range(k):
        col , row = map(int,sys.stdin.readline().split())
        arr [row][col] =1

    count = 2
    stack = collections.deque([])
    count=0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                stack.append([i,j])
                arr[i][j] = 0
                while(len(stack)):
                
                    this_turn = stack.pop()
                    this_row = this_turn[0]
                    this_col = this_turn[1]
                    ptr = [[this_row-1,this_col],[this_row+1,this_col],[this_row,this_col-1],[this_row,this_col+1]]
                    for s in ptr:
                        row_1 = s[0]
                        col_1 = s[1]
                        if row_1 >= n or row_1 <=-1 or col_1 >= m or col_1 <= -1:
                            continue
                        else:
                            if arr[row_1][col_1] == 1:
                                arr[row_1][col_1] = 2
                                stack.append([row_1,col_1])
                    
                        
                count+=1
    result.append(count)
for i in result:
    print(i)


```

## 2. [1987 알파벳](https://www.acmicpc.net/problem/1987)
![2021-08-18 (2)](https://user-images.githubusercontent.com/69501435/129838689-36f84a83-882c-4e63-983a-9fc194eb4b3d.png)

### 2.1 자료구조
1. oi(list) = 재귀적으로 dfs를 구현 하기위해 방문했는지 확인해줄 list
2. per(func) = dfs를 재귀적으로 구성해줄 함수

### 2.2 풀이과정
1. result는 최종적으로 구한 영역의 최대값
2. 0,0좌표의 값부터 dfs 시작
3. 확인 해야할 후보군을 조사하고 갈 수 있는 곳이면 그 곳을 갈 수 없다고 설정하고 다시 dfs실행
4. 그러다 만약 갈 곳이 없어지면 지금까지 온곳의 영역의 크기와 result중 최대값을 result가 갖게한다.
(하지만 아직 시간초과를 해결하지 못했다. 어떤 답이 나오는지 배우고 수정하겠다.)

### 2.3 소스코드

```python
import sys


def per(idx,length):
    global result
    count = 0
    for i in range(4): 
        row = idx[0] + dx[i]
        col = idx[1] + dy[i]
            
        if 0<=row<=n-1 and 0<=col<=n-1 and not oi[arr[row][col]]:
            oi[arr[row][col]]= 1
            per([row,col],length+1)
            oi[arr[row][col]]= 0
            count += 1
        if not count:
            result = max(result, length)
            
        
        
        
n, m = map(int,sys.stdin.readline().split())

arr = [list(map(lambda x: ord(x)-65,sys.stdin.readline().strip())) for _ in range(n)]


result = 0
dx = [-1,1,0,0]
dy = [0,0,1,-1]
oi = [0]*26
oi[arr[0][0]] = 1


per([0,0],1)
print(result)

```

## 3. [10026 적록색약](https://www.acmicpc.net/problem/10026)
![2021-08-18 (3)](https://user-images.githubusercontent.com/69501435/129839987-71bb9832-2932-4c66-8755-8a33d48b222d.png)

### 3.1 자료구조
1. visit(list) : 일반사람이 순회하는 (visited확인하는) list
2. visit_eye(list) : 적록색맹사람 ver
3. stack1 (collections.deque()) : 무슨 사람이든 자기 상황에 맞는 dfs를 실행하기 위한 stack
### 3.2 풀이과정
1. arr을 순회하면서 두가지 상황을 생각한다.
2. 일반사람이 오지 않은 곳이면 일반사람이 갈 수 있는곳 까지 dfs하는 과정
3. 적록색맹의 사람이 오지 않은 곳이면 적록색맹이 갈 수 있는 곳 까지 dfs 하는 과정
4. 각각의 구역의 개수를 (2번 3번의) if문 첫번째줄에서 숫자를 +1하도록

### 3.3 소스코드

```python
import sys
import collections
n = int(sys.stdin.readline())

arr = [list(sys.stdin.readline().strip()) for _ in range(n)]

count = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0 ,-1]
visit = []
visit_eye = []
for i in range(n):
    visit.append([])
    for j in range(n):
        visit[i].append(True)
for i in range(n):
    visit_eye.append([])
    for j in range(n):
        visit_eye[i].append([True])
compare = {'R':1, 'G':1,'B':-1}
count_eye = 0
stack1 = collections.deque([])
for i in range(n):
    for j in range(n):
        if visit[i][j]:
           
            count+=1
            visit[i][j] = False
            stack1.append([i,j])
            while(len(stack1)):
                this_turn = stack1.pop()
                this_row = this_turn[0]
                this_col = this_turn[1]
                
                for k in range(4):
                    row = this_row + dx[k]
                    col = this_col + dy[k]
                   
                    if row>=n or row<=-1 or col>=n or col<=-1 or visit[row][col] == False:
                        continue
                    if arr[row][col] == arr[this_row][this_col]:
                       
                        stack1.append([row,col])
                        visit[row][col] = False
        if visit_eye[i][j]:
            count_eye+=1
            visit_eye[i][j] = False
            stack1.append([i,j])
            while(len(stack1)):
                this_turn = stack1.pop()
                this_row = this_turn[0]
                this_col = this_turn[1]
                for k in range(4):
                    row = this_row + dx[k]
                    col = this_col + dy[k]
                    if row>=n or row<=-1 or col>=n or col<=-1 or visit_eye[row][col] == False:
                        continue
                    if compare[arr[row][col]] == compare[arr[this_row][this_col]]:
                        stack1.append([row,col])
                        visit_eye[row][col] = False
print(count,count_eye)

```

## 4. [11725 트리의 부모 찾기](https://www.acmicpc.net/problem/11725)
![2021-08-18 (4)](https://user-images.githubusercontent.com/69501435/129851456-a83e7a24-7d72-44e9-8f3c-83f5547ab406.png)

### 4.1 자료구조
1. possible (list) : 갈 수있는지 확인하기 위한 list(True로 초기화)
2. graph (dict) : 그래프의 연결형태를 저장하기
3. stack (collections.deque()) : dfs를 위한 stack
### 4.2 풀이과정
1. result 자기의 부모노드를 저장할 n+1 개의 리스트를 생성(결과로 보여줄 리스트)
2. 입력받은 arr을 돌면서 graph에 저장하기 ex) graph[1] = {2}
3. dfs과정에서 갈 수 있는곳을 stack에 넣음과 동시에 갈 수 있는곳의 부모노드가 이번 반복문에서 pop한 원소임을 이용 !
4. 모두 연결되어 있다는 가정하에 하는 것이므로 2번째 요소부터 출력!

### 4.3 소스코드

```python
import sys
import collections
n = int(sys.stdin.readline())

arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n-1)]
result =[]
for _ in range(n+1):
    result.append(0)
possible = [True]*n
graph = dict()

for i in arr:
    start , finish = i[0], i[1]
    try:
        graph[start].add(finish)
    except:
        graph[start]={finish}
    try:
        graph[finish].add(start)
    except:
        graph[finish] = {start}

stack = collections.deque([[1]])
possible[0] = False
while(len(stack)):
    this_turn = stack.pop()
    val = this_turn[0]
    for i in graph[val]:
        if possible[i-1]:
            stack.append([i])
            possible[i-1] = False
            result[i] = val
for i in range(2,n+1):
    print(result[i])



```

## 5. [1707 이분 그래프](https://www.acmicpc.net/problem/1707)
![2021-08-18 (5)](https://user-images.githubusercontent.com/69501435/129871704-4d3d21f2-48df-4fe7-b006-5c7002e22d80.png)


### 5.1 자료구조
1. chil (dict) : 지금 위치의 색깔을 0, 1로 저장
2. graph (dict) : 그래프의 연결상태를 저장
3. possible (dict) : 이미 들린 곳인지 확인할 dict
4. stack(collections.deque()) : bfs 순회 하기 위한 queue
### 5.2 풀이과정
1. 각각의 테스트 케이스마다 새로운 graph, chil, possible 이 필요하므로 이를 초기화 하는 작업을 진행
2. 처음 edge기준으로 갈 수 있는곳 다 순회 (bfs 방법 선택 why? 자식노드 끼리는 색이 같아야 하는데 다른지 확인하기 위해 bfs 이용
3. 한 번 이 순회를 하고 나면 start기준으로 갈 수 있는곳은 조사가 다 된 상태이므로 나머지 안가본 노드에 대해서도 조사가 필요
4. possible.keys()를 순회하며 지금 껏 가지못한 원소를 찾기 만약 찾으면 2번의 처음 edge를 찾은 원소로 설정하고 다시 반복 수행한다.
5. 그러다 모든 원소를 다 들렸고 문제가 없었으면 yes 그 사이에 한번이라도 잘못된 부분이 있으면 no를 append해준다

### 5.3 소스코드

```python
import sys
import collections
n = int(sys.stdin.readline())
result = []
for _ in range(n):
    vertex ,edge = map(int,sys.stdin.readline().split())
    graph = dict()
    start , arrive = map(int,sys.stdin.readline().split())
    stack = collections.deque([start])
    
    chil = dict()
    flag = 1
    chil[start] = 0
    graph[start] ={arrive}
    graph[arrive] = {start}
    possible = dict()
    possible[start] = False
    possible[arrive] = True
    for _ in range(1,edge):
        start, arrive = map(int,sys.stdin.readline().split())
        try:
            graph[start].add(arrive)
        except:
            graph[start] = {arrive}
            possible[start] = True
        try:
            graph[arrive].add(start)
        except:
            graph[arrive] = {start}
            possible[arrive] = True
    while(flag):
        while(len(stack) and flag):
            where = stack.popleft()
            this_color = chil[where]
            
            for i in graph[where]:
                if possible[i]:
                    stack.append(i)
                    chil[i] = (this_color + 1)%2
                    possible[i] = False
                else:
                    if this_color == chil[i]:
                        flag = 0 
                        result.append('NO')
                        break
        if flag == 0:
            break
        this_flag = 1
        for j in possible.keys():
            if possible[j]== True:
                new_vertex = j
                this_flag = 0
                break
        
        
        if this_flag:
            result.append('YES')
            break
        else:
            stack.append(new_vertex)
            chil[new_vertex] = 0
            possible[new_vertex] = False
  

for i in result:
    print(i)


```
