import sys
input = sys.stdin.readline

n, k = map(int, input().split())

nums = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(1, n):
        nums[i][j] += nums[i][j-1]

for _ in range(k):
    xy = list(map(int, input().split()))
    sx, sy = xy[0]-1, xy[1]-1
    ex, ey = xy[2]-1, xy[3]-1

    total = 0

    for i in range(sx, ex+1):
        if sy == 0:
            total += nums[i][ey]
        else:
            total += (nums[i][ey]-nums[i][sy-1])
    print(total)