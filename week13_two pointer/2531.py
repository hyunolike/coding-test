import sys

n, d, k, c = map(int,sys.stdin.readline().split())

suci = [int(sys.stdin.readline()) for _ in range(n)]

left = 0

right = k-1

sort = {}
value_sort = 0
max_len = 0
for i in range(left,right+1):
    try:
        sort[suci[i]] += 1
    except:
        sort[suci[i]] = 1
        value_sort += 1
if c in sort.keys():
    max_len = max(max_len,value_sort)
else:
    max_len = max(max_len, value_sort + 1)
    value_sort += 1

while left < n-1:
    sort[suci[left]]-=1
    if not sort[suci[left]]:
        if suci[left] != c:
            value_sort -= 1
    left += 1
    
    right+=1
    if right == n:
        right = 0
    try:
        sort[suci[right]]+=1
        if sort[suci[right]] == 1:
            if suci[right] != c:
                value_sort += 1
    except:
        sort[suci[right]] = 1
        if suci[right] != c:
            value_sort += 1
     
  
    max_len = max(max_len, value_sort)
print(max_len)