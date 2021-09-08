
n=int(input())
switch=list(map(int,input().split()))
s=int(input())
students=[list(map(int, input().split())) for _ in range(s)]

def male(num):
    for i in range(1, len(switch)+1):
        if i % num == 0:
            switch[i-1] = (switch[i-1]+1)%2
    return 0

def female(num):
    num = num-1
    s,e = num-1, num+1
    switch[num]=(switch[num]+1)%2
    while True:
        if not (0<=s<n and 0<=e<n):
            return 0
        if switch[s]==switch[e]:
            switch[s]=(switch[s]+1)%2
            switch[e]=(switch[e]+1)%2
        else:
            return 0
        s,e = s-1, e+1

for sex, num in students:
    if sex==1:
        male(num)
    else:
        female(num)

for i in range(len(switch)):
    if i>0 and i%20==0:
        print()
    print(switch[i], end=' ')
