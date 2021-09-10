n, k = map(int, input().split())
childs = list(map(int,input().split()))
diff = []
for i in range(1, n):
    diff.append(childs[i]-childs[i-1])

diff.sort()
result=0
for i in range(n-k):
    result+=diff[i]
print(result)