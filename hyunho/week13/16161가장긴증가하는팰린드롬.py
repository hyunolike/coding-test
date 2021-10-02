n = int(input())
a = list(map(int, input().split()))
ans = 1
for i in range(n-1):
    if a[i] == a[i+1]: #문자열의 길이가 짝수
        temp = 2
        l = i-1
        r = i+2
        while 0 <= l and r < n:
            if a[l] == a[r] and a[l] < a[l+1]:
                temp += 2
                l -= 1
                r += 1
            else:
                break
        ans = max(temp, ans)
 
    if i > 0 and a[i-1] == a[i+1] and a[i-1] < a[i]: #문자열의 길이가 홀수
        temp = 3
        l = i-2
        r = i+2
        while 0 <= l and r < n:
            if a[l] == a[r] and a[l] < a[l+1]:
                temp += 2
                l -= 1
                r += 1
            else:
                break
        ans = max(temp, ans)
print(ans)
