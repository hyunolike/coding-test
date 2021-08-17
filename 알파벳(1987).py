
# BFS 로 문제풀이

from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]



def bfs():
    max_length = 1
    queue = set([(0, 0, board[0][0])]) # queue가 중복을 허용하게 되면 시간 초과가 뜨기 때문에 set로 처리.

    while queue:
        x, y, visited = queue.pop()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=R or ny<0 or ny>=C:
                continue
            elif board[nx][ny] not in visited:
                next_visited = visited+board[nx][ny]
                queue.add((nx, ny, next_visited))
                max_length = max(max_length, len(next_visited))
    return max_length

R, C = map(int, input().split())
board = []
for _ in range(R):
    board.append(list(input()))

print(bfs())