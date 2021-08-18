from sys import setrecursionlimit 
setrecursionlimit(10**9)

def DFS(x,y):
    if visited[x][y]!=-1:
        return visited[x][y]
    
    visited[x][y]=0
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    for i in range(4):
        a = x+dx[i]
        b = y+dy[i]
        
        if 0<=a<n and 0<=b<n:
            if forest[a][b]>forest[x][y]:
                visited[x][y] = max(visited[x][y], DFS(a,b))
    visited[x][y]+=1

    return visited[x][y]

if __name__=="__main__":
    n=int(input())
    forest=[list(map(int, input().split())) for _ in range(n)]
    visited = [[-1]*n for _ in range(n)]
    answer = 0
    for i in range(n):
        for j in range(n):
            answer = max(answer, DFS(i,j))
    print(answer)