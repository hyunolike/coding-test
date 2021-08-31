import sys
input=sys.stdin.readline
sys.setrecursionlimit(100000)
N=int(input().rstrip())
grid=[ list(map(int,input().split())) for _ in range(N) ]
visit2=[0]*N



def dfs(start,cur,cost):
    global r
    if start==cur and visit2.count(0)==0:
        r=min(cost,r)
        #print(r)
        return
    for i in range(N):
        if grid[cur][i]!=0 and visit2[i]!=1:
            visit2[i]=1
            dfs(start,i,cost+grid[cur][i])
            visit2[i]=0


r=sys.maxsize
dfs(0,0,0)
print(min(sys.maxsize,r))

