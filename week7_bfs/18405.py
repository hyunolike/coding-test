import sys
import collections
n, k = map(int,sys.stdin.readline().split())

arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

s, x, y = map(int,sys.stdin.readline().split())

count = 0
dx = [-1,0,1,0]
dy = [0,1,0,-1]

visited = [[1]* n for _ in range(n)]


while(count!=s):
    count += 1
    
    stack = collections.deque([])
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                min_val = k+1
                count_a = 0
                for t in range(4):
                    row = i + dx[t]
                    col = j + dy[t]
                    if 0 <= row < n and 0 <= col < n and arr[row][col] != 0:
                        count_a += 1
                        min_val = min(arr[row][col], min_val)
                if count_a:
                    stack.append((i,j,min_val))
    while stack:
        this_turn = stack.pop()
        arr[this_turn[0]][this_turn[1]] = this_turn[2]
 
    
                        
print(arr[x-1][y-1])