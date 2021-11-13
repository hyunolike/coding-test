def DFS(L,sum,tsum):
    global answer
    if sum>c:
        return 0
    if sum+(total-tsum)<answer:
        return 0
    if answer<sum:
        answer=sum
    if L==n:
        return 0
    DFS(L+1, sum+dog[L], tsum+dog[L])
    DFS(L+1, sum, tsum+dog[L])
    
c,n=map(int, input().split())
dog=list(int(input()) for _ in range(n))
answer=0
total=sum(dog)
DFS(0,0,0)
print(answer)