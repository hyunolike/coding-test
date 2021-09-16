import sys
import collections

n, k = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))
count = 0
summation = 0
dictionary = {0:1}

result = []

for i in range(n):
    summation += arr[i]

    if summation - k in dictionary:
        
        count += dictionary[summation-k]
    if summation in dictionary:
        dictionary[summation] += 1
    else:
        dictionary[summation] = 1
print(count)
