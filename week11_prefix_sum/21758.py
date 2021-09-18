import sys
n = int(sys.stdin.readline())

bee = list(map(int,sys.stdin.readline().split()))

result = [bee[0]]

for i in range(1,len(bee)):
    result.append(result[i-1]+bee[i])

max_bee = 0

#벌 꿀 벌
for i in range(1,n-1):
    max_bee = max( max_bee, result[i] - result[0] + result[n-2]-result[i-1])

#꿀 벌 벌
for i in range(1, n-1):
    max_bee = max(max_bee, result[n-2] - result[i] + 2*(result[i-1]))
#벌 벌 꿀
for i in range(1,n-1):
    max_bee = max(max_bee, result[i-1]- result[0] + 2*(result[n-1] - result[i]))

print(max_bee)
