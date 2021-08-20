from collections import deque

if __name__=="__main__":
    n=int(input())
    graph=[list(map(int, input())) for _ in range(n)]

    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    visited = [[-1]*n for _ in range(n)]
    Q=deque()
    Q.append([0, 0])
    visited[0][0]=0

    while Q:
        a, b = Q.popleft()
        for i in range(4):
            x = a+dx[i]
            y = b+dy[i]

            if 0<=x<n and 0<=y<n and visited[x][y]==-1:
                if graph[x][y]==0:
                    visited[x][y]=visited[a][b]+1
                    Q.append([x,y])
                else:
                    visited[x][y]=visited[a][b]
                    Q.appendleft([x,y])
    print(visited[n-1][n-1])