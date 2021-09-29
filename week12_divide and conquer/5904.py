import sys

def find(sym_m,zero_count,n):
    
    if sym_m>number:
        return number
    elif sym_m == number:
        print('m')
        sys.exit()
    this_turn=0
    for i in range(n):
        this_turn+=(3+i)*(2**(n-1-i))
    value = find(this_turn,zero_count+1,n+1)
    if sym_m+zero_count < value:
        return value-(sym_m+zero_count)
    elif value<sym_m:
        return value
    elif value==sym_m:
        print('m')
        sys.exit()
    else:
        if sym_m+zero_count == value:
            print('m')
            sys.exit()
        else:
            print('o')
            sys.exit()

number = int(sys.stdin.readline())-1

find(0,3,1)

