def DFS(L,A,B,C):
    global answer
    if L==n:
        if A!=B and B!=C and C!=A:
            diff=max(A,B,C)-min(A,B,C)
            answer=min(answer, diff)
        return 0
    else:
        DFS(L+1,A+coin[L],B,C)
        DFS(L+1,A,B+coin[L],C)
        DFS(L+1,A,B,C+coin[L])

n=int(input())
coin=[]
for _ in range(n):
    x=int(input())
    coin.append(x)
answer=2e9
DFS(0,0,0,0)
print(answer)