#11725 트리의 부모찾기

#문제풀이 

import sys
input = sys.stdin.readline
from collections import deque


N = int(input().rstrip())
tree = [[]for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
arr = deque([1])
ans ={}

for i in range(N-1):
    a,b = list(map(int,input().rstrip().split()))
    tree[a].append(b)
    tree[b].append(a)



while arr:
    node = arr.popleft()
    for i in tree[node]:
        if visited[i] == 0:
            ans[i] = node
            visited[i] = 1
            arr.append(i)

for j in range(2,N+1):
    print(ans[i])

