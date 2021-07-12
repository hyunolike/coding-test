#정수가 "0"일 경우에 지울 수 있는 수가 있음을 보장할 수 있다.

from sys import stdin

k = int(stdin.readline())

stack = []
for _ in range(k):
    n = int(stdin.readline())
    if n == 0: #0이면 pop
        stack.pop()
    else:#아니면 push
        stack.append(n)

print(sum(stack))