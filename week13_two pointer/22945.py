import sys

n = int(sys.stdin.readline())

arr = list(map(int,sys.stdin.readline().split()))

if n == 2:
    print(0)
    sys.exit()

left = 0
right = n-1
max_ability = 0

while left<right:
    max_ability = max(max_ability, min(arr[right],arr[left])*(right-left-1))
    if arr[left]<arr[right]:
        left += 1
    else:
        right -= 1
print(max_ability)