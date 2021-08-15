#1987 알파벳

#문제풀이 1: DFS로풀었지만 시간초과가 나기 거의 직전수준
#다시한번 BFS접근이 시간초과로 부터 쟈유롭다는걸 깨달음

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)
ans = 0

def dfs(x, y, word):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    global ans
    check = 0
    for k in range(4): 
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m and words[nx][ny] not in word:  
            dfs(nx, ny, word+words[nx][ny])
        else:
            check += 1    
    if check == 4:
        ans = max(ans, len(word))
        return



n, m = map(int, input().split()) 
words = [list(input().rstrip()) for _ in range(n)]
dfs(0, 0, words[0][0])
print(ans)