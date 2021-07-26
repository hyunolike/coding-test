import heapq

n = int(input())
data = list(map(int, input().split()))
slime = []
for d in data:
    heapq.heappush(slime, -d)
answer = 0
while len(slime)!=1:
    x = heapq.heappop(slime)
    y = heapq.heappop(slime)
    answer += (x*y)
    heapq.heappush(slime, (x+y))
print(answer)