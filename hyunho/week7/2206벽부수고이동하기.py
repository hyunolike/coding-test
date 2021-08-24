import sys
from collections import deque

input = lambda : sys.stdin.readline()

N, M = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]


def bfs(x, y, crash, visited, arr):
    # crash 0 : 벽안부시고 가는 경우 , 1: 벽 부신 경우
    q = deque()
    q.append((x, y, crash))
    visited[x][y][crash] = 1

    while q:
        cur_x, cur_y, crash = q.popleft()
        if cur_x == N - 1 and cur_y == M - 1:
            return visited[cur_x][cur_y][crash]
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            # 벽 안부수고 이동
            if arr[nx][ny] == 0 and visited[nx][ny][crash] == 0:
                visited[nx][ny][crash] = visited[cur_x][cur_y][crash] + 1
                q.append((nx, ny, crash))

            # 벽 부수고 이동
            if crash == 0 and arr[nx][ny] == 1:
                visited[nx][ny][crash+1] = visited[cur_x][cur_y][crash] + 1
                q.append((nx, ny, crash + 1))
    return -1

print(bfs(0,0,0,visited, arr))