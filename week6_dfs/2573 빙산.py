import sys
input = sys.stdin.readline

n,m = map(int, input().split())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

count_year = 0
while True:
    count_year+=1
    count_water = [[0]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if arr[i][j]>0:
                for k in range(4):
                    nx = i+dx[k]
                    ny = j+dy[k]
                    if 0<=nx<n and 0<=ny<m:
                        if arr[nx][ny]==0:
                            count_water[i][j] += 1
    
    for i in range(n):
        for j in range(m):
            if arr[i][j] > 0:
                arr[i][j] -= count_water[i][j]
                if arr[i][j]<0:
                    arr[i][j]=0

    glacier=0
    visited=[[False]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if arr[i][j]>0 and not visited[i][j]:
                glacier+=1
                visited[i][j]=True
                queue = [[i,j]]
                while queue:
                    p = queue.pop()
                    for k in range(4):
                        nx = p[0]+dx[k]
                        ny = p[1]+dy[k]
                        if 0<=nx<n and 0<=ny<m:
                            if arr[nx][ny]>0 and not visited[nx][ny]:
                                queue.append([nx, ny])
                                visited[nx][ny] = True
    if glacier>1:
        break
    
    total = 0
    for a in arr:
        total += sum(a)
    
    if total == 0:
        print(0)
        exit(0)
print(count_year)