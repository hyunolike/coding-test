from itertools import combinations
import sys
input=sys.stdin.readline
T=list(map(int,input().split()))

while T[0]!=0:
    combo=combinations(T[1:],6)
    temp=[]
    for i in combo:
        for j in i:
            print(j,end=' ')
        print()
    T=list(map(int,input().split()))
    if T[0]!=0:
        print()