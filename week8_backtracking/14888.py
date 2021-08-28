import sys

def sol(arr,equ,cur,N,Min,Max):
    if N == 0:
        val = arr[0]
        for i in range(len(cur)):
            if cur[i]=='+':
                val += arr[i+1]
            elif cur[i]=='-':
                val -= arr[i+1]
            elif cur[i]=='*':
                val *= arr[i+1]
            else:
                if val<0:
                    val= val*(-1)
                    val = (-1)*(val//arr[i+1])
                else:
                    val = val//arr[i+1]
                
        if val < Min:
            Min = val
        if val > Max:
            Max = val
        return Min, Max
    set1 = set(equ)
    for i in set1:
        this = equ.index(i)
        cur.append(i)
        equ.pop(this)
        Min,Max = sol(arr,equ,cur,N-1,Min,Max)
        cur.pop(-1)
        equ.insert(this,i)
    return Min, Max
N = int(sys.stdin.readline())

arr = list(map(int,sys.stdin.readline().split()))

count = list(map(int,sys.stdin.readline().split()))

string = ['+','-','*','/']
equ = []
idx = 0

while(idx<4):
    if count[idx]>0:
        equ.append(string[idx])
        count[idx]-=1
    else:
        idx+=1


Min, Max = sol(arr,equ,[],N-1,1000000000,-1000000000)

print(Max)
print(Min)