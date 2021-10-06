import sys
import math
n = int(sys.stdin.readline())

arr = []
for i in range(n+1):
    arr.append(math.inf)
    

arr[n] = 0
for i in reversed(range(n+1)):
    min_val = arr[i]
   
    if i % 3 == 0:
       arr[i//3] = min(min_val+1,arr[i//3])
    if i % 2 == 0:
        arr[i//2] = min(min_val+1, arr[i//2])
    arr[i-1] =min( min_val+1 , arr[i-1])

print(arr[1]) 