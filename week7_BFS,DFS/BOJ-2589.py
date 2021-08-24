#2589 보물섬

"""
#bfs로풀이 = 큐
#dfs = recurion

문제풀이 1: visited 필수 = 두번이상지나가거나  
2. 최소값위주 = 멀리 돌아가서는 안됨
3. 서로 최단거리로 멀리있는것중 최대시간 = 보물 && 최대시간 = 정답


"""

import sys
input = sys.stdin.readline
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
Map = []
N,M = map(int,input().rstrip().split())
ans = 0
Map = [input().rstrip() for _ in range(N)]

def bfs(x,y):
    visited = [[0]*M for _ in range(N)]  #호출할때마다 넣을꺼면 반복문보다 여기넣으면 ok
    visited[x][y] = 1
    arr = deque([(x,y)])  # 초기화 구조 알아두기
    
    cnt = 0
    while arr:
#         print(visited)
        x,y =arr.popleft()
        for i in range(4):
            nx,ny = x+dx[i] , y+dy[i]
            if 0<= nx < N and 0 <= ny <M and visited[nx][ny] == 0 and Map[nx][ny] =="L":
                arr.append((nx,ny))
                visited[nx][ny] = visited[x][y] +1
                cnt = max(cnt,visited[nx][ny])
    return cnt -1

for i in range(N):
    for j in range(M):
        if Map[i][j] == "L":
            ans = max(bfs(i,j),ans)


print(ans)