import sys
from collections import deque
def bfs(i, j, visit):
    que = deque([[i, j]])
    melting_que = deque() # 빙하가 녹는 위치와 녹는 정도를 저장하는 큐
    visit[i][j] = 1
    while que:
        i, j = que.popleft()
        melt_cnt = 0
        for d_x, d_y in direction:
            next_x = i+d_x
            next_y = j+d_y
            if 0 <=next_x <= x-1 and 0<=next_y <= y-1 and visit[next_x][next_y] ==0:
                # 빙산의 높이가 있고 방문을 안했을 경우 que에 값 넣어주기
                if glacier[next_x][next_y]!=0:
                    visit[next_x][next_y] = 1 # 방문 체크
                    que.append([next_x, next_y])
                # 사방향 탐색 시 0일 경우 melt_cnt 증가
                else:
                    melt_cnt+=1
        if melt_cnt:
            melting_que.append([i, j, melt_cnt])
    return melting_que

input = sys.stdin.readline
year = 0 # 몇 년이 지났는지
x, y = map(int, input().split())
glacier = [[int(n) for n in input().split()] for _ in range(x)]
direction = ((1, 0), (-1, 0), (0,-1), (0,1)) # 동서남북
# 반복문 종료 조건 -> 빙산의 개수가 0이거나 2
while True:
    cnt =0 # 빙산의 개수를 담는 cnt 변수
    visit = [[0 for _ in range(y)] for _ in range(x)] # bfs를 위한 탬삭 확인 리스트
    for i in range(x-1):
        for j in range(y-1):
            if glacier[i][j] !=0 and visit[i][j] ==0: # 빙하의 높이가 남아있고 방문하지 않을 경우
                cnt+=1 # 빙산의 개수 추가
                melt = bfs(i, j, visit) # bfs 시작을 하고 각 좌표별로 녹는 정도 반환
                while melt:
                    m_x, m_y, m = melt.popleft()
                    glacier[m_x][m_y] = max(glacier[m_x][m_y]-m, 0)
    if cnt==0:
        year=0
        break
    if cnt>=2:
        break
    year+=1 # 일년 증가
    # 빙산의 갯수가 0이거나 2일 경우 반복문 종료
print(year)