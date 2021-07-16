import sys


input = lambda : sys.stdin.readline()
n, k = map(int, input().split())
count = k

arr = list(map(int, input().rstrip()))
result = []
for i in range(n):
    while count > 0 and result:
        if result[len(result) - 1] < arr[i]:

            result.pop()
            count -= 1
        else:
            break
    result.append(arr[i])

for i in range(n-k):
    print(result[i], end="")