s = input()
t = input()
s, t = list(s), list(t)

for i in range(len(t)-1, -1, -1):
    if t==s:
        print(1)
        exit(0)
    elif t[i]=='A':
        t.pop()
    else:
        t.pop()
        t = t[::-1]
print(0)