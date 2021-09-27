import sys

def find_path(row,col,N):
    global blue_square,white_square

    this_turn = arr[row][col]
    if N == 1:
        
        if this_turn:
            blue_square += 1
        else:
            white_square+=1
        return
    flag = 0
    for i in range(row,row+N):
        for j in range(col,col+N):
            if arr[i][j] !=  this_turn:
                flag = 1
                break
    if flag:
        find_path(row,col,N//2)
        find_path(row+N//2,col,N//2)
        find_path(row,col+N//2, N//2)
        find_path(row+N//2,col+N//2,N//2)
    else:
        if this_turn:
            
            blue_square += 1
        else:
           
            white_square += 1

n = int(sys.stdin.readline())

arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

white_square = 0
blue_square = 0

find_path(0,0,n)
print(white_square)
print(blue_square)