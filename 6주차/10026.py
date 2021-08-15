import sys
sys.setrecursionlimit(100000000)
input=sys.stdin.readline
N=int(input())
grid=list()
for i in range(N):
    grid.append(input().rstrip())

def dfs(x,y,flag):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    stack[x][y]=-1
    for i in range(4):
        mx=x+dx[i]
        my=y+dy[i]
        if (0<=mx<N) and (0<=my<N) and (stack[mx][my]!=-1):
            if flag:
                if (grid[x][y]==grid[mx][my]) or (grid[x][y]=='R' and grid[mx][my]=='G') or (grid[x][y]=='G' and grid[mx][my]=='R'):
                    dfs(mx,my,True)
            else:
                if grid[x][y]==grid[mx][my]:
                    dfs(mx,my,False)


stack=[[0]*N for _ in range(N)]


count=0

for i in range(N): 
    for j in range(N): 
        if stack[i][j]==0: 
            count+=1 
            dfs(i, j,False)


stack=[[0]*N for _ in range(N)]

count2=0

for i in range(N): 
    for j in range(N): 
        if stack[i][j]==0: 
            count2+=1 
            dfs(i, j,True)
    

print(count,count2)
