import sys


def per(idx,length):
    global result
    count = 0
    for i in range(4): 
        row = idx[0] + dx[i]
        col = idx[1] + dy[i]
            
        if 0<=row<=n-1 and 0<=col<=n-1 and not oi[arr[row][col]]:
            oi[arr[row][col]]= 1
            per([row,col],length+1)
            oi[arr[row][col]]= 0
            count += 1
        if not count:
            result = max(result, length)
            
        
        
        
n, m = map(int,sys.stdin.readline().split())

arr = [list(map(lambda x: ord(x)-65,sys.stdin.readline().strip())) for _ in range(n)]


result = 0
dx = [-1,1,0,0]
dy = [0,0,1,-1]
oi = [0]*26
oi[arr[0][0]] = 1


per([0,0],1)
print(result)