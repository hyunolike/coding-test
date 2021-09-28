import sys

def last(aim, start, finish,want):

    for i in range(start,finish):
        if first[aim] == middle[i]:
            last(aim+1,start,i,want)
            last(aim+i+1-start,i+1,finish,want)
            want.append(first[aim])
    

t = int(sys.stdin.readline())
result=[]
for i in range(t):
    result.append([])
    n = int(sys.stdin.readline())
    first = list(map(int,sys.stdin.readline().split())) 
    middle = list(map(int,sys.stdin.readline().split()))
    last(0,0,n,result[i])
for i in range(t):
    for j in result[i]:
        print(j,'',end='')
    print('')