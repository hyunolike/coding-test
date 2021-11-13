def DFS(L):
    global answer
    if L==m:
        for i in range(m):
            print(res[i], end=' ')
        print()
        answer+=1
        return 0
    else:
        for i in range(1, n+1):
            if not check[i]:
                res[L]=i
                check[i]=1
                DFS(L+1)
                check[i]=0

n,m=map(int,input().split())
res=[0]*(n+1)
check=[0]*(n+1)
answer=0
DFS(0)
print(answer)