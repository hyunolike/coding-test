import sys
def is_right(arr,row,col):
    square_row = (row//3)*3
    square_col = (col//3)*3
    cand = set(range(1,10))

    set_row = set(arr[row])

    set_square = set([arr[i][j] for i in range(square_row,square_row+3) for j in range(square_col,square_col+3)])

    set_col = set([arr[i][col] for i in range(9)])

    if len(set_row)==9 and len(set_square)==9 and len(set_col)==9:
        return True
    return False

def maze(arr,ptr,idx): #ptr속 요소들을 candi후보에서 뽑아서 비교
    if idx == len(ptr):
        flag = 0
        for i in ptr:
            this_row = i[0]
            this_col = i[1]
            if is_right(arr,this_row,this_col):
                flag = 1
            else:
                flag = 0
                break
        if flag :
            for i in range(9):
                for j in range(9):
                    print(arr[i][j],'',end='')
                print('')
            sys.exit()
        else:
            return
    
    this_row = ptr[idx][0]
    this_col = ptr[idx][1]

    candi = candidate(arr,this_row,this_col)
   
    for i in candi:
        row_col = ptr[idx]
        
        arr[row_col[0]][row_col[1]] = i
        maze(arr,ptr,idx+1)
        arr[row_col[0]][row_col[1]] = 0 
   
    return
       

def candidate(arr,row,col):
    square_row = (row//3)*3
    square_col = (col//3)*3
    cand = set(range(1,10))

    set_row = set(arr[row])

    set_square = set([arr[i][j] for i in range(square_row,square_row+3) for j in range(square_col,square_col+3)])

    set_col = set([arr[i][col] for i in range(9)])

    return ((cand-set_row) & (cand - set_square)) & (cand-set_col)

arr = [list(map(int,sys.stdin.readline().split())) for i in range(9)]

ptr = [(i,j) for i in range(9) for j in range(9) if arr[i][j]==0]

candi = []


maze(arr,ptr,0)
        
            