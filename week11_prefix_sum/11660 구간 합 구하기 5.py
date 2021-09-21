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


################################
# 풀이2
import sys
input = sys.stdin.readline

n,m = map(int,input().split())

nums = [[0]*(n+1)]

for _ in range(n):
    numbers = [0]+list(map(int, input().split()))
    nums.append(numbers)

# 1. 행 별로 더하기
for i in range(1, n+1):
    for j in range(2, n+1):
        nums[i][j] += nums[i][j-1]

# 2. 열 별로 더하기
for i in range(1, n+1):
    for j in range(2, n+1):
        nums[j][i] += nums[j-1][i]

for _ in range(m):
    a,b,c,d = map(int, input().split())
    # (x1,y1)에서 (x2,y2)까지의 합
    # nums[x2][y2]-nums[x1-1][y2]-nums[x2][y1-1]+nums[x1-1][y1-1]
    answer = nums[c][d]-nums[a-1][d]-nums[c][b-1]+nums[a-1][b-1]
    print(answer)