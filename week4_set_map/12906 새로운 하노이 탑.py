from collections import deque

visited = set()
q = deque()

a = input().split()
s1 = a[-1] if len(a)>1 else ''
a = input().split()
s2 = a[-1] if len(a)>1 else ''
a = input().split()
s3 = a[-1] if len(a)>1 else ''

q.append((s1, s2, s3, 0))

while q:
    a, b, c, count = q.popleft()
    cont_str = a + '/' + b + '/' + c

    if a=='A'*len(a) and b=='B'*len(b) and c=='C'*len(c):
        print(count)
        break

    if cont_str not in visited:
        visited.add(cont_str)

        if len(a)>0:
            q.append((a[:-1], b+a[-1], c, count+1))
            q.append((a[:-1], b, c+a[-1], count+1))
        if len(b)>0:
            q.append((a, b[:-1], c+b[-1], count+1))
            q.append((a+b[-1], b[:-1], c, count+1))
        if len(c)>0:
            q.append((a, b+c[-1], c[:-1], count+1))
            q.append((a+c[-1], b, c[:-1], count+1))
