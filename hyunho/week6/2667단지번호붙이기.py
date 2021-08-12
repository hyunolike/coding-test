import sys
input = lambda : sys.stdin.readline()

N = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
count, result = 0, 0
arr = []
house = []

def dfs(x, y):
    global result
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= N or y <= -1 or y >= N:
        return False
    if graph[x][y] == 1:
        # 해당 노드를 방문 처리
        graph[x][y] = "#"
        result += 1
        # 상,하,좌,우의 위치도 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

for i in range(N):
    for j in range(N):
        if dfs(i,j) == True:
            house.append(result)
            count += 1
            result = 0
house.sort()
print(count)
print('\n'.join(str(h) for h in house))