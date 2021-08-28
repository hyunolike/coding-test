import sys
import copy
sys.setrecursionlimit(1000000)
calc=['+','-',' ']
T=int(input())

def sol(array,N):
    if len(array)==N-1:
        Nlist.append(copy.deepcopy(array))
        return
    for i in calc:
        array.append(i)
        sol(array,N)
        array.pop()


count=0
for _ in range(T):
    N=int(input())
    Nlist=[]
    sol([],N)
    numbers=[ num for num in range(1,N+1) ]
    ans=[]
    for ii in range(len(Nlist)):
        STR=""
        for jj in range(N):
            STR+=str(jj+1)
            try:
                STR+=Nlist[ii][jj]
            except:
                pass
        STR1=STR.replace(' ','')
        if eval(STR1)==0:
            ans.append(STR)
    ans.sort()
    for a in ans:
        print(a)


    if count==T-1:
        continue
    else:
        print()
        count+=1





