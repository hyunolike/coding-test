def DFS(L, total):
    if L==n and total==f:
        for i in range(n):
            print(num[i], end=' ')
        print()
        exit(0)
    else:
        for i in range(1, n+1):
            if not ch[i]:
                ch[i]=1
                num[L]=i
                DFS(L+1, total+b[L]*num[L])
                ch[i]=0

n,f=map(int, input().split())
ch=[0]*(n+1)
num=[0]*n
b=[1]*n
for i in range(1, n):
    b[i]=b[i-1]*(n-i)//i
DFS(0,0)