n, m = map(int, input().split())
lesson = list(map(int, input().split()))
left, right = max(lesson), sum(lesson)
answer = left

while left <= right:
    cnt = 0
    file = 0
    mid = (left + right)//2

    for l in lesson:  
        if file+l > mid:
            cnt += 1
            file = l
        else:
            file += l
    if file:
        cnt+=1
    
    if cnt>m:
        left = mid+1
    else:
        answer = mid
        right = mid-1
print(answer)