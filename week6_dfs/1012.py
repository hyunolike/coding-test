import sys
import collections
#
t=int(sys.stdin.readline())
result = []
for _ in range(t):
    m, n, k=map(int,(sys.stdin.readline().split()))
    
    arr = [[0]*m for _ in range(n)]
   
    for _ in range(k):
        col , row = map(int,sys.stdin.readline().split())
        arr [row][col] =1

    count = 2
    stack = collections.deque([])
    count=0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                stack.append([i,j])
                arr[i][j] = 0
                while(len(stack)):
                
                    this_turn = stack.pop()
                    this_row = this_turn[0]
                    this_col = this_turn[1]
                    ptr = [[this_row-1,this_col],[this_row+1,this_col],[this_row,this_col-1],[this_row,this_col+1]]
                    for s in ptr:
                        row_1 = s[0]
                        col_1 = s[1]
                        if row_1 >= n or row_1 <=-1 or col_1 >= m or col_1 <= -1:
                            continue
                        else:
                            if arr[row_1][col_1] == 1:
                                arr[row_1][col_1] = 2
                                stack.append([row_1,col_1])
                    
                        
                count+=1
    result.append(count)
for i in result:
    print(i)
