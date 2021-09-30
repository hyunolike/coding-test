import sys
import collections
n, k = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))

left = 0
right = 0
odd_count = 0
q = collections.deque([])
max_cnt = 0


while left<n and right <n:
    if arr[right]%2 == 0:
        right+=1
    else:
        if odd_count<k:
            q.append(right)
            right+=1
            odd_count+=1
        else:
            q.append(right)
            max_cnt = max(max_cnt,right-left-k)
            left = q.popleft()+1
            right += 1
            odd_count = k
       

max_cnt = max(max_cnt,right-1 - left + 1 - odd_count)

print(max_cnt)
