import sys
import collections

n,m = map(int,sys.stdin.readline().split())

arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
count_1 = 0
stack = collections.deque([])
del_stack = collections.deque([])

while(True):
    count_1 += 1
    count = 0
    visited = set()
    for i in range(1,n-1):
        for j in range(1,m-1):
            
            if arr[i][j] > 0 and m*i+j not in visited:
                count+=1
                stack.append([i,j])
                visited.add(m*i+j)
               
            
                while(len(stack)):
                    
                    this_turn = stack.pop()
                    this_row = this_turn[0]
                    this_col = this_turn[1]
                    del_count = 0
                    for k in range(4):
                        row = this_row + dx[k]
                        col = this_col + dy[k]
                        if 0<=row and row<=n-1 and 0 <= col and col <= m-1 :
                            if arr[row][col] > 0:
                                if m*row+col not in visited:
                                    stack.append([row,col])
                                    visited.add(m*row+col)
                            else:
                                del_count += 1
                    
                    if del_count >0:
                        del_stack.append([this_row,this_col,del_count])
    
    if count >= 2:
        
        print(count_1-1)
        break
    if count == 0:
        print(0)
        break
    while(len(del_stack)):
        this_turn = del_stack.pop()
        row = this_turn[0]
        col = this_turn[1]
        sea = this_turn[2]

        if arr[row][col] - sea < 0:
            arr[row][col] = 0
        else:
            arr[row][col] = arr[row][col]-sea 
   