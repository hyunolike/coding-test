def DFS(L, P):
    global cnt
    if L==n:
        cnt+=1
        for i in range(P):
            print(chr(res[i]+64), end='')
        print()
    else:
        for i in range(1, 27):
            if code[L]==i:
                res[P]=i
                DFS(L+1, P+1)
            elif i>=10 and i//10==code[L] and i%10==code[L+1]:
                res[P]=i
                DFS(L+2, P+1)
    

code=list(map(int, input()))
n=len(code)
code.insert(n,-1)
res=[0]*n
cnt=0
DFS(0,0)
print(cnt)