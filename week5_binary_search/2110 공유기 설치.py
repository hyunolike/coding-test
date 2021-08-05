import sys

n,c = map(int, input().split())
house = list(int(sys.stdin.readline()) for _ in range(n))
house.sort()

left = 1
right = house[-1]-house[0]
answer = 0

while left <= right:
    mid = (left+right)//2
    cnt = 1
    wifi = house[0]

    for i in range(1, n):
        if house[i] >= wifi + mid:
            cnt += 1
            wifi = house[i]
    
    if cnt < c:
        right = mid - 1
    else:
        left = mid + 1
        answer = mid
print(answer)