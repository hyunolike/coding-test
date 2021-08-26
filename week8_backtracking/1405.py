import sys

def dfs(where, count, pro,this_turn):
    global probability
    if count == n:
       
        probability += pro * percent[where]
        return
    row = this_turn[0]
    col = this_turn[1]
    if arr[row+1][col] :
        arr[row+1][col] = 0
        dfs('d', count+1, pro*percent[where],(row+1,col))
        arr[row+1][col] = 1
    if arr[row][col+1] :
        arr[row][col+1] = 0
        dfs('r', count+1, pro*percent[where],(row,col+1))
        arr[row][col+1] = 1
    if arr[row-1][col] :
        arr[row-1][col] = 0
        dfs('u', count+1, pro*percent[where],(row-1,col))
        arr[row-1][col] = 1
    if arr[row][col-1] :
        arr[row][col-1] = 0
        dfs('l', count+1, pro*percent[where],(row,col-1))
        arr[row][col-1] = 1
n, l, r, d, u = map(int,sys.stdin.readline().split())
percent = {'l':l/100,'r':r/100,'d':d/100,'u':u/100}

probability = 0
arr = [[1]* (2*n+1) for _ in range(2*n+1)]



arr[n][n] = 0
arr[n][n+1] = 0
dfs('r',1,1,(n,n+1))
arr[n][n+1] = 1
arr[n+1][n] = 0
dfs('d',1,1,(n+1,n))
arr[n+1][n] = 1
arr[n][n-1] = 0
dfs('l',1,1,(n,n-1))
arr[n][n-1] = 1
arr[n-1][n] = 0
dfs('u',1,1,(n-1,n))

print('%0.9f'%(probability))