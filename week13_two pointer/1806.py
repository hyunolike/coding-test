import sys

n, s = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))

left = 0
right = 0
value = 0
min_len=100001

while left< n and right < n:
    value += arr[right]
    if value<s:
        right+=1

    else:
        min_len = min(right-left,min_len)
        value-=arr[right]
        value-=arr[left]
        left+=1





if min_len == 100001:
    print(0)
else:
    print(min_len+1)