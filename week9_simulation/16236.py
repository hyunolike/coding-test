import sys

n = int(sys.stdin.readline())

shark = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

for i in zip(dx,dy):
    print(i)