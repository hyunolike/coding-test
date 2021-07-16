from sys import stdin

n, k = map(int, stdin.readline().split()) #k도 업데이트 됨
num = stdin.readline().rstrip()
stack = []
digit = n - k

for i in range(n):
    while k > 0 and stack and stack[-1] < num[i]: #반복을 통해서 stack에서 작은 수를 pop
        stack.pop()
        k -= 1

    stack.append(num[i])

print(int(''.join(stack[:digit]))) #k가 그대로일때 처리

