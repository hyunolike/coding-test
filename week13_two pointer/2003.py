import sys

n, m = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))

cnt = 0
left = 0
right = 0
value = 0
while left<n and right<n:
    value += arr[right]
    if value == m:
        
        cnt +=1
        value-=arr[left]
        left+=1
        
        value-=arr[right]

    elif value < m:
        right+=1
        
    else:
        value -= arr[left]
        left += 1
        value-=arr[right]
print(cnt)