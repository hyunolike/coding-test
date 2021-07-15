N = int(input().strip())
arr = list(input().strip())
num = [0] * N
for i in range(N):
    num[i] = int(input())
ans = []



for i in arr:
    if i in "+-/*":
        if i == "+":
            n1 = ans.pop()
            n2 = ans.pop()
            ans.append(n1+n2)
        elif i == '*':
            n1 = ans.pop()
            n2 = ans.pop()
            ans.append(n1*n2)
        elif i == '-':
            n1 = ans.pop()
            n2 = ans.pop()
            ans.append(n2-n1)
        elif i == '/':
            n1 = ans.pop()
            n2 = ans.pop()
            ans.append(n2/n1)
    else:
        ans.append(num[ord(i)-ord('A')])

print('%.2f' %ans[0])
