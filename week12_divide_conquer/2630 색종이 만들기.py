import sys
input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
answer = []

def check(x, y, length):
    color = paper[x][y]
    for i in range(x, x+length):
        for j in range(y, y+length):
            if color != paper[i][j]:
                length = length//2
                check(x, y, length)
                check(x, y+length, length)
                check(x+length, y, length)
                check(x+length, y+length, length)
                return 0
    if color == 0:
        answer.append(0)
    else:
        answer.append(1)

check(0,0,n)
print(answer.count(0))
print(answer.count(1))