def DFS_solution():
    def DFS(x, y, ans):
        global answer

        answer = max(ans, answer)

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<r and 0<=ny<c and board[nx][ny] not in visit:
                visit.append(board[nx][ny])
                DFS(nx, ny, ans+1)
                visit.remove(board[nx][ny])

    r,c = map(int, input().split())
    board = list(list(map(str, input())) for _ in range(r))

    visit=[board[0][0]]
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    answer = 1
    DFS(0, 0, answer)
    print(answer)

def BFS_solution():
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    def BFS(x, y):
        global answer
        q = set([(x, y, board[x][y])])

        while q:
            x, y, alphas = q.pop()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if ((0 <= nx < R) and (0 <= ny < C)) and (board[nx][ny] not in alphas):
                    q.add((nx,ny,alphas + board[nx][ny]))
                    answer = max(answer, len(alphas)+1)


    R, C = map(int, input().split())
    board = [list(map(str, input())) for _ in range(R)]

    answer = 1
    BFS(0, 0)
    print(answer)