# 지렁이가 이동하면서 인접 배추들을 보호해준다.
# 모든 배추를 보호할 수 있는 최소 지렁이의 수를 구하는 문제
# 인접 배추들은 다 지렁이 하나로 계산해서 더하면 된다.
# 0,0 오른쪽과 아래쪽만 볼 수 있음.
# 0, m 왼쪽과 아래쪽
# n,0 위쪽과 오른쪽
# m, n 왼쪽과 위쪽

# 맨 윗줄 = 왼쪽, 오른쪽, 아래
# 맨 왼쪽 = 위쪽, 아래쪽, 오른쪽
# 맨 오른쪽 = 왼쪽, 위쪽, 아래쪽
# 맨 아래 = 위쪽, 왼쪽, 오른쪽

# 나머지는 다 안에 있는거니깐 상화좌우 모두 탐색

# 1이 하나 있으면 그것을 쭉 타고 가서 모두 1을 0으로 바꾸면서 더이상 볼 필요가 없다는 것을 표시



# BFS를 사용하여 해결
import sys
from collections import deque
T = int(input()) # 테스트 케이스 수


# 상하좌우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
def bfs(graph, y, x):
    queue = deque()
    queue.append([y, x]) # ??????
    graph[y][x] = 0

    while queue:
        now_y, now_x = queue.popleft()
        for i in range(4):
            ny = now_y + dy[i]
            nx = now_x + dx[i]
            if 0<= ny < n and 0<=nx <m:
                if graph[ny][nx]==1:
                    queue.append([ny, nx])
                    graph[ny][nx] = 0

# 케이스
for _ in range(T):
    # 가로길이 m, 세로길이 n, 배추개수 k
    m, n, k = map(int, input().split())

    graph = [[0] * m for _ in range(n)] # 0으로 구성된 그래프 만들어주기

    # 배추인거 1 집어넣어주기
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    # 필요한 지렁이 수
    worm = 0

    for y in range(n):
        for x in range(m):
            if graph[y][x] ==1:
                worm +=1
                bfs(graph, y,x)
    print(worm)