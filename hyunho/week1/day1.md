9012 괄호 / 2504 괄호의 값


## 9012 괄호

```python
n = int(input())

def check(list):
    stack = []

    for i in list:
        if i == "(":
            stack.append(i)
        else:
            if not stack:
                print("NO")
                return
            else:
                stack.pop()
    if not stack:
        print("YES")
        return
    else:
        print("NO")
        return

for _ in range(n):
    list = input()
    check(list)
```

## 2504 괄호의 값

```python
import sys

str = sys.stdin.readline().rstrip() # (()())

stack = list()

for i in str:
    if i == ")":
        temp = 0 

        while stack: 
            top = stack.pop() 
            if top == "(":
                if temp == 0:
                    stack.append(2) 
                else:
                    stack.append(2 * temp)
                break
            elif top == "[":
                print("0")
                exit(0)
            else:
                if temp == 0:
                    temp = int(top)
                else:
                    temp = temp + int(top)

    elif i == "]":
        temp = 0

        while stack: 
            top = stack.pop() 
            if top == "[":
                if temp == 0:
                    stack.append(3) 
                else
                    stack.append(3 * temp)
                break
            elif top == "(":
                print("0")
                exit(0)
            else:
                if temp == 0:
                    temp = int(top)
                else:
                    temp = temp + int(top)

    else:
        stack.append(i) 

result = 0

for i in stack:
    if i == "(" or i == "[":
        print(0)
        exit(0)
    else:
        result += i

print(result)
```