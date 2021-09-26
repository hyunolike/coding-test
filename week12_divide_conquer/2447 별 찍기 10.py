import sys
sys.setrecursionlimit(10**6)

def print_star(length):
    if length == 1:
        return ['*']
    
    stars = print_star(length//3)
    tmp = []

    for s in stars:
        tmp.append(s*3)
    for s in stars:
        tmp.append(s+' '*(length//3)+s)
    for s in stars:
        tmp.append(s*3)
    
    return tmp

n = int(input())
for s in print_star(n):
    print(s)