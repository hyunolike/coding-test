import sys


def per(idx,length,string):
    global result
    count = 0
    for i in range(4): 
        row = idx[0] + dx[i]
        col = idx[1] + dy[i]
            
        if 0<=row<=n-1 and 0<=col<=m-1 and not oi[ord(arr[row][col])-65] and (row,col,string + arr[row][col]) not in visited:
            oi[ord(arr[row][col])-65]= 1
            visited.add((row,col,string+arr[row][col]))
            per([row,col],length+1,string + arr[row][col])
            oi[ord(arr[row][col])-65]= 0
            count += 1
        if not count:
            result = max(result, length)
            
        
        
        
n, m = map(int,sys.stdin.readline().split())

arr = [list(sys.stdin.readline().strip()) for _ in range(n)]


result = 0
dx = [-1,1,0,0]
dy = [0,0,1,-1]
oi = [0]*26
oi[ord(arr[0][0]) - 65] = 1

visited = set()

visited.add((0,0,arr[0][0]))

per([0,0],1,arr[0][0])
print(result)