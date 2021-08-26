import sys

def dfs(visited, count,string,before):
    if count == l:
        this_count = 0
        for i in string:
            if i == 'a' or i == 'i' or i == 'e' or i == 'o' or i == 'u':
                this_count += 1
        if this_count >= 1 and l - this_count >= 2:
            result.append(string)
        return
    for i in visited:
        if before < i:
            dfs(visited - {i}, count+1, string+i, i)
        

l , c = map(int,sys.stdin.readline().split())

arr = list(sys.stdin.readline().split())

result = []
for alphabet in arr:
    visited = set(arr)
    visited.remove(alphabet)
    dfs(visited,1,alphabet,alphabet)
result.sort()
for i in result:
    for j in i:
        print(j,end='')
    print('')