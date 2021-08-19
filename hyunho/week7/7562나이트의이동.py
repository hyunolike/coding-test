from collections import deque
import sys
input = lambda : sys.stdin.readline()

def bfs(x, y, a, b):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        if x == a and y == b:
            print(graph[x][y])
            return

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < I and 0 <= ny < I and graph[nx][ny] == '':
                graph[nx][ny] = graph[x][y] + 1
                if nx == a and ny == b:
                    print(graph[nx][ny])
                    return
                queue.append((nx,ny))

dx = [-1,-2,-2,-1,1,2,2,1]
dy = [-2,-1,1,2,2,1,-1,-2]

for _ in range(int(input())):
    I = int(input())
    graph = [[''] * I for _ in range(I)]
    x, y = map(int,input().split())
    a, b = map(int, input().split())
    graph[x][y] = 0
    bfs(x, y, a, b)
