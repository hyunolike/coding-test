import sys
from math import ceil

input = lambda : sys.stdin.readline()

n, l = map(int, input().split())
info = [list(map(int, input().split())) for i in range(n)]

info.sort()

res, s = 0, 0

for i in range(n):
  s = max(info[i][0], s) 
  diff = info[i][1] - s
  count = ceil(diff / l)

  res += count
  s += count + l

print(res)