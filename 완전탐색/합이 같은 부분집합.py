def DFS(L, sum):
    global total
    if sum>total//2:
        return 0
    if L==n:
        if sum==(total-sum):
            print("YES")
            exit(0)
    else: # L번째 원소를 더하거나, 안더하거나
        DFS(L+1, sum+num[L])
        DFS(L+1, sum)

n=int(input())
num=list(map(int, input().split()))
total=sum(num)
DFS(0, 0)
print("NO")