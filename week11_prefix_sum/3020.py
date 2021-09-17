import sys

n, h = map(int,sys.stdin.readline().split())

down =[0]*(h+1)

up = [0]*(h+1)

for i in range(n):
    if i%2 :
        down[int(sys.stdin.readline())] += 1
    else:
        up[int(sys.stdin.readline())] += 1
down.append(0)
up.append(0)
min_gap = n
min_gap_count = 0

for i in reversed(range(1,h+1)):
    down[i] = down[i]+down[i+1]
    up[i] = up[i]+up[i+1]
summation = 0

for i in range(1,h+1):
 
    if min_gap > down[i] + up[h+1-i]:
        min_gap = down[i]+up[h+1-i]
        min_gap_count = 1
    elif min_gap == down[i] + up[h+1-i]:
        min_gap_count += 1
print(min_gap, min_gap_count)