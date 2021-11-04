# 116
"""
1. 왼쪽방향부터 간다.
2. 왼쪽에 가보지 않았으면, 왼쪽 회전 + 한 칸 전진
3. 왼쪽에 다 가봤으면, 왼쪽 방향 회전
4. 모두 가봤거나 바다인 경우, 방향 유지한 채 한 칸 뒤로
5. 단, 뒤쪽이 바다이면 종료
"""

a,b=map(int, input().split())
x,y,dir=map(int, input().split())
graph=[list(map(int, input().split())) for _ in range(a)]
visited=[[0]*b for _ in range(a)]
visited[x][y]=1
answer=1

dx=[-1,0,1,0]
dy=[0,1,0,-1]

while True:
    ny=x+dx[dir]
    nx=y+dy[dir]
    if not visited[nx][ny]:
        visited[nx][ny]=1
        x,y=nx,ny
        dir=(dir+1)%4
    else:
        dir=(dir+1)%4
    break

# another solution
n,m=map(int, input().split())

d=[[0]*m for _ in range(n)]
x,y,direction=map(int,input().split())
d[x][y]=1

array=[]
for i in range(n):
    array.append(list(map(int, input().split())))

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def turn_left():
    global direction
    direction-=1
    if direction==-1:
        direction=3

count=1
turn_time=0
while True:
    turn_left()
    nx=x+dx[direction]
    ny=y+dy[direction]
    if d[nx][ny]==0 and array[nx][ny]==0:
        d[nx][ny]=1
        x,y=nx,ny
        count+=1
        turn_time=0
        continue
    else:
        turn_time+=1
    
    if turn_time==4:
        nx=x-dx[direction]
        ny=y-dy[direction]
        if array[nx][ny]==0:
            x=nx
            y=ny
        else:
            break
        turn_time=0
print(count)