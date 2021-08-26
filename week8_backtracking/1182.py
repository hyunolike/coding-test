import sys

def dfs(val, index, include):
    global count
    if val == s and include:
        count+=1
    if index < n-1:
        dfs(val+arr[index+1], index+1,1)
        
        dfs(val,index+1,0)

n, s = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))

count = 0

prune = sum(arr)

for i in range(n): 
    dfs(arr[i], i, 1)
print(count)