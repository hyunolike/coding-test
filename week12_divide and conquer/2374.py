import sys

def same(left_idx,right_idx):
    
    if left_idx == right_idx:
        return 0
    elif right_idx - left_idx == 1:
        return (0,arr[left_idx])
    Max = 0
    Max_idx = 0

    for i in range(left_idx,right_idx):
        if Max<arr[i]:
            Max = arr[i]
            Max_idx = i
    right = same(Max_idx+1,right_idx)
    
    left = same(left_idx, Max_idx)
    
    
    if type(left) == int:
        right_count, right_max =right
        return(Max - right_max + right_count, Max)

    elif type(right) == int:
        left_count, left_max =left
        return(Max - left_max + left_count, Max)
    else:
        left_count,left_max = left
        right_count, right_max = right
        return (Max - left_max+left_count + Max - right_max + right_count, Max)

n = int(sys.stdin.readline())

arr = [int(sys.stdin.readline()) for _ in range(n)]

print(same(0,n)[0])