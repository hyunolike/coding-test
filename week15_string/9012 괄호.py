t=int(input())
for _ in range(t):
    word=input()
    stack=[]
    flag=True
    for w in word:
        if w=='(':
            stack.append(w)
        else:
            if stack:
                stack.pop()
            else:
                print('NO')
                flag=False
                break
    if stack:
        print('NO')
        flag=False
    if flag:
        print('YES')