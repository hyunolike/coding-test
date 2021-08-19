import sys
import collections

n, m , r = map(int,sys.stdin.readline().split())

arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,-1,0,1]
day = 0
while(True):
    visited = [[1]*n for _ in range(n)]
    confirm_set = []
    change = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                people = 0
                
                ever = {i*n+j}
                stack = collections.deque([[i,j]])
                visited[i][j] = 0
                people += arr[i][j]
                while(len(stack)):
                    this_turn = stack.popleft()
                   
                    this_row = this_turn[0]
                    this_col = this_turn[1]
                    for k in range(4):
                        row = this_row + dx[k]
                        col = this_col + dy[k]
                        if 0 <= row < n and 0 <= col < n and visited[row][col]:
                            if m <= abs(arr[row][col] - arr[this_row][this_col]) <= r:
                                stack.append([row,col])
                                visited[row][col] = 0
                                ever.add(row*n+col)
                                people += arr[row][col]
                                change += 1
                length = len(ever)
                
                this_people = people // length
                for t in ever:
                    row = t//n
                    col = t%n
                    arr[row][col] = this_people
               
   
    if change == 0:
        print(day)
        break
    if change == n*n:
        print(day+1)
        break
    day+=1
    