import sys

def dfs(x,visited):
    global count
    if x == n-1:
        count+=1
    this_row = x+1
    possible = [1]*n
    for row,col in visited:
        if col + abs(this_row - row) < n:
            possible[col + abs(this_row - row)] = 0
        if col - abs(this_row - row) > -1:
            possible[(col - abs(this_row - row))] = 0
        possible[col] = 0    
        
    for i in range(n):
        if possible[i] == 1:
            dfs(this_row, visited.union({(this_row,i)}))
n = int(sys.stdin.readline())

arr = []
count = 0
for i in range(n):
    arr.append([])
    for _ in range(n):
        arr[i].append(0)



for i in range(n):
    dfs(0,{(0,i)})
        
print(count)