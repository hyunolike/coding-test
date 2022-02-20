import sys
input=sys.stdin.readline
R,C=map(int,input().split())

s=list()
for _ in range(R):
    s.append(input().rstrip())

stack=[ s[0][0] ]


res=[]
def dfs(x,y):
    global res
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    for i in range(4):
        mx=x+dx[i]
        my=y+dy[i]
        if (0 <= mx <R) and (0 <= my < C) and s[mx][my] not in stack:
                stack.append(s[mx][my])
                res.append(len(stack))
                dfs(mx,my)
                stack.remove(s[mx][my])

dfs(0,0)
print(max(res))
