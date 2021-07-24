import heapq

n, m = map(int, input().split())
data = list(map(int, input().split()))
heapq.heapify(data)

for _ in range(m):
    a = heapq.heappop(data)
    b = heapq.heappop(data)
    c = a + b
    heapq.heappush(data, c)
    heapq.heappush(data, c)

print(sum(data))