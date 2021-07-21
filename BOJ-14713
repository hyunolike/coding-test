#앵무새

from collections import deque

N = int(input().strip())
count = 0
count2 =0
arr = []

for i in range(N):
    arr.append(deque(map(str, input().split())))


arr2 = deque(list(map(str, input().split())))

tmp = True

while arr2:
    if count2 >= N*len(arr):
        tmp = False
        break

    for i in arr:
        
        if i and arr2[0] == i[0]:
            arr2.popleft()
            i.popleft()
            count = 0
        else:
            if count == N:
                tmp = False
                break
            else:
                count = count +1
    count2 = count2 +1


if not arr2 and tmp:
    print("Possible")
else:
    print("Impossible")
