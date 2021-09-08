n, m, x, y, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
commands = list(map(int, input().split()))

# dx=[1,-1,0,0]
# dy=[0,0,-1,1]
dx=[0,0,-1,1] # x좌표가 북쪽으로부터 떨어진 개수. 위아래. 
dy=[1,-1,0,0] # y좌표가 서쪽으로부터 떨어진 개수. 좌우
dice=[0,0,0,0,0,0]

for dir in commands:
    nx = x + dx[dir-1]
    ny = y + dy[dir-1]
    
    if not (0<=nx<n and 0<=ny<m):
        continue

    if dir == 1:
        dice[0],dice[1],dice[2],dice[5] = dice[5],dice[0],dice[1],dice[2]
    elif dir == 2:
        dice[0],dice[1],dice[2],dice[5] = dice[1],dice[2],dice[5],dice[0]
    elif dir == 3:
        dice[1],dice[3],dice[4],dice[5] = dice[4],dice[1],dice[5],dice[3]
    else:
        dice[1],dice[3],dice[4],dice[5] = dice[3],dice[5],dice[1],dice[4]
    
    if graph[nx][ny] == 0:
        graph[nx][ny] = dice[1]
    else:
        dice[1] = graph[nx][ny]
        graph[nx][ny] = 0
    
    x, y = nx, ny
    print(dice[5])