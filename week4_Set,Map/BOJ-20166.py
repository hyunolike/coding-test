
#수)  20166 문자열 지옥에 빠진 호석
#BFS

# 문제풀이 1.좌표계 구현 + 범위넘어갈시 처리  2.dfs 탐색 + return 조건 파악해서 모든 경우의수 도출



import sys
input = sys.stdin.readline

N,M,K =list(map(int,input().split()))
Map = []
ans ={}
dir = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

for _ in range(N):
   Map.append(list(input()))

def dfs(x,y,Root):
       ans[Root] = ans.get(Root,0)+1
       if len(Root) == 5:
              return
       for i in range(8):
              dir_x =(x + dir[i][0])%N
              dir_y =(y + dir[i][1])%M
              dfs(dir_x,dir_y,Root+Map[dir_x][dir_y])

for i in range(N):
    for j in range(M):
        dfs(i, j, Map[i][j])

for _ in range(K):
   print(ans.get(input().rstrip(), 0))