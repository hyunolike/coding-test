import sys
import math


N = int(input())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


def pooling(matrix):
    l = len(matrix)
    k = l // 2
    ret = [[0] * k for _ in range(k)]
    nx = 0

    for x in range(0, l, 2):
        ny = 0
        for y in range(0, l, 2):
            window = [matrix[x][y], matrix[x + 1][y], matrix[x][y + 1], matrix[x + 1][y + 1]]
            window.sort(reverse=True)
            ret[nx][ny] = window[1]
            ny += 1
        nx += 1

    return ret


def solution():
    answer = matrix

    for _ in range(int(math.log2(N))):
        answer = pooling(answer)

    return answer[0][0]


print(solution())
