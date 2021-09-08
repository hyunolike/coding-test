#1713 후보추천


import sys
input =sys.stdin.readline

 
N= int(input().rstrip())
M= int(input().rstrip())
a=list(map(int, input().rstrip().split()))

b=[a[0]]
c=[1]

for i in a[1:]:

    if i in b:
        c[b.index(i)]+=1

    else:

        if len(b)==N:
            ind=c.index(min(c))
            del b[ind]
            del c[ind]
        b.append(i)
        c.append(1)

        
b.sort()
print(' '.join(map(str, b)))