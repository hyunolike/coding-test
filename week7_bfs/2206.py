import sys
import collections
n, m = map(int,sys.stdin.readline().split())

arr = [list(map(int,sys.stdin.readline().strip())) for _ in range(n)]

dp = []

for i in range(n):
    dp.append([])
    for j in range(m):
        dp[i].append([])
        for k in range(2):
            dp[i][j].append([k,n*m])

q = collections.deque([(0,0,1,0)])
dx = [-1,0,1,0]
dy = [0,1,0,-1]
while q:
    this_row, this_col, length, possible = q.popleft()
    for i in range(4):
        row = this_row + dx[i]
        col = this_col + dy[i]
        if 0 <= row < n and 0 <= col < m:
            if arr[row][col]:
                if possible == 0:
                    if dp[row][col][1][1] > length + 1:
                        dp[row][col][1][1] = length + 1
                        q.append((row,col,length+1,1))
            else:
                if dp[row][col][possible][1] > length + 1:
                    dp[row][col][possible][1] = length + 1
                    q.append((row,col,length+1,possible))
if n==1 and m==1:
    print(1)
    sys.exit()
if dp[n-1][m-1][0][1] == n*m and dp[n-1][m-1][1][1]== n*m:
    print(-1)
else:
    
    print(min(dp[n-1][m-1][0][1], dp[n-1][m-1][1][1]))
