#2667 단지 번호 붙이기

#문제풀이 1:

import sys
input =sys.stdin.readline
N = int(input().rstrip())
arr = [list(input().strip()) for _ in range(N)]
visited = [[0]* N for _ in range(N)]
house = []
count = 0

def Search(i,j):
    global count
    if i < 0 or j < 0 or i>N-1 or j > N-1 or visited[i][j] == 1 or arr[i][j] == '0':
        return
    visited[i][j] = 1
    count = count + 1
    Search(i-1,j)
    Search(i+1,j)
    Search(i,j-1)
    Search(i,j+1)
    
    
for i in range(N):
    for j in range(N):
        
        if visited[i][j] == 0 and arr[i][j] == '1':
                
                Search(i,j)
                house.append(count)
                count= 0

print(len(house))
for k in sorted(house):
    print(k)