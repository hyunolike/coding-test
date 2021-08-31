# 1. 최대 운동장 만들기
# 2. 각 방향의 확률 처리
# 3. 파라미터 처리
# 4. ...


import sys
sys.setrecursionlimit(10**6)

def search(x, y, p , count):
    global total
    if count == num:
        total += p
        return
    now = p
    ground[x][y] = 1 # 현재 방문 좌표 체크
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 2*num+1 and 0 <= ny < 2*num+1:
            if ground[nx][ny] == 1: #이미 방문했다면
                continue
            else:
                search(nx, ny, now*percent[i], count + 1)
                ground[nx][ny] =  0 # 현재지점의 방문체크 0으로 되돌리기

num, e, w, s, n = map(int,input().split())

percent = [e/100, w/100, s/100, n/100]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

ground = [[0] * (2*num + 1) for _ in range(2*num+1)] # 운동장의 크기
total = 0
search(num, num, 1, 0) # num, num 가운데 이자 로봇의 최초지점, 1은 곱해나갈 확률(최초), 횟수

print(total)