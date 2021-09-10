import sys

t = int(sys.stdin.readline())
real = []
for _ in range(t):
    n = int(sys.stdin.readline())

    arr = sorted([list(map(int,sys.stdin.readline().split())) for _ in range(n)], key = lambda x : x[0])
    
    Max = arr[0][1]
    count = 1
    for i in range(1,n):
        if Max > arr[i][1]:
             count += 1
             Max = arr[i][1]
    real.append(count)
for i in real:
    print(i)
   
    