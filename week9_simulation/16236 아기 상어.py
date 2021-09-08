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