#16234 인구이동

"""
문제풀이 1: 좌표계 방향 이동 = 똑같음
2: 다른점은 어떻게 "국경선 동시 해방" 을 구현하느냐 가포인트
3: 따라서 조건을 만족하는것들을 tranfer(인구이동)에 집어넣어서 
인구이동이 있을떄까지 while 문을진행하고  인구수의 합도 같이 정리할수있따

개선포인트 : 1. 인구이동과 인구수 는 사실 같이 이용되므로 한쌍으로 사용하면 변수 줄일수있다.
2. 모든점을 기준으로 이동을하였는데 이것또한 dp로 줄일수 있을까?
하지만 조건이복잡해서 그냥 다했다....
하지만 여기서는 조건환경들이 계속바뀌기 때문에(ex)인구이동의 나라와 인구수)
안될꺼같아서 시도도 안했다.
dp and dfs 사이의 더많은경험이 필요할듯!

"""

import sys
input = sys.stdin.readline
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
N, L, R = map(int, input().split())
people = []
transfer = []
ans = 0
for _ in range(N):
    people.append(list(map(int, input().split())))

while True:
    Merge = False
    visited = [[False]*(N) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                arr = deque([i,j])
                visited[i][j] = True
                sum = arr[i][j]
                transfer = [[i,j]]

                while arr:
                    x,y = arr.popleft()
                    for k in range(4):
                        nx = x+dx[k]
                        ny = y+dy[k]
                        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                            if L <= abs(arr[x][y]-arr[nx][ny]) <= R:
                                visited[nx][ny] = True
                                arr.append([nx, ny])
                                transfer.append([nx,ny])
                                sum += arr[nx][ny]
                if len(transfer) > 1:
                    Merge = True
                    for x,y in transfer:
                        people[x][y] = sum // len(transfer)
    
    if Merge:
        ans += 1
    else:
        break
                        
print(ans)

