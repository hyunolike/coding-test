arr = list(input())
Alist = []
Blist = []
ans = 0
mul = 1
pair = True

for i in range(len(arr)):
    if arr[i] == '(':
        Alist.append(arr[i])
        mul *= 2
    elif arr[i] == '[':
        Blist.append(arr[i])
        mul *= 3
    elif arr[i] == ')':
        if Alist:
            if arr[i-1] == '(':
                 ans += mul
            Alist.pop()
            mul = mul //2
        else:
            pair=False
            break
    elif arr[i] == ']':
        if Blist:
            if arr[i-1] == '[':
                ans += mul
            Blist.pop()
            mul = mul//3
        else:
            pair=False
            break


if not Alist and not Blist and pair:
    print(ans)
else:
    print(0)
