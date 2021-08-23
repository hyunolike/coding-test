import sys
import collections
n, m, k = map(int,sys.stdin.readline().split())

arr = [list(map(int,sys.stdin.readline().split())) for _ in range(k)]

ptr = [[0]*m for _ in range(n)]
result = []
for i in arr:
    
    start_x = i[0]
    finish_x = i[2]

    start_y = i[1]
    finish_y = i[3]
  
    for row in range(start_y, finish_y):
        for col in range(start_x,finish_x):
            ptr[row][col] =1
visited = [[1] * m for _ in range(n)]
q = collections.deque([])

dx = [-1,0,1,0]
dy = [0,1,0,-1]

for i in range(n):
    for j in range(m):
        if ptr[i][j] == 0 and visited[i][j]:
            count = 1
            visited[i][j] = 0
            q.append((i,j))
            while q:
                this_row, this_col = q.popleft()
                for t in range(4):
                    row = this_row + dx[t]
                    col = this_col + dy[t]
                    if 0 <= row < n and 0 <= col < m and ptr[row][col] == 0 and visited[row][col]:
                        visited[row][col] = 0
                       
                        q.append((row,col))
                        count+=1
            result.append(count)
result.sort()

print(len(result))
for i in result:
    print(i,'',end='')