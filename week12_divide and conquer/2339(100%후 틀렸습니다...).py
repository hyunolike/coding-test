import sys

def divide (start_row, start_col, finish_row, finish_col, horizonal):
    divide_complete ,jewel, trash =0,0,0
    for i in range(start_row,finish_row):
        for j in range(start_col, finish_col):
            if arr[i][j] == 1:
                trash += 1
                if horizonal:
                    for t in range(start_col,finish_col):
                        if arr[i][t]==2:
                            break
                    else:
                        divide_complete += divide(start_row,start_col, i,finish_col, not(horizonal)) * divide(i+1,start_col,finish_row,finish_col,not(horizonal))
                else:
                    for t in range(start_row,finish_row):
                        if arr[t][j] == 2:
                            break
                    else:
                        divide_complete += divide(start_row,start_col, finish_row,j,not(horizonal)) * divide(start_row,j+1,finish_row,finish_col, not(horizonal))
            elif arr[i][j] == 2:
                jewel+=1
    if trash == 0:
        if jewel == 1:
            return 1
        else:
            return 0
    return divide_complete
n = int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

trash = 0
jewel = 0


for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            trash += 1

        elif arr[i][j] == 2:
            jewel += 1

if trash == 0: 
    if jewel == 1:
        print(0)
    else:
        print(-1)
    sys.exit()
cnt = divide(0,0,n,n,0) + divide(0,0,n,n,1)
if cnt :
    print(cnt)
else:
    print(-1)