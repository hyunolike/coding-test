#18405 경쟁적 전염

"""
문제풀이 1: 전형적인 bfs 느낌 잘알아두기
"""
import sys
input = sys.stdin.readline
from collections import deque


data = []
Map = []
dx =[-1,1,0,0]
dy =[0,0,-1,1]

N,K =map(int,input().rstrip().split())
for i in range(N):
    tmp =list(map(int,input().rstrip().split()))
    for j in range(N):
        if tmp[j] != 0:
            data.append([tmp[j],0,i,j])
    Map.append(tmp)


x,y,virus =map(int,input().rstrip().split())

data.sort()
arr =deque(data)

while arr:
    vv ,s ,xx,yy = arr.popleft()
    if s == x:
        break
    for i in range(4):
        nx ,ny = xx + dx[i],yy +dy[i]
        if 0<= nx <N and 0 <= ny <N :
            if Map[nx][ny] ==0:
                Map[nx][ny] =vv
                arr.append([vv,s+1,nx,ny])

print(Map[x-1][y-1])