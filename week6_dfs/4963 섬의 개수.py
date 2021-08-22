import sys
from collections import deque
input = sys.stdin.readline

while True:
    w, h =map(int, input().split())
    if w==0 and h==0:
        break

    island = [list(map(int, input().split())) for _ in range(h)]

    # 기존 방향에 북동, 북서, 남동, 남서방향 추가
    dx=[-1,-1,0,1,1,1,0,-1]
    dy=[0,1,1,1,0,-1,-1,-1]

    q = deque()
    cnt = 0
    for i in range(h):
        for j in range(w):
            if island[i][j]==1: # 육지라면
                q.append((i,j))
                island[i][j]=2 # 큐에 넣고 방문표시

                while q: # 방문한 큐를 꺼내고
                    cx, cy = q.popleft()
                    for k in range(8): # 8방위 탐색
                        nx = cx+dx[k]
                        ny = cy+dy[k]

                        if 0<=nx<h and 0<=ny<w: # 지도 범위 안이며
                            if island[nx][ny]==1: # 육지값이면 바꾼 후 큐에 추가
                                q.append((nx,ny))
                                island[nx][ny]=2
                else: # 이어진 육지 확인 후 cnt+1
                    cnt+=1
    print(cnt)
