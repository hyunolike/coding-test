import sys
input=sys.stdin.readline
sys.setrecursionlimit(10000000)

N=int(input())
temp=list(map(int,(input().split())))
D=int(input().rstrip())


def sol(d):
    temp[d]=-2
    for i in range(len(temp)):
        if d==temp[i]:
            print(i,temp[i],d)
            sol(i)
sol(D)

stack=[]
count = 0
for i in range(len(temp)):
    if temp[i] != -2 and i not in temp:
        count += 1
print(count)