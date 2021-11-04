# 9 Week Simulation
- 시뮬레이션: 문제에서 제시한 알고리즘을 한 단계식 차례대로 직접 수행하는 유형
- 완전 탐색: 모든 경우의 수를 다 계산하는 해결방법

1. 2933 미네랄
2. 14719 빗물
3. 3190 뱀
4. 1713 후보추천하기
5. [13335 트럭](#5-13335-트럭)
6. [14499 주사위 굴리기](#6-14499-주사위-굴리기)
7. [14503 로봇 청소기](#7-14503-로봇-청소기)
8. 17140 이차원 배열과 연산
9. [16236 아기상어](#9-16236-아기상어)
10. [1244 스위치 켜고 끄기](#1244-스위치-켜고-끄기)

## 5. [13335 트럭](https://www.acmicpc.net/problem/13335)
![image](https://user-images.githubusercontent.com/44918665/132179064-c884a6c0-b746-4fdc-83f3-c8189f2a933c.png)

### 5.1. 문제유형
- 시뮬레이션

### 5.2. 풀이과정
- 주어진 로직을 따라가며 그대로 구현하였다.
- 두 가지 조건을 체크하며, 트럭을 통과시켰다.
1. 다리가 꽉 차 있는가?
2. 다리의 무게가 버틸 수 있는가?
- 다리가 꽉 차 있지 않고, 트럭 무게를 감당할 수 있으면 트럭을 통과시킨다.
- 다리 위의 트럭 초를 증가시키며 1칸씩 전진시킨다.
- ⭐ 주의할 점은 다리를 완전히 통과할 때, 동시에 다음 트럭이 들어와야 하는 경우를 고려해야한다.
- 따라서 미리 트럭을 제거해주었으므로, 마지막 소스코드에 1초를 추가해주었다.

### 5.3. 소스코드
```python
from collections import deque

n, w, l = map(int, input().split())
trucks = deque(list(map(int, input().split())))
bridge = deque()
sec = 0
while trucks:
    sec += 1
    total = sum([weight for weight, _ in bridge])
    
    if total+trucks[0] <= l and len(bridge) < w:
        go = trucks.popleft()
        bridge.append([go, 1])
    for i in range(len(bridge)):
        bridge[i][1] += 1
    if bridge[0][1] == w+1:
        bridge.popleft()

while bridge:
    sec += 1
    for i in range(len(bridge)):
        bridge[i][1] += 1
    if bridge[0][1] == w+1:
        bridge.popleft()
# 1초를 추가하는 이유
# 맨 앞 트럭이 다음 트럭이 들어 올 수 있도록 미리 빠져나가므로, 1초 일찍 종료됨
print(sec+1)
```

## 6. [14499 주사위 굴리기](https://www.acmicpc.net/problem/14499)
![image](https://user-images.githubusercontent.com/44918665/132179923-07b2d4df-20b9-467d-87a0-541a04d54a64.png)

### 6.1. 문제유형
- 시뮬레이션

### 6.2. 풀이과정
- 이 문제는 크게 3가지를 고려해야 해결할 수 있었다.
1. 뒤집어진 좌표계 (r,c)로 이동한다. r은 북쪽으로부터 떨어진 수, c는 서쪽으로부터 떨어진 수
    - 따라서 동,서,북,남 이동 시 반대로 좌표계를 설정해주어야한다.
2. 두 번째는 동서남북 이동 시, 변하는 주사위 모양대로 변형시켜 주어야한다.
    - 실제 전개도를 그려보며, 어떤 특징이 있는지 파악했다.
3. 현재 좌표값이 0이면 현재 좌표에 주사위 밑면 값을 저장한다.
    - 현재 좌표값이 0이 아니라면, 주사위 밑면에 좌표값을 저장하고 좌표값을 0으로 바꾼다.

### 6.3. 소스코드

```python
n, m, x, y, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
commands = list(map(int, input().split()))

# dx=[1,-1,0,0]
# dy=[0,0,-1,1]
dx=[0,0,-1,1] # x좌표가 북쪽으로부터 떨어진 개수. 위아래. 
dy=[1,-1,0,0] # y좌표가 서쪽으로부터 떨어진 개수. 좌우
dice=[0,0,0,0,0,0]

for dir in commands:
    nx = x + dx[dir-1]
    ny = y + dy[dir-1]
    
    if not (0<=nx<n and 0<=ny<m):
        continue

    if dir == 1:
        dice[0],dice[1],dice[2],dice[5] = dice[5],dice[0],dice[1],dice[2]
    elif dir == 2:
        dice[0],dice[1],dice[2],dice[5] = dice[1],dice[2],dice[5],dice[0]
    elif dir == 3:
        dice[1],dice[3],dice[4],dice[5] = dice[4],dice[1],dice[5],dice[3]
    else:
        dice[1],dice[3],dice[4],dice[5] = dice[3],dice[5],dice[1],dice[4]
    
    if graph[nx][ny] == 0:
        graph[nx][ny] = dice[1]
    else:
        dice[1] = graph[nx][ny]
        graph[nx][ny] = 0
    
    x, y = nx, ny
    print(dice[5])
```
### 6.4. 노트필기
![image](https://user-images.githubusercontent.com/44918665/132491285-4281d244-5dbb-4e37-b14b-88d8c6520dd4.png)

## 7. [14503 로봇 청소기](https://www.acmicpc.net/problem/14503)
![image](https://user-images.githubusercontent.com/44918665/132345088-47ae57f6-d385-4a27-b42c-d946d306a9fc.png)

### 7.1. 문제유형
- 시뮬레이션

### 7.2. 풀이과정
- 3가지를 정확히 구현해야 해결할 수 있었다.
1. 좌표 이동을 기존 좌표계와 반대로 구현해야한다.
2. 좌표 이동 시 방향 d가 현재 기준 왼쪽부터 탐색하도록 구현해야 한다.
3. 방향 d에 대해 후진 위치를 정확히 지정해주어야 한다.
- 1,2번까지는 제대로 구현했으나, 3번 제대로 지정하지 못해 오랜 시간이 소요되었다.

### 7.3. 소스코드
```python
n, m = map(int, input().split())
r,c,d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

dx=[-1,0,1,0] #북,동,남,서
dy=[0,1,0,-1]

def DFS(x, y, d):
    global answer
    if graph[x][y]==0:
        graph[x][y]=2
        answer+=1

    for _ in range(4):
        idx=(d+3)%4
        nx,ny=x+dx[idx],y+dy[idx]
        if graph[nx][ny]==0:
            DFS(nx,ny,idx)
            return 0
        d=idx
    nd=(d+2)%4 # 후진 위치 지정
    nx,ny=x+dx[nd],y+dy[nd]
    if graph[nx][ny]==1:
        return 0
    DFS(nx,ny,d) # 방향을 유지한 채 후진
        
answer = 0
DFS(r, c, d)
print(answer)

```
### 7.4. 노트필기
![image](https://user-images.githubusercontent.com/44918665/132345518-96ba503d-f8c2-41e1-a7b9-8649a10097ed.png)

## 9. [16236 아기상어](https://www.acmicpc.net/problem/16236)
![image](https://user-images.githubusercontent.com/44918665/132512550-dbec48cd-77ef-4c24-9d34-bde022e53c61.png)

### 9.1. 문제유형
- 시뮬레이션

### 9.2. 해결과정
- 고려할 조건이 많은 까다로운 문제였다.
1. 상어 위치를 찾고, BFS 탐색을 수행한다.
2. 먹을 물고기가 있는지 없는지를 확인한다.
3. 같은 거리라면 가장 위 물고기를, 그런 물고기가 여러마리라면 왼쪽 물고기를 먼저 먹는다.
4. 상어의 크기 변화 조건 (먹은 물고기 수)을 체크한다.
5. 먹이를 먹은 후, 새로운 위치 탐색을 위해 큐와 방문장소를 초기화한다.
6. 먹이를 먹은 후, 현재까지의 시간을 저장한다.

### 9.3. 소스코드

```python
from collections import deque

dxs=[-1,1,0,0]
dys=[0,0,-1,1]

def BFS(x, y):
    Q, visited=deque([(x,y)]), set([(x,y)])
    time=0
    shark=2
    eats=0
    answer=0
    flag = False # 먹을 물고기가 있는지를 확인하는 변수
    
    while Q:
        length = len(Q)

        Q=deque(sorted(Q)) # 정렬하여, 왼쪽 물고기부터 Eat
        for _ in range(length):
            x, y = Q.popleft()
            
            if graph[x][y] !=0 and graph[x][y]<shark: # 먹을 수 있는 물고기
                graph[x][y]=0
                eats+=1

                if eats == shark: # 크기 변화 조건 충족
                    shark+=1
                    eats=0

                Q, visited = deque(), set([(x,y)]) # 새로운 위치 탐색을 위한 초기화
                flag = True
                answer=time # 현재까지의 시간 저장

            for dx, dy in zip(dxs, dys): # 새 위치에서 상하좌우 탐색
                nx, ny = x+dx, y+dy
                if not (0<=nx<n and 0<=ny<n) or (nx,ny) in visited:
                    continue
                if graph[nx][ny] <= shark: # 이동 가능한 위치일 경우 이동
                    Q.append((nx,ny))
                    visited.add((nx,ny))

            if flag: # 만약 더 이상 먹을 물고기가 없다면
                flag=False
                break

        time+=1 # 시간 1 증가
    return answer


n = int(input())
graph=[list(map(int,input().split())) for _ in range(n)]

x,y=0,0
for i in range(n):
    for j in range(n):
        if graph[i][j]==9:
            x, y = i, j
            graph[i][j]=0

print(BFS(x,y))
```

## 10. [1244 스위치 켜고 끄기](https://www.acmicpc.net/problem/1244)
![image](https://user-images.githubusercontent.com/44918665/132516638-3a8656c6-7352-4c59-8098-be89e57cc95b.png)

### 10.1. 문제유형
- 시뮬레이션

### 10.2. 해결과정
1. 여성일 경우와 남성일 경우를 처리하는 함수를 2개 구성했다.
2. 남성의 경우 받은 번호의 배수에 해당하는 스위치를 Turnoff한다.
    - 배수임을 확인할 때는 입력받은 값을 그대로 사용하되, 인덱싱할 때는 -1 처리한다.
3. 여성의 경우 받은 번호의 양 옆 대칭인 스위치를 Turnoff한다.
    - 입력받은 값을 -1 처리 후 왼쪽, 오른쪽 값을 인덱싱한다.

### 10.3. 소스코드
```python

n=int(input())
switch=list(map(int,input().split()))
s=int(input())
students=[list(map(int, input().split())) for _ in range(s)]

def male(num):
    for i in range(1, len(switch)+1):
        if i % num == 0:
            switch[i-1] = (switch[i-1]+1)%2
    return 0

def female(num):
    num = num-1
    s,e = num-1, num+1
    switch[num]=(switch[num]+1)%2
    while True:
        if not (0<=s<n and 0<=e<n):
            return 0
        if switch[s]==switch[e]:
            switch[s]=(switch[s]+1)%2
            switch[e]=(switch[e]+1)%2
        else:
            return 0
        s,e = s-1, e+1

for sex, num in students:
    if sex==1:
        male(num)
    else:
        female(num)

for i in range(len(switch)):
    if i>0 and i%20==0:
        print()
    print(switch[i], end=' ')
```
