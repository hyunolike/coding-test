import sys
sys.setrecursionlimit(10*6)
input = lambda : sys.stdin.readline()

def dfs(num, arr):
    arr[num] = -2 # 배열값을 삭제한다는 의미 = -2
    for i in range(len(arr)):
        if num == arr[i]:
            dfs(i, arr) # 부모노드를 가진 노드를 찾아서 재귀호출

N = int(input())
arr = list(map(int, input().split()))
# print(arr)
k = int(input())
count = 0

dfs(k, arr)
count = 0

for i in range(len(arr)):
    if arr[i] != -2 and i not in arr: # -2가 아니면서 다른노드의 부모노드도 아닌 원소를 찾는 로직
        # print(arr[i], i, arr)
        count += 1

print(count)