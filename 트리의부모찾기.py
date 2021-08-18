import sys
input = sys.stdin.readline

n= int(input())
tree = [[] for i in range(n+1)]

for i in range(n-1):
    a, b = list(map(int, input().split()))
    tree[a].append(b) # 서로 연결
    tree[b].append(a)
queue = [1] # 1부터 시작하므로 시작전에 큐에 1을 넣어줌.
visit = [0 for i in range(n+1)] # 방문된 곳인지 여부를 확인하기 위해
result = {} #result[4]는 4번 노드의 부모가 담김.

while queue:
    now = queue.pop(0) # 현재 가르키는 노드. 처음엔 1이 온다.
    for i in tree[now]: # tree[1]에 있는 요소를 꺼냄. tree[1]에는 4와 6
        if visit[i] ==0: # 방문한적이 없으면
            result[i]=now # 4번 노드에 대한 출력값으로 부모인 now=1 삽입
            visit[i] =1 # 방문했으므로 1로 변경
            queue.append(i) # 큐에 추가해 다음 탐색을 이어가도록.
for i in range(2, n+1):
    print(result[i])
