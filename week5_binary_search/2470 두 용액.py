n = int(input())
liq = list(map(int, input().split()))
liq.sort()
l, r = 0, n-1
flag = False
a, b, answer = 0, 0, 1000000001

if liq[l]<0 and liq[r]<0:
    print(liq[-2], liq[-1])
    exit()
elif liq[l]>0 and liq[r] >0:
    print(liq[0], liq[1])
    exit()
else:
    flag=True

while flag and l<r:    
    sum = liq[l]+liq[r]
    if abs(sum) < answer:
        answer = abs(sum)
        a = l
        b = r
    if sum < 0:
        l += 1
    else:
        r -= 1
    
print(liq[a], liq[b])