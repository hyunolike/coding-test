def solution(ps):
    stack = []
    for s in ps:
        if s == '(':
            stack.append(s)
        elif s == ')' and stack:
            stack.pop()
        else:
            print("NO")
            return None
    if stack:
        print("NO")
    else:
        print("YES")

t = int(input())
data = [input() for i in range(t)]
for ps in data:
    solution(ps)
    