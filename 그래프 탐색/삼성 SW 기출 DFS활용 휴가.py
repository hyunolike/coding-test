def DFS(L, sum):
    global answer
    if L>n+1:
        return 0
    if answer<sum:
        answer=sum
    if L==n+1:
        return 0
    else:
        DFS(L+T[L],sum+P[L])
        DFS(L+1, sum)
    
n=int(input())
T,P=[],[]
for _ in range(n):
    t,p=map(int,input().split())
    T.append(t)
    P.append(p)
T.insert(0,0)
P.insert(0,0)
answer=0
DFS(1,0)
print(answer)