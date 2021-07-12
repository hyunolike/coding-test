from sys import stdin

n = int(stdin.readline())
stack = []
result = []
flag = False
top = 0

for i in range(1, n+1):
    tmp = int(stdin.readline().rstrip())

    if top < tmp:
        for j in range(top+1, tmp+1):
            stack.append(j)
            result.append('+')

    top = stack[-1] if top < stack[-1] else top

    if stack.pop() != tmp:
        flag = True
    else:
        result.append('-')

if flag:
    print('NO')
else:
    for i in result:
        print(i)
