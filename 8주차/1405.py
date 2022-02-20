n,E,W,S,N=map(int,input().split())
percent=[E/100,W/100,S/100,N/100]
grid=[[0 for i in range(n*2+1)] for ii in range(n*2+1)]

dx=[1,-1,0,0]
dy=[0,0,-1,1]

def dfs(x,y,count):
    if count==n:
        return 1
    grid[x][y] = 1
    ret = 0
    for i in range(4):
        X = x+dx[i]
        Y = y+dy[i]
        if grid[X][Y]: 
            continue
        ret += dfs(X,Y,count+1)*percent[i] 
    grid[x][y] = 0
    return ret


print(dfs(n,n,0))