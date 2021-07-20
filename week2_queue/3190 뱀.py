from collections import deque

def change(d,c):
    if c == 'L':
        d = (d-1)%4
    else:
        d = (d+1)%4
    return d

def solution(map, times, n):
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    x, y = 0,0
    snake = deque()
    snake.append([y,x])
    direction = 1
    seconds = 1

    while True:
        x, y = x+dx[direction], y+dy[direction]
        if 0<=x<n and 0<=y<n and map[y][x]!=-1:
            if not map[y][x] == 1: # 사과가 없는 경우
                last_y, last_x = snake.popleft()
                map[last_y][last_x] = 0
            map[y][x]=-1
            snake.append([y,x])
            if seconds in times.keys():
                direction = change(direction, times[seconds])            
            seconds += 1
        else:
            return seconds

n = int(input())
k = int(input())
map = [[0]*n for i in range(n)]
for i in range(k):
    x, y = input().split()
    map[int(x)-1][int(y)-1]=1
l = int(input())
times = dict()
for i in range(l):
    a, b = input().split()
    times[int(a)] = b
print(solution(map, times, n))