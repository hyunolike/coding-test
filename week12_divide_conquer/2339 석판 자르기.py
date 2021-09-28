n=int(input())
L=[list(map(int,input().split())) for i in range(n)]
def f(s,e,l,r,c):
    if e==s or l==r: return 1
    cnt2=0
    cnt1=0
    for i in range(s,e):
        for j in range(l,r):
            if L[i][j]==1:
                cnt1+=1
            if L[i][j]==2:
                cnt2+=1
    if cnt1==0:
        if cnt2==0: return 0
        if cnt2==1: return 1
    ret=0
    for i in range(s,e):
        for j in range(l,r):
            if L[i][j]==1:
                if c!=0:
                    for k in range(l,r):
                        if L[i][k]==2:
                            break
                    else:
                        ret+=f(s,i,l,r,0)*f(i+1,e,l,r,0)
                if c!=1:
                    for k in range(s,e):
                        if L[k][j]==2:
                            break
                    else:
                        ret+=f(s,e,l,j,1)*f(s,e,j+1,r,1)
    return ret

r=f(0,n,0,n,-1)
if r==0: print(-1)
else: print(r)