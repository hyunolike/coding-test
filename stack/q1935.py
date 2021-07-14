from sys import stdin

n = int(stdin.readline())
exp = stdin.readline().rstrip()
values = []
stack = []

for _ in range(n):
    values.append(int(stdin.readline()))

for ele in exp:
    if 'A' <= ele <= 'Z':
        stack.append(values[ord(ele)-65])
    else:
        a = str(stack.pop())
        b = str(stack.pop())
        stack.append(eval(b+ele+a))

print("%0.2f"%round(stack[0], 2))
