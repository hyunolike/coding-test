import sys

arr = sys.stdin.readline().split()

if len(arr[0]) != len(arr[1]):
    print(0)
    
else:
    count = 0
    for i in range(len(arr[0])):
        if arr[0][i] == arr[1][i]:
            if arr[0][i] == str(8):
                count +=1
            else:
                continue
        else:
            break
    print(count)