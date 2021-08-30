from itertools import combinations

while True:
    nums = list(map(int, input().split()))
    if nums[0]==0:
        break    
    k = nums[0]
    nums = nums[1:]
    c = combinations(nums, 6)
    for answer in c:
        print(' '.join(map(str, answer)))
    print()