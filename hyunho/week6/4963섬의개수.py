import sys
sys.setrecursionlimit(10**6)
input = lambda : sys.stdin.readline()

while True:
    n ,m = map(int, input().split())
    if n == 0 and m == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(m)]

    def dfs(x,y):
        # print(graph)
        if x <= -1 or x >= m or y <= -1 or y >= n:
            return False
        if graph[x][y] == 1:
            graph[x][y] = 0
            dfs(x - 1, y - 1)
            dfs(x - 1, y)
            dfs(x - 1, y + 1)
            dfs(x, y - 1)
            dfs(x, y + 1)
            dfs(x + 1, y - 1)
            dfs(x + 1, y)
            dfs(x + 1, y + 1)
            return True
        return False

    result = 0
    for i in range(m):
        for j in range(n):
            if dfs(i,j):
                result += 1

    print(result)


