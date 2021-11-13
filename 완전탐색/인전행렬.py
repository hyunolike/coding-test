n,m=map(int, input().split())
graph=[list(map(int, input().split())) for _ in range(m)]
result=[[0]*n for _ in range(n)]

for i, j, val in graph:
    result[i-1][j-1]=val

for i in range(n):
    for j in range(n):
        print(result[i][j], end=' ')
    print()
