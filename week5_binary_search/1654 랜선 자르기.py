import sys

k, n = map(int, sys.stdin.readline().split())
lans = list(int(sys.stdin.readline()) for _ in range(k))
left, right, answer = 1, 21470000000, 0

while left <= right:
    mid = (left+right)//2
    cnt = 0

    for l in lans:
        cnt += l//mid
    
    if cnt < n: # 너무 크게 자름
        right = mid-1
    else: # 너무 작게 자름
        left = mid+1
        answer = mid
print(answer)