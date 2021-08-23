#7562 나이트의 이동

"""
문제풀이 1: 전형적인 좌표계 움직임에서 움직임이 좀 남다르기 때문에 그거에 알맞게구현
2: visited + bfs = 정답

"""

import sys
inpuy = sys.stdin.readline
from collections import deque

dx = [-2,-1,1,2,2,1,-1,-2]
dy = [-1,-2,-2,-1,1,2,2,1]


N =int(input().rstrip())

for _ in range(N):
    arr = deque()
    size = int(input().rstrip())
    x,y = map(int,input().rstrip().split())
    ans_x,ans_y = map(int,input().rstrip().split())

    arr.append([x,y,0])
    visited = [[False]*size for _ in range(size)]
    visited[x][y] = True

    while arr:
        xx,yy,dd = arr.popleft()

        if ans_x == xx and ans_y == yy:
            print(dd)
            break
        
        for i in range(8):
            if 0<= xx+dx[i] < size and 0<= yy+dy[i] <size and not visited[yy+dy[i]][xx+dx[i]]:
                arr.append([xx+dx[i],yy+dy[i],dd+1])
                visited[yy+dy[i]][xx+dx[i]] = True