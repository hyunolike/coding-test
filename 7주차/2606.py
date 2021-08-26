import sys
input=sys.stdin.readline
from collections import deque


numberOfComputers=int(input().rstrip())


numberOfConnections=int(input().rstrip())

network=[ [] for _ in range(numberOfComputers+1) ]
visit=[ 0 for _ in range(numberOfComputers+1)]
visit[1]=1
for i in range(numberOfConnections):
    a,b=map(int,input().split())
    network[a].append(b)
    network[b].append(a)


queue=deque()
queue.append((network[1]))
count=0
while queue:
    temp=queue.popleft()
    for i in temp:
        if visit[i]==0:
            visit[i]=1
            count+=1
            queue.append((network[i]))
            
print(count)
