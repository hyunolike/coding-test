from sys import stdin

while True:
    s = stdin.readline().rstrip()
    if s == '.':
        break

    flag = False
    stack = []

    for ele in s:
        if ele not in ['(', ')', '[', ']']:
            continue

        if ele in '([':
            stack.append(ele)

        elif ele == ')':
            if len(stack) == 0 or stack.pop() != '(':
                flag = True
                break

        else:
            if len(stack) == 0 or stack.pop() != '[':
                flag = True
                break

    print('no') if flag or len(stack) != 0 else print('yes')
