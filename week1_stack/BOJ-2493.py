
N = int(input())
top = list(map(int, input().split()))
arr = []
ans = []

for i in range(N):
    while arr:
        if arr[-1][1] > top[i]: 
            ans.append(arr[-1][0] + 1) 
            break
        arr.pop() 

    if not arr:
        ans.append(0) 

    arr.append([i, top[i]])


for i in range(N):
    print(ans[i], end=' ')
