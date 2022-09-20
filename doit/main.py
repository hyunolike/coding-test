import sys
input = sys.stdin.readline

n,m = map(int, input().split())
table = [[0]*(n+1) for _ in range(n+1)]
psum = [[0]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    tsum = list(map(int, input().split()))
    for j in range(1, n+1):
        table[i][j] = tsum[j-1]

for i in range(1, n+1):
    for j in range(1, n+1):
        psum[i][j] = psum[i][j-1]+psum[i-1][j]-psum[i-1][j-1]+table[i][j]

for _ in range(m):
    x1,y1,x2,y2 = map(int, input().split())
    print(psum[x2][y2]-psum[x1-1][y1-1])