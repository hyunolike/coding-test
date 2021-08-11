n = int(input())
bay = list(int(input()) for _ in range(n))
bay.sort()

answer = 0

for i in range(n):
    cur, rad = i, 1
    cnt = 1
    l = cur-1

    while True:
        if l < 0 or bay[cur]-bay[l]>rad:
            break
        while l >=0 and bay[cur]-bay[l]<=rad:
            cnt += 1
            l -=1
        cur = l+1
        rad += 1
    
    cur, rad = i,1
    r = cur+1

    while True:
        if r >= n or bay[r]-bay[cur]>rad:
            break
        while r<n and bay[r]-bay[cur] <= rad:
            cnt += 1
            r += 1
        cur = r-1
        rad += 1
    
    answer = max(answer, cnt)
print(answer)
    