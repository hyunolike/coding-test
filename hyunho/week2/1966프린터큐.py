from collections import deque

for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = deque(map(int, input().split()))
    index = [0 for _ in range(n)]
    index[m] = 1
    count = 0

    while 1:
        if arr[0] == max(arr):
            if index[0] == 1:
                break
            else:
                arr.popleft() 
                index.pop(0) 
                count += 1
        else:
            arr.append(arr.popleft())
            index.append(index.pop(0))
    print(count + 1)