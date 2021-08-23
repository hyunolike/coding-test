import sys
import copy
from itertools import combinations
from collections import deque
input = sys.stdin.readline

n, m, d = map(int, input().split())
ogmap = [list(map(int, input().split())) for _ in range(n)]
archers = [i for i in range(m)]

# 궁수 위치 정하기 - 경우의 수
pos = deque(combinations(archers, 3))
# for p in pos:
#     print(p)
answer = 0

# 궁수 위치 Fix
for archer in pos: # 궁수가 0,1,2자리에 위치
    a,b,c = archer
    graph = copy.deepcopy(ogmap)
    shot, killed, cnt = 0, 0, 0

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while True:
        if cnt == n:
            break
        cnt += 1
        dead = set()
        for j in range(m): # 성벽 바로 앞부터 탐색
            stop = False
            for i in range(n-1, -1, -1): # 성벽 바로 앞부터 오른쪽 탐색
                distance = abs(n-i)+abs(a-j)
                if graph[i][j] == 1 and distance <= d: # 궁수 앞에 적 존재
                    graph[i][j]=0
                    # dead.add((i, j))
                    shot += 1
                    stop = True
                if stop:
                    break
            if stop:
                break
        for j in range(m): # 성벽 바로 앞부터 탐색
            stop = False
            for i in range(n-1, -1, -1): # 성벽 바로 앞부터 오른쪽 탐색
                distance = abs(n-i)+abs(b-j)
                if graph[i][j] == 1 and distance <= d: # 궁수 앞에 적 존재
                    graph[i][j]=0
                    # dead.add((i, j))
                    shot += 1
                    stop = True
                    break
                if stop:
                    break
            if stop:
                break
        for j in range(m): # 성벽 바로 앞부터 탐색
            stop = False
            for i in range(n-1, -1, -1): # 성벽 바로 앞부터 오른쪽 탐색
                distance = abs(n-i)+abs(c-j)
                if graph[i][j] == 1 and distance <= d: # 궁수 앞에 적 존재
                    graph[i][j]=0
                    # dead.add((i, j))
                    shot += 1
                    stop = True
                    break
                if stop:
                    break
            if stop:
                break
        for x, y in dead:
            graph[x][y]=0
            killed += 1

        # 궁수가 활을 다 쏘았으므로 적 1칸 전진
        for i in range(n-1, 0, -1):
            graph[i] = graph[i-1]
        graph[0] = [0 for _ in range(m)]

    if killed > answer:
        answer = killed

print(answer)