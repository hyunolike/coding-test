import sys
import collections


   
n = int(sys.stdin.readline())

arr = [list(map(int,sys.stdin.readline().strip())) for _ in range(n)]



dp = [[n*n] * n for _ in range(n)]


dx = [-1,0,1,0]
dy = [0,1,0,-1]



stack = collections.deque([[0,0,0]])

while(len(stack)):
    this_turn = stack.popleft()
    this_row = this_turn[0]
    this_col = this_turn[1]
    
    for i in range(4):
        row = this_row + dx[i]
        col = this_col + dy[i]
        if 0 <= row < n and 0 <= col < n :
            if arr[row][col] == 1:
                if dp[row][col] > this_turn[2]:
                    stack.append([row,col,this_turn[2]])
                    dp[row][col] = this_turn[2]
            else:
                if dp[row][col] > this_turn[2] + 1:
                    stack.append([row,col,this_turn[2]+1])
                    dp[row][col] = this_turn[2]+1
print(dp[n-1][n-1])
