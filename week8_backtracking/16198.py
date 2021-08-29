import sys
n= int(sys.stdin.readline())

lst = list(map(int,sys.stdin.readline().split()))

max_val = 0



def dfs(value):
    global max_val
    if len(lst)== 2:
        max_val = max(value, max_val)
        return 0
    for i in range(1,len(lst)-1):
        val = lst[i]
        add_val = lst[i-1]*lst[i+1]
        del lst[i]
        dfs(value + add_val)
        lst.insert(i,val)

dfs(0)

print(max_val)