import sys
input = sys.stdin.readline

n, m = map(int, input().split())
k=int(input())
graph = [list(map(str, input())) for _ in range(n)]

J=[[0]*(m+1) for _ in range(n+1)]
O=[[0]*(m+1) for _ in range(n+1)]
I=[[0]*(m+1) for _ in range(n+1)]

for i in range(n):
    for j in range(m):
        J[i+1][j+1] = J[i+1][j]+J[i][j+1]-J[i][j]
        O[i+1][j+1] = O[i+1][j]+O[i][j+1]-O[i][j]
        I[i+1][j+1] = I[i+1][j]+I[i][j+1]-I[i][j]
        
        if graph[i][j]=='J':
            J[i+1][j+1]+=1
        elif graph[i][j]=='O':
            O[i+1][j+1]+=1
        elif graph[i][j]=='I':
            I[i+1][j+1]+=1

for _ in range(k):
    a,b,c,d = map(int, input().split())
    cnt_J,cnt_O,cnt_I = 0,0,0

    cnt_J = J[c][d]-J[a-1][d]-J[c][b-1]+J[a-1][b-1]
    cnt_O = O[c][d]-O[a-1][d]-O[c][b-1]+O[a-1][b-1]
    cnt_I = I[c][d]-I[a-1][d]-I[c][b-1]+I[a-1][b-1]
    print(cnt_J, cnt_O, cnt_I)
