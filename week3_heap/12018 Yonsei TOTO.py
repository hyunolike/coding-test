import heapq

n,m = map(int, input().split())
mylect = []
present = []
for _ in range(n):
    p, l = map(int, input().split())
    milege = list(map(int, input().split()))
    heapq.heapify(milege)
    heapq.heappush(present, [p-l, milege])

while present:
    data = heapq.heappop(present)
    if data[0]<0:
        heapq.heappush(mylect, -1)
    else:
        while data[0]!=0:
            heapq.heappop(data[1])
            data[0] -= 1
        heapq.heappush(mylect, -1 * heapq.heappop(data[1]))
while -1*sum(mylect) > m:
    heapq.heappop(mylect)
print(len(mylect))