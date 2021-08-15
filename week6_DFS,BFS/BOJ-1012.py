#1012 유기농 배추

# 문제풀이 1:

import sys
sys.setrecursionlimit(10 ** 5)  # dfs로 풀다가 오기생겨서 여기까지옴 
                                # 파이썬 = 기본재귀 깊이가 얕음 //따라서 리미트해제
input = sys.stdin.readline
count = 0
T = int(input().rstrip()) # 테스트케이스 갯수 

def dfs(x,y):   
               
    global count
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx >= N or nx < 0 or ny >= M or ny < 0 or visited[nx][ny]:
            continue
        if arr[nx][ny] != 0:
            visited[nx][ny] = 1
            dfs(nx, ny)

    

for _ in range(T):
      count = 0
      M,N,K =map(int,input().rstrip().split())
      arr = [[0]*M for _ in range(N)]
      visited = [[0]*M for _ in range(N)]
      for _ in range(K):
            a,b=map(int,input().split())
            arr[b][a]=1


      for i in range(N):
            for j in range(M):
                  if arr[i][j]==1 and visited[i][j] ==0:
                        visited[i][j] =1
                        count += 1
                        dfs(i,j)
      print(count)





  
