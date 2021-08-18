import sys
from collections import deque

def bfs(i, j, color, arr):
    queue = deque()
    queue.append((i, j)) #[i][j] 부터 bfs 시작
    arr[i][j] =0   # 방문 처리

    while queue:
        x, y = queue.popleft()
        for i in range(4): # 상,하,좌,우
            nx = x+dx[i]
            ny = y+dy[i]
            if nx <0 or nx>=n or ny<0 or ny>=n:
                continue # 인덱스가 범위를 벗어난 경우
            if arr[nx][ny] == color:
                arr[nx][ny] = 0
                queue.append((nx, ny))

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(sys.stdin.readline())
matrix = [list(sys.stdin.readline()) for _ in range(n)] # 적록색약 아닌 경우
matrix_rg = [[0] * n for _ in range(n)] # 적록색약인 경우

# 적록색약의 matrix(초록색을 모두 빨간색으로 바꿈)
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'R' or matrix[i][j] =='G':
            matrix_rg[i][j] = 'R'
        else:
            matrix_rg[i][j] = 'B'


num = 0
num_rg = 0
for i in range(n):
    for j in range(n):
        # 적록색약 아닌 사람
        if matrix[i][j] !=0:
            bfs(i, j, matrix[i][j], matrix)
            num +=1
        # 적록색약인 경우
        if matrix_rg[i][j] !=0:
            bfs(i, j, matrix_rg[i][j], matrix_rg)
            num_rg+=1

print(num, num_rg)
