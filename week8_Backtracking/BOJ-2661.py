import sys
input =sys.stdin.readline

def dfs(a,arr):
    for j in range(1,a//2+1):
        if arr[a-(2+j):a-(2*j)+j] == arr[a-(2*j)+j:]:
            return
    if a == n:
        print(*arr,sep = " ")
        exit(0)
    for i in range(1,4):
        if arr and arr[-1] == i:
            continue
        dfs(a+1,arr+[i])

n = int(input().rstrip())
dfs(0,[])