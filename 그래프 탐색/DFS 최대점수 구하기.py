def DFS(L, sum, tsum, time):
    global answer
    if time>m or answer>sum+(total-tsum):
        return 0
    if answer<sum:
        answer=sum
    if L==n:
        return 0
    else:
        DFS(L+1, sum+p[L][0], tsum+p[L][0], time+p[L][1])
        DFS(L+1, sum, tsum+p[L][0], time)

n,m=map(int, input().split())
p=[list(map(int, input().split())) for _ in range(n)]
p.sort(key=lambda x: (x[0], -x[1]), reverse=True)
total=sum([score for score, _ in p])
answer=0
DFS(0,0,0,0)
print(answer)