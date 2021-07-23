#3190 뱀
#문제풀이  1. 방향 설정하는것은 코드 길어서 따로 함수로 편집
#2.디큐를 사용해서 시간 복잡도 감소
#3. 뱀의 위치를 2차원 배열을 통해 구현 + 사과의 위치를  1로 따로 표시해서 구현
#4 특정 위치 -> 방향전화  ==> 딕셔너리 사용
from collections import deque

arr = []
snake = deque()
Dir = {}
N = int(input().strip())
Location = [[0 for _ in range(N)]for _ in range(N)]
Ap = int(input().strip())
for i in range(Ap):
    a,b = map(int,input().split())
    Location[a-1][b-1] = 7
#지도 형태 구현을 위해 2차원배열 이용,사과위치를 7로 구현
Di = int(input().strip())
for j in range(Di):
    a,b = input().split()
    Dir[int(a)] = b
#시간 입력시 방향을 도출해 내기 위해 DIC 사용

def Direction(move,D):
    x,y = move
    if x == 0:
        if D == 'D':
            if y>0:
                return(-1,0)
            else:
                return(1,0)
        else:
            if y>0:
                return(1,0)
            else:
                return(-1,0)
    elif y ==0:
        if D =='D':
            if x>0:
                return(0,1)
            else:
                return(0,-1)
        else:
            if x>0:
                return(0,-1)
            else:
                return(0,1)

Location[0][0] = 1
x,y = 0,0
time = 0
move = (1,0)
snake.appendleft((0,0))

while True:
    time = time + 1
    
    a,b = move
    x,y = x+a,y+b
    
    if 0 <= x < N and 0 <= y <N:
        if Location[y][x] == 7:
            snake.appendleft((y,x))
           
            Location[y][x] = 1
        elif Location[y][x] ==0:
            
            Location[y][x] = 1
            snake.appendleft((y,x))
            a,b = snake.pop()
            Location[a][b] = 0
        elif Location[y][x] == 1:
            
            break
        if time in Dir:
            
            move = Direction(move,Dir[time])
    else:
        break
print(time)