
def DFS(n):
    if n==0:
        return 0
    DFS(n//2)
    print(n%2, end='')
    
n=int(input())
DFS(n)

# 11: DFS(11), DFS(5), DFS(2), DFS(1), DFS(0)
# 0, -> 1, 0, 1, 1
