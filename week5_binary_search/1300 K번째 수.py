n = int(input())
k = int(input())
cnt, answer = 0, 0
left, right = 1, k

while left <= right:
    mid = (left + right)//2
    cnt = 0
    for i in range(1, n+1):
        cnt += min(mid // i, n)
    if cnt >= k:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1
print(answer)
