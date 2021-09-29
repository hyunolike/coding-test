n = int(input())
s = 'moo'

def solve(n, k, length):
    next_len = length*2 + k+3
    if n <= 3:
        print(s[n-1])
        return 0
    if next_len < n:
        solve(n, k+1, next_len)
    else:
        if length < n <= length+k+3:
            if n == length+1:
                print('m')
            else:
                print('o')
            return 0
        else:
            solve(n-(length+k+3), 1, 3)

solve(n, 1, 3)