import sys
import collections


n = int(sys.stdin.readline())
dx = [-2,-1,1,2,2,1,-1,-2]
dy = [1,2,2,1,-1,-2,-2,-1]
result = []
for i in range(n):
    width = int(sys.stdin.readline())
    current_place = list(map(int,sys.stdin.readline().split()))
    aim_place = list(map(int,sys.stdin.readline().split()))
    visited = [[1]*width for _ in range(width)]
    stack = collections.deque([[current_place,0]])
    visited[current_place[0]][current_place[1]] = 0
    min_val = width*width
    while(len(stack)):
        this_turn = stack.popleft()
        
        this_turn_row = this_turn[0][0]
        this_turn_col = this_turn[0][1]
        if this_turn_row == aim_place[0] and this_turn_col == aim_place[1]:
            min_val = min(this_turn[1], min_val)
        for i in range(8):
            row = this_turn_row + dx[i]
            col = this_turn_col + dy[i]
            if 0<= row < width and 0 <= col < width and visited[row][col] :
                stack.append([[row,col],this_turn[1]+1])
                visited[row][col] = 0
    result.append(min_val)
for i in result:
    print(i)