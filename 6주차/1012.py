
import sys
sys.setrecursionlimit(10000)
input=sys.stdin.readline
T=int(input())

def dfs(x,y):

    dx = [1, -1, 0, 0] 
    dy = [0, 0, 1, -1]
    for i in range(4):
        tx=x+dx[i]
        ty=y+dy[i]

        if (0 <= tx < M) and (0 <= ty < N):
            if table[tx][ty]==1:
                table[tx][ty]=-1
                dfs(tx,ty)

for _ in range(T):
    M,N,K = map(int,input().split())
    table=[[0]*N for _ in range(M)]
    for _ in range(K):
        x,y=map(int,input().split())
        table[x][y]=1
    count=0
    for i in range(M):
        for j in range(N):
            if table[i][j]>0:
                dfs(i,j)
                count=count+1
    print(count)


