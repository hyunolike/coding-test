N = int(input().strip())
arr = []
sum = 0

for i in range(N):
    a = int(input().strip())
    if a == 0:
        arr.pop()
    else:
        arr.append(a)

for i in range(len(arr)):
    sum += arr[i]

print(sum)
