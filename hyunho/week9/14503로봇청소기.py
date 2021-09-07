import sys
input = sys.stdin.readline

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 방향 바꾸는 함수
def direction(d):
    if d==0: # 북 -> 서
        return 3
    elif d==1: # 동 -> 북 
        return 0
    elif d==2: # 남 -> 동
        return 1
    elif d==3: # 서 -> 남
        return 2


def solution(r, c, d):
    cnt = 1
    x, y = r, c
    arr[x][y] = 2
    while True:
        dc = d
        for _ in range(4):
            empty = 0
            dc = direction(dc)
            sx, sy = x+dx[dc], y+dy[dc]
            if 0<=sx<N and 0<=sy<M and arr[sx][sy] == 0:
                cnt += 1
                x, y, d = sx, sy, dc
                arr[sx][sy] = 2
                empty = 1
                # 청소를 하는데 성공했으면 for문을 빠져나가 다시 현재 위치 기준으로 왼쪽부터 
                break
        
        # 현재 위치 기준 동서남북 갈곳이 없을 경우, 후진을 해준다.
        if empty == 0:
            if d == 0:
                x += 1
            elif d == 1:
                y -= 1
            elif d == 2:
                x -= 1
            elif d == 3:
                y += 1
            # 후진을 했는데 벽이 있다면 더이상 갈곳 없으므로 멈춘다.
            if arr[x][y]==1:
                break
    return cnt
            


N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(solution(r, c, d))