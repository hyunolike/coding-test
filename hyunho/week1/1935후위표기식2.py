n = int(input())
sen = input()
stack = [0] * n

for i in range(n):
    stack[i] = int(input())

for i in sen:
    if i.isupper():
        stack.append(stack[ord(i) - ord('A')])
    else:
        str2 = stack.pop()
        str1 = stack.pop()

        if i == '+':
            stack.append(str1 + str2)
        elif i == '-':
            stack.append(str1 - str2)
        elif i == '*':
            stack.append(str1 * str2)
        elif i == '/':
            stack.append(str1 / str2)


print('%.5f' %stack[0])
