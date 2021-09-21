import sys

n = int(sys.stdin.readline())

arr = list(map(int,sys.stdin.readline().split()))

even = []
even_val = 0
odd = []
odd_val = 0
for i in range(n):
    if i%2:
        odd.append(odd_val + arr[i])
        odd_val += arr[i]
    else:
        even.append(even_val + arr[i])
        even_val += arr[i]
even.insert(0,0)
odd.insert(0,0)
Max = 0

for i in range(1,n//2+1):
    
    Max = max(Max, even[i-1] + odd[n//2] - odd[i-1])
    Max = max(Max, even[i] + odd[n//2] - odd[i-1] - arr[n-1])


print(Max)