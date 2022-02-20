from itertools import permutations

def calc(comboi,temp):
    global maxvalue,minvalue
    result=temp[0]

    for i in range(len(comboi)):
        if comboi[i]=='+':
            result+=temp[i+1]
        elif comboi[i]=='-':
            result-=temp[i+1]
        elif comboi[i]=='÷':
            if result>0:
                result = result // temp[i+1]
            else:
                result =-( abs(result) // temp[i+1] )
        elif comboi[i]=='×':
            result*=temp[i+1]
    if result>maxvalue:
        maxvalue=result
    if result<minvalue:
        minvalue=result

N=int(input())

sequence=list(map(int,input().split()))
tempOp=list(map(int,input().split()))


op=['+','-','×','÷']
operation=[]
for i in range(4):
    for j in range(tempOp[i]):
        operation.append(op[i])


combo=permutations(operation,N-1)


maxvalue=-1000000000
minvalue=1000000000

for i in combo:
    calc(i,sequence)

print(maxvalue)
print(minvalue)