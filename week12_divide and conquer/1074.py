import sys

def find(n,row,col,number):
    if n == 1:
        
        for i in range(4):
            if row + dx[i] == r and col + dy[i] == c:
                print(number + i)
                sys.exit()
    if r < row +  2**(n-1):
        if  c < col + 2**(n-1):
            
            find(n-1, row,col, number)
        else:
           
            find(n-1, row, col+2**(n-1), number+4**(n-1))
    else:
        if c < col + 2**(n-1):
            
            find(n-1,row + 2**(n-1),col, number+2 * 4**(n-1))
        else:
           
            find(n-1,row+2**(n-1), col + 2**(n-1), number + 3* 4**(n-1))
n, r, c = map(int,sys.stdin.readline().split())

dx = [0,0,1,1]
dy = [0,1,0,1]

find(n,0,0,0)