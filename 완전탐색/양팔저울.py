def DFS(L,weight):
    if weight>0:
        ch[weight]=1
    if L==n:
        return 0
    else:
        DFS(L+1,weight+w[L])
        DFS(L+1,weight-w[L])
        DFS(L+1,weight)

n=int(input())
w=list(map(int, input().split()))
s=sum(w)
ch=[0]*(s+1)
DFS(0,0)
print(len(ch)-sum(ch)-1)