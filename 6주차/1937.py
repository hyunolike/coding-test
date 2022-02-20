import sys
input=sys.stdin.readline
sys.setrecursionlimit(100000)

n=int(input().rstrip())


bamboo=[ list(map(int,input().split())) for _ in range(n) ]
stack=[[-1]*n for _ in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def sol(x,y):
    if stack[x][y]!=-1:
        return stack[x][y]
    stack[x][y]=0
    for i in range(4):
        mx=x+dx[i]
        my=y+dy[i]
        if (0<=mx<n) and (0<=my<n):
            if bamboo[mx][my]>bamboo[x][y]:
                stack[x][y]=max(stack[x][y],sol(mx,my))
    stack[x][y]+=1   
    return stack[x][y]
    



result=0
for i in range(n):
    for j in range(n):
        if stack[i][j]==-1:
            result=max(result,sol(i,j))
print(result)

