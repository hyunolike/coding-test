import sys

def fractal(row,col,number):
    
    if number == 1:
       
        fractals[row+1][col+1] = ' '
        
    else:
        for i in range(row+number,row+number*2):
            for j in range(col+number,col+number*2):
                fractals[i][j] = ' '
        for i in range(3):
            for j in range(3):
                if i == j and j==1:
                    continue
                
                fractal(row+i*number,col+j*number,number//3)
        
n = int(sys.stdin.readline())
fractals = [['*']*n for _ in range(n)]

fractal(0,0,n//3)
for i in range(n):
    for j in range(n):
        print(fractals[i][j],end='')
    print('')