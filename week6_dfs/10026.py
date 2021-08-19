import sys
import collections
n = int(sys.stdin.readline())

arr = [list(sys.stdin.readline().strip()) for _ in range(n)]

count = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0 ,-1]
visit = []
visit_eye = []
for i in range(n):
    visit.append([])
    for j in range(n):
        visit[i].append(True)
for i in range(n):
    visit_eye.append([])
    for j in range(n):
        visit_eye[i].append([True])
compare = {'R':1, 'G':1,'B':-1}
count_eye = 0
stack1 = collections.deque([])
for i in range(n):
    for j in range(n):
        if visit[i][j]:
           
            count+=1
            visit[i][j] = False
            stack1.append([i,j])
            while(len(stack1)):
                this_turn = stack1.pop()
                this_row = this_turn[0]
                this_col = this_turn[1]
                
                for k in range(4):
                    row = this_row + dx[k]
                    col = this_col + dy[k]
                   
                    if row>=n or row<=-1 or col>=n or col<=-1 or visit[row][col] == False:
                        continue
                    if arr[row][col] == arr[this_row][this_col]:
                       
                        stack1.append([row,col])
                        visit[row][col] = False
        if visit_eye[i][j]:
            count_eye+=1
            visit_eye[i][j] = False
            stack1.append([i,j])
            while(len(stack1)):
                this_turn = stack1.pop()
                this_row = this_turn[0]
                this_col = this_turn[1]
                for k in range(4):
                    row = this_row + dx[k]
                    col = this_col + dy[k]
                    if row>=n or row<=-1 or col>=n or col<=-1 or visit_eye[row][col] == False:
                        continue
                    if compare[arr[row][col]] == compare[arr[this_row][this_col]]:
                        stack1.append([row,col])
                        visit_eye[row][col] = False
print(count,count_eye)