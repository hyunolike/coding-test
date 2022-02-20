import sys
input=sys.stdin.readline
from collections import deque

N=int(input().rstrip())

A,B=map(int,input().split())

M=int(input().rstrip())

grid=[ [] for _ in range(N+1) ]

for _ in range(M):
    x,y=map(int,input().split())
    grid[x].append(y)
    grid[y].append(x)


Q=deque()
visit=[ 0 for _ in range(N+1)  ]

#print(grid)
def sol():        
    global result
    Q.append([grid[A],0])
    while Q:
        temp,chon=Q.popleft()
        if B in temp:
            result=chon+1
            break
        for i in temp:
            if visit[i]==0:
                visit[i]=1
                Q.append([grid[i],chon+1])


        
result=-1
if A==B:
    print(0)
else:
    sol()
    print(result)

#[[],   [],       [1],      [1],   [],   [4], [4], [2], [2], [2]]
#[[], [2, 3], [1, 7, 8, 9], [1], [5, 6], [4], [4], [2], [2], [2]]

# 9
# 3 3
# 7
# 1 2
# 1 3
# 2 7
# 2 8
# 2 9
# 4 5
# 4 6


# 5
# 3 4
# 4
# 2 3
# 3 4
# 1 2
# 4 5

#1
