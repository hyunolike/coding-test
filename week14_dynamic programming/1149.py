import sys

n = int(sys.stdin.readline())

arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

ptr = []

for i in range(n):
    ptr.append([])
    for j in range(3):
        ptr[i].append(arr[0][j])
for i in range(1,n):
    for j in range(3):
        if j == 0:
            ptr[i][j] = min(ptr[i-1][1]+arr[i][0],ptr[i-1][2]+arr[i][0])
        elif j == 1:
            ptr[i][j] = min(ptr[i-1][0]+arr[i][1],ptr[i-1][2]+arr[i][1])
        else:
            ptr[i][j] = min(ptr[i-1][1]+arr[i][2],ptr[i-1][0]+arr[i][2])

print(min(ptr[n-1][0],ptr[n-1][1],ptr[n-1][2]))