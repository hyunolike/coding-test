import sys
input=sys.stdin.readline
N,M=map(int,input().split())
square=[list(map(int,input().split())) for _ in range(N)]
op=[list(map(int,input().split())) for _ in range(M)]


squareSum=[[0]*(N+1) for _ in range(N)]


for i in range(N):
    temp=0
    for j in range(N):
        temp+=square[i][j]
        squareSum[i][j+1]=temp


for x1,y1,x2,y2 in op:
    res=0
    for i in range(x1,x2+1):
        res += (squareSum[i-1][y2] - squareSum[i-1][y1-1])
    print(res)