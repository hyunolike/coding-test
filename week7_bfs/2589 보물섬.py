from collections import deque

if __name__=="__main__":
    # L은 육지, W는 바다
    n,m = map(int, input().split())
    graph=[list(map(str, input())) for _ in range(n)]

    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    answer = 0

    for i in range(n):
        for j in range(m):
            dist = 0
            if graph[i][j]=='L':
                Q=deque()
                Q.append([i, j])
                visited = [[0]*m for _ in range(n)]
                visited[i][j] = 1

                while Q:
                    a, b = Q.popleft()
                    for k in range(4):
                        x = a+dx[k]
                        y = b+dy[k]
                        if 0<=x<n and 0<=y<m:
                            if graph[x][y]=='L' and visited[x][y]==0:
                                visited[x][y]=visited[a][b]+1
                                dist = max(dist, visited[x][y]-1)
                                Q.append([x, y])
            if dist !=0:
                answer = max(answer, dist)
    print(answer)