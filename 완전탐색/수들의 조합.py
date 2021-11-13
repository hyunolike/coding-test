def DFS(L, s, sum):
    if L==k:
        total.append(sum)
        return 0
    else:
        for i in range(s, n):
            DFS(L+1, i+1, sum+num[i])

n,k=map(int, input().split())
num=list(map(int, input().split()))
div=int(input())
total=[]
DFS(0,0,0)
total=[t for t in total if t%div==0]
print(len(total))