import sys
sys.setrecursionlimit(10 ** 8)

def DFS(x, y):
    if x==m-1 and y==n-1:
        return 1
    if visited[x][y] != -1:
        return visited[x][y]
    visited[x][y]=0

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    for i in range(4):
        a = x + dx[i]
        b = y + dy[i]

        if 0<=a<m and 0<=b<n and graph[a][b]<graph[x][y]:
            visited[x][y] += DFS(a, b)
        
    return visited[x][y]

if __name__=="__main__":
    m, n = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(m)]
    visited = [[-1]*n for _ in range(m)]
    print(DFS(0, 0))
    for a in visited:
        print(a)