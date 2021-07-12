from sys import stdin

stack = []
s = stdin.readline().rstrip()

for ele in s:
    if ele == ')':
        tmp = 0
        while stack: #스택에 원소가 있다면 반복
            top = stack.pop()
            if top == '(':
                if tmp == 0: #()
                    stack.append(2)
                else: #(x)
                    stack.append(2*tmp)
                break
            elif str(top).isdigit():
                tmp += top
            else:
                print(0)
                exit(0)

    elif ele == ']':
        tmp = 0
        while stack:
            top = stack.pop()
            if top == '[':
                if tmp == 0:
                    stack.append(3)
                else:
                    stack.append(3 * tmp)
                break
            elif str(top).isdigit():
                tmp += top
            else:
                print(0)
                exit(0)
    else: #열린괄호
        stack.append(ele)

p = True if '(' in stack or '[' in stack else False
if p:
    print(0)
else:
    print(sum(stack))
