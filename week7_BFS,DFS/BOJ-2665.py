#2665 미로 만들기

"""
문제풀이 1: 시작 - 끝방 을 가는 모든 루트중에 검은색을 가장적게 지나는 루트가 정답
#2. 
"""
import sys
input = sys.stdin.readline
from collections import deque
N = int(input().rstrip())
Map = [list(map(int,input().rstrip()))for _ in range(N)]
visited = [[-1]*N for _ in range(N)] 
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(x,y):
    arr = deque([[x,y]])  
    visited[x][y] = 0


    while arr:
        x,y = arr.popleft()
        for i in range(4):
            nx ,ny = x + dx[i], y+dy[i]
            if 0<= nx < N and 0 <= ny <N :
                if visited[nx][ny] == -1:
                    if Map[nx][ny] == 0:
                        visited[nx][ny] = visited[x][y] + 1
                        arr.appendleft([nx,ny])
                    else:
                        visited[nx][ny] = visited[x][y] 
                        arr.append([nx,ny])

                        # appendleft 쓰는 이유 알아두기~
bfs(0,0)
print(visited[N-1][N-1])
                
