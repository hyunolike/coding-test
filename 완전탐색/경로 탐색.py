def DFS(v):
    global answer
    if v==n-1:
        answer+=1
        return 0
    else:
        for i in range(n):
            if graph[v][i] and not visited[i]:
                visited[i]=1
                DFS(i)
                visited[i]=0

n,m=map(int,input().split())
edge=[list(map(int, input().split())) for _ in range(m)]
graph=[[0]*n for _ in range(n)]
visited=[0]*n
visited[0]=1
answer=0
for i,j in edge:
    graph[i-1][j-1]=1

DFS(0)
print(answer)