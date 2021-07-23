N = int(input().strip())

up= []
ans = []
count = 1
a= 0

for i in range(N):
    comp = int(input().strip())
    while comp >= count:
        up.append(count)
        ans.append("+")
        count = count +1
    if up[-1] == comp:
        up.pop()
        ans.append("-")
    else:
        a = 1
if a == 1:
    print("No")
else:
    for j in range(len(ans)):
        print(ans.pop(0))
