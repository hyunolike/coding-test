def DFS(L, s):
    global answer
    if L==m:
        for i in range(m):
            print(res[i], end=' ')
        print()
        answer+=1
        return 0
    else:
        for i in range(s, n+1):
            res[L]=i
            DFS(L+1,i+1)

n,m=map(int, input().split())
answer=0
res=[0]*m
DFS(0,1)
print(answer)