import heapq
import sys

input = lambda : sys.stdin.readline()

n = int(input())
slime = list(map(int, input().split()))
slime.sort(reverse=True)
i = 0
total = []

while len(slime) > 1:
    heapq.heappush(total, slime[i]*slime[i+1])
    slime[i] += slime[i+1]
    del(slime[i+1])

print(sum(total))