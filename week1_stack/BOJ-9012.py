
def solution():
    list1 =list(input())
    count = 0

    for i in list1:
        if i  == "(":
            count += 1
        elif i == ")":
            count -= 1
        if count < 0 :
            print("NO")
            break
    if count == 0:
        print("YES")
    elif count > 0:
        print("NO")

a = int(input())
for j in range(a):
    solution()
