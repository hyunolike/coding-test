# Week3 Heap 발표자료

## [1.3190 뱀](https://www.acmicpc.net/problem/3190)

![pa1](https://user-images.githubusercontent.com/87264787/127296052-5163e4ba-0fd5-49f8-b0ad-5b88a310981a.png)


### 1.1 자료구조

1. 뱀의 이동은 꼬리와 머리의 이동으로 이루어지기 때문에 리스트의 앞 뒤부분 둘다 삽입,삭제 가능해야되므로
    deque 사용

2. 좌표계를 구현하기 위해서 2차원 배열 사용 이때 사과위치,비어있는곳,뱀이 잇는곳 3가지를 값의 차이를   
   가지고 구현

3. 시간에 따른 방향 변화를 구현하기 위해 딕셔너리 자료형 사용

### 1.2 풀이 과정

1.  이차원 배열을통해 보드 와 사과의 위치를 식별해주는 것을 구현

2. 딕셔너리를 통해 시간에 따른 방향 전환을 구현

2.5 디렉션 함수를 생성하여 현재 방향에 따른 방향변화를 구현

3. 반복문을 통해 뱀의 이동을 구현 이때 x,y 좌표를 조건과 같이 잘 넣어햐 함.
    큰 조건 : 벽을 만날시
    세부조건 :
   조건1. 사과가 잇을시  
   조건2. 뱀이 이미 그자리에 있을시 
   조건3. 아무것도 없을시

   + 시간에 따른 방향전환

4. 마지막 시간출력
   



### 1.3 소스 코드

```python
#3190 뱀

#현재 뱀의 머리 방향에 따른 방향변화를 구현
from collections import deque

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

# 필요 선언문 + 입력

arr = []
snake = deque()
Dir = {}
N = int(input().strip())
Ap = int(input().strip())

#지도 형태 구현을 위해 2차원배열 이용,사과위치를 7로 구현

Location = [[0 for _ in range(N)]for _ in range(N)]

for i in range(Ap):
    a,b = map(int,input().split())
    Location[a-1][b-1] = 7


#시간 입력시 방향을 도출해 내기 위해 딕셔너리 사용 사용

Di = int(input().strip())

for j in range(Di):
    a,b = input().split()
    Dir[int(a)] = b



#기본 셋팅 설정
Location[0][0] = 1
x,y = 0,0
time = 0
move = (1,0)
snake.appendleft((0,0))


#뱀의 이동 구현
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
```
