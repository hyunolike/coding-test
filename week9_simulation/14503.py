import sys

n, m = map(int,sys.stdin.readline().split())

loc_x , loc_y, direct = map(int,sys.stdin.readline().split())

arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

direction = [[-1,0],[0,1],[1,0],[0,-1]]

count = 0

flag = 1
while True:
    #현재 위치를 청소한다
    if flag:
        count += 1
        arr[loc_x][loc_y] = 2
        
    flag = 0
    
    for i in range(4):
        this_turn_direct = direction[(direct-1-i)%4]
        this_turn_x = loc_x + this_turn_direct[0]
        this_turn_y = loc_y + this_turn_direct[1]
        if 0<=this_turn_x<n and 0<=this_turn_y<m:
            if arr[this_turn_x][this_turn_y] == 0:
                loc_x = this_turn_x
                loc_y = this_turn_y
                direct = (direct-1-i)%4
                
                flag = 1
            if flag:
                break
    if flag:
        continue
    else:
      
        if 0<=loc_x + (-1)*direction[direct][0]<n and 0<=loc_y + (-1)*direction[direct][1]<m and arr[loc_x + (-1)*direction[direct][0]][loc_y + (-1)*direction[direct][1]] !=1:
            
            loc_x = loc_x+(-1)*direction[direct][0]
            loc_y = loc_y+(-1)*direction[direct][1]
        else:
            break
print(count)
            
        
