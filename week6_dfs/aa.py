
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def BFS(x, y):
    global answer
    q = set([(x, y, board[x][y])])

    while q:
        x, y, ans = q.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if ((0 <= nx < R) and (0 <= ny < C)) and (board[nx][ny] not in ans):
                q.add((nx,ny,ans + board[nx][ny]))
                answer = max(answer, len(ans)+1)

R, C = map(int, input().split())
board = [list(map(str, input())) for _ in range(R)]


answer = 1
BFS(0, 0)
print(answer)