import sys

def square(arr, n):
    if n == 1:
        print(arr[0][0])
        sys.exit()
    this_turn_arr = []
  
    for i in range(n//2):
        this_turn_arr.append([])
        for j in range(n//2):
            first_max = -10000
            second_max = -10000
            for t in range(4):
                row = i*2 + square_row[t]
                col = j*2 + square_col[t]
                if arr[row][col] > first_max:
                    first_max, second_max = arr[row][col], first_max
                elif arr[row][col] > second_max:
                    second_max = arr[row][col]
            this_turn_arr[i].append(second_max)
    
    square(this_turn_arr,n//2)
            


n = int(sys.stdin.readline())

arr= [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

square_col = [0,1,1,0]
square_row = [0,0,1,1]

square(arr,n)

