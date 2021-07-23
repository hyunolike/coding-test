while 1:
    tmp =True
    ans = []
    arr = list(input().rstrip())
    if arr[0] =='.':
        break
    for i in arr:
        if i == '(' or i =='[':
            ans.append(i)
        elif i ==')':
            if not ans:
                tmp = False
                break
            if ans[-1] == '(':
                ans.pop()
            else:
                tmp = False
                break
        elif i ==']':
            if not ans:
                tmp = False
                break
            if ans[-1] == '[':
                ans.pop()
            else:
                tmp = False
                break

    if not ans and tmp:
        print("yes")
    else:
        print("no")
