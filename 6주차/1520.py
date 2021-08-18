import sys
input=sys.stdin.readline
sys.setrecursionlimit(2000)


def sol(x,y):
    if x==N-1 and y==M-1:
        return 1
    if stack[x][y]!=-1:
        return stack[x][y]
    stack[x][y]=0
    for i in range(4):
        mx=x+dx[i]
        my=y+dy[i]
        if (0<=mx<N) and (0<=my<M):
            if (grid[mx][my])<(grid[x][y]):
                stack[x][y]+=sol(mx,my)
    return stack[x][y]


N,M=map(int,input().split())
grid=[ list(map(int,input().split())) for _ in range(N) ]
stack=[ [-1]*M for _ in range(N) ]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
print(sol(0,0))

# 4 5
# 50 45 37 32 30
# 35 50 40 20 25
# 30 30 25 17 28
# 27 24 22 15 10

# 10 10
# 20 19 18 17 16 15 14 13 12 11 
# 19 18 17 16 15 14 13 12 11 10 
# 18 17 16 15 14 13 12 11 10  9 
# 17 16 15 14 13 12 11 10  9  8 
# 16 15 14 13 12 11 10  9  8  7 
# 15 14 13 12 11 10  9  8  7  6 
# 14 13 12 11 10  9  8  7  6  5 
# 13 12 11 10  9  8  7  6  5  4 
# 12 11 10  9  8  7  6  5  4  3 
# 11 10  9  8  7  6  5  4  3  2


