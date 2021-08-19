import sys
import collections
result =[]
dx = [-1,0,1,0,1,-1,1,-1]
dy = [0,1,0,-1,1,-1,-1,1]
while(True):
    width , height = map(int,sys.stdin.readline().split())
    if width == 0 and height == 0:
        break
    arr = [list(map(int,sys.stdin.readline().split())) for _ in range(height)]
    count = 0

    for i in range(height):
        for j in range(width):
            if arr[i][j] == 1:
                count += 1
                stack = collections.deque([[i,j]])
                arr[i][j] = 0
                while(len(stack)):
                    this_turn = stack.pop()
                    this_row = this_turn[0]
                    this_col = this_turn[1]
                    for k in range(8):
                        row = this_row + dx[k]
                        col = this_col + dy[k]
                        if row>=height or row <= -1 or col >=width or col <= -1:
                            continue
                        if arr[row][col]:
                            stack.append([row,col])
                            arr[row][col] = 0
    result.append(count)

for i in result:
    print(i)