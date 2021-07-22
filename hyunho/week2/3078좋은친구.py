import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())

inp = [len(input()) for i in range(N)]
num = [0 for i in range(22)]

cnt = 0
for i in range(3, 22):
  q = deque()
  for leng in inp:
      q.append(leng)
      if len(q) > K + 1:
          if q.popleft() == i: num[i] -= 1
      if leng == i:
          if num[i] > 0: cnt += num[i]
          num[i] += 1

print(cnt)    
