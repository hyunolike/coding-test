import sys
import collections
from itertools import combinations


n, m, d = map(int,sys.stdin.readline().split())

ptr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

#m개중 3개를 뽑아야 될거 같은데
dx = [0,-1,0]
dy = [-1,0,1]
Castle = combinations(list(range(m)),3)
max_count = 0
stack = collections.deque([])
for t in Castle:
    this_count = 0
    arr = []
    for q in range(n):
        arr.append([])
        for q2 in range(m):
            arr[q].append(ptr[q][q2])
   
    for k in range(n): # n개의 row에 대해서
        have_to = []
       
        for i in range(3): # 3개의 아쳐가 각각 잡는거임
            visited = [[1]*m for _ in range(n)]
            stack.clear()
            stack.append((n-k-1,t[i],1))
            
            flag = 0
            visited[n-k-1][t[i]] = 0
            while len(stack):
                this_row, this_col, length = stack.popleft()
                
                if length > d:
                    break
                if length <= d and arr[this_row][this_col]:
                   
                    have_to.append([this_row,this_col])
                    break
                
                for j in range(3):
                    row = this_row + dx[j] 
                    col = this_col + dy[j] 
                    if 0 <= row < n and 0 <= col < m and visited[row][col]:
                        visited[row][col] = 0
                        stack.append((row,col,length+1))
                if flag:
                    break
       
        for p in have_to:
            if arr[p[0]][p[1]] :
                this_count += 1
                arr[p[0]][p[1]] = 0
       
                
    
    max_count = max(max_count, this_count)
print(max_count)
    

            