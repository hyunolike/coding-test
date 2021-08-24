from sys import stdin
input = stdin.readline
from collections import deque
from itertools import combinations

# 상 좌 우
dr = (0, -1, 0)
dc = (-1, 0, 1)

# 궁수가 있는 열
def killEnemy(pos, A):
    enemyLst = set()   # 죽일 적의 후보 위치 리스트 - 중복 제거를 위해 set 사용
    
    check = [[-1] * M for _ in range(N)]        # 궁수별 적 찾는 visited를 공유하기 위함
    for col in pos:
        if A[N-1][col]:     # 탐색 시작 위치에 적이 있는 경우 가장 가까운 적임
            enemyLst.add((N-1, col))
            continue

        check[N-1][col] = col
        Q = deque([(N-1, col, 1)])      # (위치, 거리)
        flag = False
        while Q:
            r, c, dis = Q.popleft()
            if dis == D:     # 거리 공격 제한 거리 D 넘으면
                break
            for d in range(3):
                nr = r + dr[d]
                nc = c + dc[d]
                if not (0 <= nr < N and 0 <= nc < M) or check[nr][nc] == col:
                    continue
                check[nr][nc] = col
                Q.append((nr, nc, dis+1))
                if A[nr][nc]:       # 가장 처음 만난 적을 enemyLst에 담기
                    enemyLst.add((nr, nc))
                    flag = True
                    break
            if flag:
                break
    return enemyLst

# 궁수의 공격
def attack(pos):
    global maxKill
    A = [x[:] for x in raw]     # 궁수 배치 후 사용할 맵 A에 복사
    killCnt = 0                 # 죽인 적의 수
    
    for _ in range(N):
        enemyLst = killEnemy(pos, A)    # 죽일 후보 적의 위치 리스트

        # 적 죽이기
        for er, ec in enemyLst:     # 타겟 적 죽이기
            A[er][ec] = 0
            killCnt += 1
        
        # 적 한 칸씩 아래로 이동
        A.pop()
        A.insert(0, [0] * M)

    maxKill = max(maxKill, killCnt)     # 최댓값 갱신

# (방법 1) 재귀로 조합 구현 => 3명의 궁수 배치 경우의 수 구하기
# def posArcher(depth, k):
#     global maxKill
#     if maxKill == enemyCnt:     # 이미 다 죽였으면
#         return

#     if depth == 3:
#         attack(castle)
#         return

#     for i in range(k, M):
#         castle.append(i)
#         posArcher(depth+1, i+1)
#         castle.pop()

# main
N, M, D = map(int, input().split())
enemyCnt = 0        # 맵에 있는 모든 적의 수
raw = []
for r in range(N):
    raw.append(list(map(int, input().split())))
    for c in range(M):
        if raw[r][c]:
            enemyCnt += 1
maxKill = 0

# 방법 1 - dfs 재귀로 조합 구현
# castle = []
# posArcher(0, 0)

# 방법 2 - itertools 패키지의 combination 라이브러리 사용
for comb in combinations(range(M), 3):
    attack(comb)
    if maxKill == enemyCnt:     # 이미 다 죽였으면
        break
print(maxKill)