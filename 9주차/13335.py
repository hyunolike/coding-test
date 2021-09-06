
from collections import deque
n,w,L=map(int,input().split())
trucks=deque(map(int,input().split()))


unitTime=1

bridge=[0 for _ in range(w)] 

bridge[-1]=trucks.popleft()
while trucks:
    if sum(bridge[1:])+trucks[0] <= L:
        bridge[0:-1] = bridge[1:]
        bridge[-1] = trucks.popleft()
        unitTime += 1
    else:
        bridge[0:-1] = bridge[1:]
        bridge[-1] = 0
        unitTime += 1

print(unitTime+w)

