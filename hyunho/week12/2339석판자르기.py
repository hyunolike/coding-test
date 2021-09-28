import sys
N = int(input())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


def solve(sy, sx, ey, ex, direction):
    count = [0] * 3
    for i in range(sy, ey + 1):
        for j in range(sx, ex + 1):
            if table[i][j]:
                count[table[i][j]] += 1
    if count[1] < count[2] - 1:
        return 0
    elif count[1] == 0 and count[2] == 1:
        return 1

    out = 0
    # 0이 가로로 1이 세로로 자르는 경우
    if direction != 1:
        for row in range(sy + 1, ey):
            isDirty, isCrystal = False, False
            for col in range(sx, ex + 1):
                if table[row][col] == 1:
                    isDirty = True
                elif table[row][col] == 2:
                    isCrystal = True
            if isDirty and not isCrystal:
                out += solve(sy, sx, row - 1, ex, 1) * solve(row + 1, sx, ey, ex, 1)
    if direction != 0:
        for col in range(sx + 1, ex):
            isDirty, isCrystal = False, False
            for row in range(sy, ey + 1):
                if table[row][col] == 1:
                    isDirty = True
                elif table[row][col] == 2:
                    isCrystal = True
            if isDirty and not isCrystal:
                out += solve(sy, sx, ey, col - 1, 0) * solve(sy, col + 1, ey, ex, 0)
    return out


result = solve(0, 0, N-1, N-1, -1)
print(result if result else -1)
