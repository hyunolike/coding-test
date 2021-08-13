import sys
sys.setrecursionlimit(10**6)
input = lambda : sys.stdin.readline()

def dfs(x, y):
    if x <= -1 or x >= M or y <= -1 or y >= N:
        return False
    if arr[x][y] == 1:
        arr[x][y] = 0
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

T = int(input())

for _ in range(T):

    M, N, K = map(int, input().split())
    arr = [[0] * N for _ in range(M)]


    for _ in range(K):
        n, m = map(int, input().split())
        arr[n][m] = 1
    result = 0

    for i in range(M):
        for j in range(N):
            if dfs(i, j) == True:
                result += 1

    print(result)