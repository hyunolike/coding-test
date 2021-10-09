import sys

str1 = sys.stdin.readline().strip()

str2 = sys.stdin.readline().strip()

result = []

for i in range(len(str1)+1):
    result.append([])
    for j in range(len(str2)+1): 
        result[i].append(0)

for i in range(1,len(str1)+1):
    for j in range(1,len(str2)+1):
        col = str1[i-1]
        row = str2[j-1]
        if col == row:
            result[i][j] = max(max(result[i-1][j-1]+1, result[i-1][j]),result[i][j-1])
        else:
            result[i][j] = max(max(result[i-1][j-1],result[i-1][j]),result[i][j-1])


print(result[len(str1)][len(str2)])