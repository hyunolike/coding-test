import heapq
import sys

input = lambda : sys.stdin.readline()
n = int(input())
arr = []
sorted_arr = []
room = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

sorted_arr = sorted(arr, key = lambda x: x[0])

for i in range(n):
    if room and room[0] <= sorted_arr[i][0]:
        heapq.heappop(room)
    heapq.heappush(room,sorted_arr[i][1])

print(len(room))
