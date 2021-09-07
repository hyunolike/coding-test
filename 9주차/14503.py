import sys
input=sys.stdin.readline

N,M=map(int,(input().split()))
r,c,d=map(int,input().split())
grid=[ list(map(int,input().split())) for _ in range(N)]

# 0북 1동 2남 3서
dx=[-1,0,1,0]
dy=[0,1,0,-1]

# def cleanable(xx,yy):
#     if grid[xx][yy]==0:
#         return True
#     for i in range(4):
#         mx=xx+dx[i]
#         my=yy+dy[i]
#         if 0<=mx<N and 0<=my<M:
#             if grid[mx][my]==0 or grid[mx][my]==2:
#                 return True
#     return False

count=0
while True:
    if grid[r][c]==0:
        grid[r][c]=2
        count+=1

    f1=False
    for _ in range(4):
        d-=1
        if d<0:
            d=3
        mr=r+dx[d]
        mc=c+dy[d]
        if 0<=mr<N and 0<=mc<M:
            if grid[mr][mc]==0:                
                r=mr
                c=mc
                f1=True
                break
    if f1==False:
        if grid[ r-dx[d] ][ c-dy[d] ]==1:
            print(count)
            break
        else:
            r=r-dx[d]
            c=c-dy[d]