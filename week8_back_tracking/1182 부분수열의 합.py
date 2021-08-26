
def DFS(L, total):
    global answer
    if L == n:
        return 0
    total += nums[L]
    if total == m:
        answer += 1
    DFS(L+1, total)
    DFS(L+1, total-nums[L])

n, m = map(int, input().split())
nums = list(map(int, input().split()))
answer = 0
DFS(0, 0)
print(answer)