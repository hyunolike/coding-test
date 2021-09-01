import sys
sys.setrecursionlimit(10**6)

board = [list(map(int, input().split())) for _ in range(9)]
zeros = [(i,j) for i in range(9) for j in range(9) if board[i][j] == 0]

def get_possible(r, c):
    possible = set(range(1, 10))
    possible -= set(board[r])
    test = set()
    for i in range(9):
        test.add(board[i][c])
    possible -= test
    for i in range(r//3*3, r//3*3+3):
        for j in range(c//3*3, c//3*3+3):
            test.add(board[i][j])
    possible -= test
    return tuple(possible)

def solve(i):
    if i == len(zeros):
        [print(*row) for row in board]
        sys.exit()
    r, c = zeros[i]
    possibles = get_possible(r, c)
    for num in possibles:
        board[r][c] = num
        solve(i+1)
        board[r][c] = 0
solve(0)


