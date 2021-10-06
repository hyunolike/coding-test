import sys

n = int(sys.stdin.readline())

min_count = 0

first = n//5

for i in range(first+1):
    if (n-(i*5))%3 == 0:
        min_count = (n-(i*5))//3 + i
    

if min_count :
    print(min_count)
else:
    print(-1) 