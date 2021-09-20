n = int(input())
ans=0
a = list(map(int,input().split()))

s=[]
s.append(a[0])
for i in range(1,n):
    s.append(s[i-1]+a[i])

print(s,'s')
print(a,'a')


#벌통이 가운데
for i in range(1,n-1):
    print(s[n-2]-a[0]+a[i],'aaaa',i)
    ans=max(ans,s[n-2]-a[0]+a[i])


#벌통이 오른쪽 끝
for i in range(1, n - 1):
    print((s[n-1]-s[1])*2,'bbb')
    print(s[n-1] - a[0] - a[i] + s[n-1] - s[i],'bbb2',i)
    ans = max(ans, s[n-1] - a[0] - a[i] + s[n-1] - s[i])

#벌통이 왼쪽
for i in range(1,n-1):
    print(s[n-2]+s[i-1]-a[i],'ccc1')
    print(2*s[i-1]+s[n-2]-s[i],'ccc2')
    ans=max(ans,2*s[i-1]+s[n-2]-s[i])

print(ans)


