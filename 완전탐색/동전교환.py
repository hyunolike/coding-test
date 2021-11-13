def DFS(cnt, total):
    global money, answer
    if total>money or cnt>answer:
        return 0
    if total==money and answer>cnt:
        answer=cnt
        return 0
    else:
        for i in range(len(coin)):
            DFS(cnt+1, total+coin[i])

n=int(input())
coin=list(map(int, input().split()))
coin.sort(reverse=True)
money=int(input())
answer=2e9
DFS(0,0)
print(answer)