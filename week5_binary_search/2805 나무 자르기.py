n, m = map(int, input().split())
trees = list(map(int, input().split()))

left, right = 1, max(trees)
answer = 0

while left <= right:
    mid = (left+right)//2
    cuts = sum(tree-mid for tree in trees if tree-mid>0)

    if cuts < m:
        right = mid-1
    else:
        left = mid+1
        answer = mid

print(answer)