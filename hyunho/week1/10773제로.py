num = int(input())
stack = []

for _ in range(num):

    n = int(input())

    if n == 0:
        stack.pop()
    else:
        stack.append(n)

print(sum(stack))
