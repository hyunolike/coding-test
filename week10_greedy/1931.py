import sys

n = int(sys.stdin.readline())

arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
arr = sorted(arr,key = lambda x : (x[1],x[0]))

count = 0
idx = 0
while(True):
    flag = 1
    end = arr[idx][1]
    count += 1
    for j in range(idx+1,len(arr)):
        if arr[j][0]>=end:
            idx = j
            flag = 0
            break
    if flag:
        print(count)
        break
    
    