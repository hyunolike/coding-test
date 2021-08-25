import copy
import sys

input = sys.stdin.readline


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
max_value = 0
virus_list = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            virus_list.append([i,j])

def select_wall(start, count):
    global max_value
    if count == 3:
        select_arr = copy.deepcopy(arr)
        for num in range(len(virus_list)):
            x, y = virus_list[num]
            spread_virus(x, y, select_arr)
        safe_counts = sum(i.count(0) for i in select_arr)
        max_value = max(max_value, safe_counts)
        return True
    else:
        for i in range(start, N*M): # 조합 구하기
            x = i // M
            y = i % M
            if arr[x][y] == 0:
                arr[x][y] = 1
                select_wall(i, count + 1)
                arr[x][y] = 0

def spread_virus(x, y, select_arr):
    if select_arr[x][y] == 2:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if select_arr[nx][ny] == 0:
                    select_arr[nx][ny] = 2
                    spread_virus(nx, ny, select_arr)

select_wall(0,0)
print(max_value)