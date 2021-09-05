import sys

def opposite(index):
    if index == 0:
        return 5
    

def dice_right(rotate):
    rotate[0],rotate[1],rotate[2],rotate[3],rotate[4],rotate[5] = rotate[3], rotate[1], rotate[0], rotate[5], rotate[4], rotate[2]
def dice_down(rotate):
    rotate[0],rotate[1],rotate[2],rotate[3],rotate[4],rotate[5] = rotate[1],rotate[5], rotate[2],rotate[3],rotate[0], rotate[4]
def dice_up(rotate):
    rotate[0],rotate[1],rotate[2],rotate[3],rotate[4],rotate[5] = rotate[4], rotate[0], rotate[2], rotate[3], rotate[5], rotate[1]
def dice_left(rotate):
    rotate[0],rotate[1],rotate[2],rotate[3],rotate[4],rotate[5] = rotate[2], rotate[1], rotate[5], rotate[0], rotate[4], rotate[3] 

n, m, x, y, k = map(int,sys.stdin.readline().split())

arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

command = list(map(int,sys.stdin.readline().split()))

direction = [[0,1],[0,-1],[-1,0],[1,0]]

dice = [0,0,0,0,0,0]

this_turn_above = 0
result = []
for i in command:
    if i == 1: #동쪽
        row = x + direction[i-1][0]
        col = y + direction[i-1][1]
        if 0 <= row < n and 0 <= col < m:
            x = row
            y = col
            dice_right(dice)
            if arr[row][col]:
                dice[5] = arr[row][col]
                arr[row][col] = 0
            else:
                arr[row][col] = dice[5]
            
            result.append(dice[0])


    elif i == 2: #서쪽
        row = x + direction[i-1][0]
        col = y + direction[i-1][1]
        if 0 <= row < n and 0 <= col < m:
            x = row
            y = col
            dice_left(dice)
            if arr[row][col]:
                dice[5] = arr[row][col]
                arr[row][col] = 0
            else:
                arr[row][col] = dice[5]
            result.append(dice[0])
    elif i == 3: #북쪽
        row = x + direction[i-1][0]
        col = y + direction[i-1][1]
        if 0 <= row < n and 0 <= col < m:
            x = row
            y = col
            dice_up(dice)
            if arr[row][col]:
                dice[5] = arr[row][col]
                arr[row][col] = 0
            else:
                arr[row][col] = dice[5]
            
            result.append(dice[0])
    else: #남쪽
        row = x + direction[i-1][0]
        col = y + direction[i-1][1]
        if 0 <= row < n and 0 <= col < m:
            x = row
            y = col
            dice_down(dice)
            if arr[row][col]:
                dice[5] = arr[row][col]
                arr[row][col] = 0
            else:
                arr[row][col] = dice[5]

            result.append(dice[0])
    
for i in result:
    print(i)

