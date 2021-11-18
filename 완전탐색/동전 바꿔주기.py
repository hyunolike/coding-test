def DFS(L,sum):
    global answer
    if L==k:
        if money==sum:
            answer+=1
        return 0
    else:
        for i in range(cnt[L]+1):
            DFS(L+1, sum+coin[L]*i)

money=int(input())
k=int(input())
coin,cnt=[],[]
answer=0
for _ in range(k):
    a,b=map(int,input().split())
    coin.append(a)
    cnt.append(b)
DFS(0,0)
print(answer)