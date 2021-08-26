
def DFS(y, x):
    for i in range(y):
        if x==vx[i]: return 0
        if y==vy[i]: return 0
        if abs(x-vx[i])==abs(y-vy[i]): return 0
    
    if y == n-1:
        return 1
    
    vx[y] = x
    vy[y] = y
    
    answer = 0
    for i in range(n):
        answer += DFS(y+1, i)
    return answer

n = int(input())
vx, vy = [0]*(n+1), [0]*(n+1)
answer = 0
for i in range(n):
    answer += DFS(0, i)
print(answer)