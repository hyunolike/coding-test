n = int(input())
city = [list(map(int, input().split())) for i in range(n)]
visited = [0]*n
answer = 2e10

def DFS(start, total):
    global answer
    if total < answer:
        if all(visited) and start==0:
            answer = min(answer, total)
        for next in range(n):
            if city[start][next]!=0 and not visited[next]:
                visited[next] = 1
                DFS(next, total+city[start][next])
                visited[next] = 0
DFS(0, 0)
print(answer)