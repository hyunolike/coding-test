#4963 섬의 개수



import sys
input =sys.stdin.readline
sys.setrecursionlimit(10000)


N = int(input().rstrip())
dx = [0,0,1,-1,1,1,-1,-1]
dy = [1,-1,0,0,1,-1,1,-1]

def dfs(x,y):
    a[x][y] = 0
    for i in range(8):
        nx,ny = x+dx[i],y+dy[i]
        if 0<=nx<h and 0<=ny<w and a[nx][ny] == 1:
            dfs(nx,ny)


while True:
    w,h = map(int,input().rstrip().split())
    if w == 0 and h == 0:
        break
    cnt = 0
    a = [list(map(int,input().split())) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if a[i][j] == 1:
                dfs(i,j)
                cnt += 1
    print(cnt)

