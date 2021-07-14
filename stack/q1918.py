from sys import stdin

exp = stdin.readline().rstrip()

stack = []
result = []

for ele in exp:
    if ele == '(':
        stack.append(ele)

    elif ele in ['*', '/']:
        if len(stack) != 0:
            if stack[-1] in ['*', '/']:
                result.append(stack.pop())
        stack.append(ele)

    elif ele in ['+', '-']:
        while len(stack) != 0:
            if stack[-1] in ['*', '/', '+', '-']:
                result.append(stack.pop())
            else:
                break
        stack.append(ele)

    elif ele == ')':
        while True:
            p = stack.pop()
            if p == '(':
                break
            result.append(p)
    else:
        result.append(ele)

while stack:
    result.append(stack.pop())

print(''.join(result))
