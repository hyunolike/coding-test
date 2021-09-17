import sys
input = sys.stdin.readline

def bs_search(height, cave):
    l, r = 0, len(cave)-1
    while l<=r:
        mid = (l+r)//2
        if cave[mid]<=height:
            l = mid+1
        else:
            r = mid-1
    
    return len(cave) - (r+1)

n, h = map(int, input().split())
top, bottom = [], []

for i in range(n):
    rock = int(input())
    if i%2 == 0:
        top.append(rock)
    else:
        bottom.append(rock)

top.sort()
bottom.sort()

rock_cnt, range_cnt = 1e10, 0

for i in range(1, h+1):
    top_cnt = bs_search(i-1, top)
    bottom_cnt = bs_search(h-i, bottom)
    cnt = top_cnt + bottom_cnt

    if cnt < rock_cnt:
        rock_cnt = cnt
        range_cnt = 1
    elif cnt == rock_cnt:
        range_cnt += 1
    else:
        pass

print(rock_cnt, range_cnt)