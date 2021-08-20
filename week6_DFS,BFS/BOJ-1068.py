#1068 트리

#문제풀이 1.트리 구조를 어캐구현 했더라?
#파이썬 트리구조 = 2차원배열 or  딕셔너리

import sys
input =sys.stdin.readline
from collections import deque

N = int(input().rstrip())
arr = deque([] for _ in range(N))
Node = list(map(int,input().rstrip().split()))
K = int(input().rstrip())
cnt = 0
root = -1

for i in range(N):
    if Node[i] == -1:
        root = i
    else:
        arr[Node[i]].append(i)

def dfs(node):
    global cnt
    if not arr[node]:
        cnt += 1
        return

    for j in range(len(arr[node])):
        if arr[node][j] == K:
            if len(arr[node]) == 1:
                cnt += 1
            else:
                continue
        else:
            dfs(arr[node][j])
   

if K == root:
    print(0)
else:
    dfs(root)
    print(cnt)





