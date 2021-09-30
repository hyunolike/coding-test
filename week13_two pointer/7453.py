import sys


n = int(sys.stdin.readline())

arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

left_value = dict()
cnt = 0
for i in range(n):
    for j in range(n):
        if arr[i][0]+arr[j][1] in left_value:
            left_value[arr[i][0]+arr[j][1]]+=1
        else:
            left_value[arr[i][0]+arr[j][1]] = 1
for i in range(n):
    for j in range(n):
        if -1*(arr[i][2]+arr[j][3]) in left_value:
            cnt+=left_value[-1*(arr[i][2]+arr[j][3])]

print(cnt)