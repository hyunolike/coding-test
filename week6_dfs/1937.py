import sys
sys.setrecursionlimit(25000)
def dfs(x,y):
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = 1
    count = 0
    this_turn = []
    for i in range(4):
        row = x + dx[i]
        col = y + dy[i]
        if 0<=row<n and 0<=col<n and arr[x][y] < arr[row][col]:
            result = dfs(row,col)
            try: 
                compare = this_turn.pop()
                if result>compare:
                    this_turn.append(result)
                else:
                    this_turn.append(compare)
            except:
                this_turn.append(result)
            
            count+=1
    
    if count == 0:
        return dp[x][y]
    dp[x][y] += this_turn.pop()
    return dp[x][y]
   

n = int(sys.stdin.readline())

arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]


dp = [[-1]*n for _ in range(n)]
max = 0

for i in range(n):
    for j in range(n):
        if dp[i][j]== -1:
            real = dfs(i,j)
            if real> max:
                max = real

print(max)