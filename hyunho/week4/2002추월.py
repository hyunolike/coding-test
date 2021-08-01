import sys
from collections import defaultdict

input = lambda : sys.stdin.readline().rstrip()

a = defaultdict(int)
b = []

n = int(input())
answer = 0

for i in range(n):
    car = input()
    a[car] = i

for _ in range(n):
    car = input()
    b.append(car)

for i in range(n-1):
    for j in range(i+1, n):
        if a[b[i]] > a[b[j]]:
            answer += 1
            break
            
print(answer)