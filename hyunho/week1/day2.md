## 10773 제로

```python
num = int(input())
stack = []

for _ in range(num):

    n = int(input())

    if n == 0:
        stack.pop()
    else:
        stack.append(n)

print(sum(stack))

```

## 1874 스택수열

```python
import sys
T = int(input())
count = 1
stack = []
result = []

for i in range(1, T + 1):
    data = int(input())
    while count <= data:
        stack.append(count)
        count += 1
        result.append('+')
    if stack[-1] == data:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        sys.exit(0)

print('\n'.join(result))

```

