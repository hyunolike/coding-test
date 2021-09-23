import math

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

def pooling(graph):
    length = len(graph)
    l = length//2
    res = [[0]*l for _ in range(l)]
    nx = 0
    for x in range(0, length, 2):
        ny = 0
        for y in range(0, length, 2):
            window = [graph[x][y], graph[x+1][y], graph[x][y+1], graph[x+1][y+1]]
            window.sort(reverse=True)
            res[nx][ny] = window[1]
            ny += 1
        nx += 1
    
    return res

def solve():
    answer = graph

    for _ in range(int(math.log2(n))):
        answer = pooling(answer)
    
    return answer[0][0]

print(solve())