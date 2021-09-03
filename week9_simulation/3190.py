import sys
import collections
n = int(sys.stdin.readline())

k = int(sys.stdin.readline())

arr = [list(map(int,sys.stdin.readline().split())) for _ in range(k)]

l = int(sys.stdin.readline())

snake = [list(sys.stdin.readline().split()) for _ in range(l)]

direction = [[-1,0], [0,1], [1,0], [0,-1]]

snake_direct = 1

position = [[0]*n for _ in range(n)]

for i in arr:
    position[i[0]-1][i[1]-1] = 1
position[0][0] = -1
current_position = [0,0]
count = 1
l_index = 0
stack = collections.deque([(0,0)])
while True:
    this_turn_row = current_position[0] + direction[snake_direct][0]
    this_turn_col = current_position[1] + direction[snake_direct][1]
    
    if not (0 <= this_turn_row < n and 0 <= this_turn_col < n) :
        break

    if position[this_turn_row][this_turn_col] == 1:
        stack.append((this_turn_row,this_turn_col))
        current_position[0] = this_turn_row
        current_position[1] = this_turn_col
    elif position[this_turn_row][this_turn_col] == 0:
        stack.append((this_turn_row,this_turn_col))
        row, col= stack.popleft()
        position[row][col] = 0
        position[this_turn_row][this_turn_col] = -1
        current_position[0] = this_turn_row
        current_position[1] = this_turn_col

        
    elif position[this_turn_row][this_turn_col] == -1:
        break
    
    if l_index < l:
        
        if str(count) == snake[l_index][0]:
            
            if snake[l_index][1] == 'D':
                snake_direct = (snake_direct+1)%4
            else:
                snake_direct = (snake_direct-1)%4
         
            l_index+=1
    count+=1

print(count)