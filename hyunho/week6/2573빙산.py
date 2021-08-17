import sys

sys.setrecursionlimit(20000)
readline = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

N, M = map(int, input().split())

fields = [list(map(int, readline().split())) for _ in range(N)]
ices = []

# 빙산이 몇 개 연결되어 있는지 계산해주는 함수
# 몇 개 연결되어 있는지 계산하면서 녹인다.
def dfs(c_y, c_x, visited):
    cur_added = 0
    visited[c_y][c_x] = 1
    melt_num = 0
    for c_d in range(4):
        n_y, n_x = c_y + dy[c_d], c_x + dx[c_d]

        if visited[n_y][n_x]:
            continue

        if fields[n_y][n_x]:
            cur_added += dfs(n_y, n_x, visited)
        else:
            melt_num += 1
    else:
        if fields[c_y][c_x] - melt_num > 0:
            fields[c_y][c_x] -= melt_num
        else:
            fields[c_y][c_x] = -1

    return cur_added + 1

# 빙산에 대한 정보를 ices 리스트에 넣어둔다.
for n in range(N):
    for m in range(M):
        if fields[n][m]:
            ices.append((n, m))

isFinished = False
year = 0

while ices:
    new_ices = []

    # 지금 빙산들이 다 연결되어 있는지 계산
    cur_num = dfs(ices[0][0], ices[0][1], [[0 for _ in range(M)] for _ in range(N)])
    # 현재 남아 있는 빙산의 수와 임의의 위치에서 DFS를 순회한 결과가 다르다면 끝
    if cur_num != len(ices):
        break
    else:
        # 이번 턴에 다 녹은 빙산의 위치 값을 0으로 바꿔줌
        for i_y, i_x in ices:
            if fields[i_y][i_x] == -1:
                fields[i_y][i_x] = 0
            else:
                new_ices.append((i_y, i_x))

        if len(new_ices):
            year += 1
            ices = new_ices
        else:
            year = 0
            break

print(year)