import sys

input = lambda : sys.stdin.readline()

n = int(input())
arr = list(map(int , input().split()))

for _ in range(n-1):
    temp = sorted(list(map(int, input().split())) + arr)
    arr = temp[n:]


print(arr[0])