import sys

m, n, l = map(int, input().split())
gun = list(map(int, sys.stdin.readline().split()))
animal = list(map(int, sys.stdin.readline().split()) for _ in range(n))
gun.sort()
cnt = 0

for x, y in animal:
    if (y>l):
        continue
    s = x+y-l
    e = x-y+l
    left, right = 0, m-1
    while left <= right:
        mid = (left+right)//2
        if gun[mid] >= s and gun[mid] <= e:
            cnt += 1
            break
        elif gun[mid] < e:
            left = mid + 1
        else:
            right = mid - 1
print(cnt)