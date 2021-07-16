N = int(input().strip())




ans = 0
for j in range(N):
    arr = list(input().strip())
    A = []
    for i in arr:
        if not A:
            A.append(i)
        elif A[-1] == i:
            A.pop()
        else:
            A.append(i)
    if not A:
        ans =ans+1

print(ans)
