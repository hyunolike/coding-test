import sys

n, k = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))

Max_len = 0
idx = 0
cant_idx = -1
length = 0

while idx<n-1:
    if arr[idx]<=k:
        length+=1
        idx+=1
    else:
        if cant_idx>=0:
       
            Max_len = max(Max_len,length)
            
            idx = cant_idx+1
            cant_idx = -1  
            length = 0
        else:
            cant_idx = idx
            length+=1
            idx+=1
Max_len=max(Max_len, length)    

print(Max_len+1)