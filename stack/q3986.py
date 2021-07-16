from sys import stdin

n = int(stdin.readline())
count = 0

for _ in range(n):
    s = stdin.readline().rstrip()
    stack = []

    for i in range(len(s)):
        if stack:
            if s[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
        else:
            stack.append(s[i])

    if not stack:
        count += 1

print(count)
