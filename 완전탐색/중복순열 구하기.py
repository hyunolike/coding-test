# another solution
def DFS(L):
    global cnt
    if L==m:
        for i in range(m):
            print(res[i], end=' ')
        print()
    else:
        for i in range(1, n+1):
            res[L]=i
            DFS(L+1)

if __name__=="__main__":
    n,m=map(int, input().split())
    res=[0]*n
    DFS(0)
    print(n**m)