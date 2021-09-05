import sys
import collections



n, l, w = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))

road = []

length = 0
time = 0
weight = 0 
idx = 0

while idx < n:
    if length == l:
        this_turn_out = road[0]
        del road[0]
        weight -= this_turn_out
        length-=1
    
    if weight + arr[idx] <= w:
        road.append(arr[idx])
        weight += arr[idx]
        idx += 1
        length +=1
    else:
        road.append(0)
        length+=1
    time+=1

print(time+l)   

    
        
