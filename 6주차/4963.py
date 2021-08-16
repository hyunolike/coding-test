import sys
input=sys.stdin.readline
sys.setrecursionlimit(1000000)

dx=[-1,-1,-1,0,0,1,1,1]
dy=[-1,0,1,-1,1,-1,0,1]

def sol(x,y):
    visit[x][y]=1
    for i in range(8):
        mx=x+dx[i]
        my=y+dy[i]
        if (0<=mx<h) and (0<=my<w) :
            if (visit[mx][my]==False) and grid[mx][my]==1:
                sol(mx,my)
                
w,h=map(int,input().split())          
while w!=0 and h!=0:

    grid=[list(map(int,input().split())) for _ in range(h)]
    visit=[ [False]*w for _ in range(h) ]


    result=0
    for i in range(h):
        for j in range(w):
            if grid[i][j]==1 and visit[i][j]==False:
                sol(i,j)
                result+=1

    print(result)
    w,h=map(int,input().split())
