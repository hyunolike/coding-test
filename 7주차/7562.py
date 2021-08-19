import sys
input=sys.stdin.readline
sys.setrecursionlimit(1000000)
from collections import deque
dx = [+2, +1, -1, -2, -2, -1, +1, +2]
dy = [+1, +2, +2, +1, -1, -2, -2, -1]


def sol(a,b):
    if a==c and b==d:
        print(0)
        return
    queue=deque()
    queue.append([a,b])
    while queue:
        x,y=queue.popleft()
        if x==c and y==d:
            print(visit[x][y])
            return
        for i in range(8):
            mx=x+dx[i]
            my=y+dy[i]
            if (0<=mx<l) and (0<=my<l):
                if visit[mx][my]==0:
                    visit[mx][my]=visit[x][y]+1
                    queue.append([mx,my])
                    print(queue,'queue')
        #print(visit)

    


T=int(input().rstrip())
for _ in range(T):
    l=int(input().rstrip())
    a,b=map(int,input().split())
    c,d=map(int,input().split())
    visit=[ [0]*l for _ in range(l)]
    sol(a,b)
# 1
# 8
# 0 0
# 7 0