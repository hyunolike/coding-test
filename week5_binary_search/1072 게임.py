x, y = map(int, input().split())
left, right = 0, x
answer = 0
z = y*100//x

while left<=right:
    mid = (left+right)//2
    game = x + mid
    win = y + mid
    target = win*100//game

    if z == target:
        left = mid + 1
    else:
        answer = mid
        right = mid - 1

x, y = x+answer, y+answer
result = y*100//x
if result == z:
    print(-1)
else: 
    print(answer)