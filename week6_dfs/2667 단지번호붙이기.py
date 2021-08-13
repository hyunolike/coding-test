n = int(input())
graph = list(list(map(int, input())) for _ in range(n))
visited = [[0]*n for _ in range(n)]
answer = []
cnt = 0

def search(i, j):
    global cnt
    if i<0 or j>=n or i>=n or j<0 or graph[i][j]==0:
        return
    graph[i][j]=0
    visited[i][j]=1
    cnt += 1
    
    search(i+1, j)
    search(i, j+1)
    search(i-1, j)
    search(i, j-1)

for i in range(n):
    for j in range(n):
        if visited[i][j]==0 and graph[i][j]==1:
            search(i,j)
            answer.append(cnt)
            cnt = 0

print(len(answer))
for i in sorted(answer):
    print(i)
