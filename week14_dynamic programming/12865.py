import sys

n,m = map(int,sys.stdin.readline().split())

arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

result = []



for i in range(m+1):
    result.append([])
    for j in range(len(arr)+1):
        result[i].append(0)

for i in range(1,len(arr)+1):
    weight=arr[i-1][0]
    val = arr[i-1][1]
    
    for j in range(m+1):
        if j - weight < 0:
            result[j][i] = result[j][i-1]
        else:
            result[j][i] = max(result[j-weight][i-1] + val,result[j][i-1])




print(result[-1][-1])

