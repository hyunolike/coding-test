from itertools import combinations

mo=['a','e','i','o','u']
L,C= map(int,input().split())
password=list(input().split())
password.sort()

def moeum(list):
    count=0
    for i in range(5):
        if list.count(mo[i]):
            count+=list.count(mo[i])
    return count

combo=combinations(password,L)
for i in combo:
    if not moeum(i)>L-2 and moeum(i)!=0:
        for j in i:
            print(j,end='')
        print()