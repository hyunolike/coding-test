import sys
import collections

n, m = map(int,sys.stdin.readline().split())

arr = [list(sys.stdin.readline().strip()) for _ in range(n)]



dx = [-1,0,1,0]
dy = [0,1,0,-1]
real_max = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L':
            visited = [[1]*m for _ in range(n)]
            visited[i][j] = 0
            stack = collections.deque([[i,j,0]])
            max_len = 0
            while(len(stack)):
                this_turn = stack.popleft()
                this_row = this_turn[0]
                this_col = this_turn[1]
                count = 0
                for k in range(4):
                    row = this_row + dx[k]
                    col = this_col + dy[k]
                    if 0 <= row < n and 0 <= col < m and arr[row][col] =='L' and visited[row][col]:
                        visited[row][col] = 0
                        stack.append([row,col,this_turn[2]+1])
                        count += 1
                if count == 0 :
                   
                    max_len = max(max_len, this_turn[2]) 
            real_max = max(real_max, max_len)
print(real_max)  