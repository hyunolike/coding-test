import sys
import collections
n, l = map(int,sys.stdin.readline().split())

water = collections.deque([])
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
arr.sort()
count = 0
left_count = 0
left_num = 0
for i in arr:
    i[0] = max(i[0],left_num+left_count+1)
    if i[0]>=i[1]:
        continue
    if (i[1] - i[0]) % l:
        count += ((i[1]-i[0])//l)+ 1
        left_num = i[1] - 1
        left_count = l - (i[1]-i[0])%l
    else:
        count += ((i[1]-i[0])//l)
        left_num = 0
        left_count = 0
   
    
print(count)