import sys
def star (left_upper_row, left_upper_col,number):
    if number == 3:
        stars[left_upper_row] += ' '*2
        stars[left_upper_row] +='*'
        stars[left_upper_row] += ' '*2
        stars[left_upper_row+1] +=' *'*2
        stars[left_upper_row+1] += ' '
        stars[left_upper_row+2] +='*****'
    else:
        for i in range(number//2):
            stars[left_upper_row+i] += ' '*(number//2)
        star(left_upper_row,left_upper_col + number//2 ,number//2)
        for i in range(number//2):
            stars[left_upper_row+i] += ' '*(number//2)
        star(left_upper_row+number//2,left_upper_col,number//2)
        
        for i in range(number//2,number):
            stars[left_upper_row+i]+=' '
       
        star(left_upper_row + number//2, left_upper_col + number, number//2)
        
n = int(sys.stdin.readline())

stars = ['' for _ in range(n)]

star (0,0,n)

for i in stars:
    print(i)