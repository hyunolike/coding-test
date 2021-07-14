n = int(input())

def check(list):
    stack = []

    for i in list:
        if i == "(":
            stack.append(i)
        else:
            if not stack:
                print("NO")
                return
            else:
                stack.pop()
    if not stack:
        print("YES")
        return
    else:
        print("NO")
        return

for _ in range(n):
    list = input()
    check(list)