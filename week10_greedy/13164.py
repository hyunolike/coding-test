import sys

n, k = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))

result = [arr[i]- arr[i-1] for i in range(1,n)]
result.sort()
sum = 0
for i in range(n-k):
    sum += result[i]
print(sum)