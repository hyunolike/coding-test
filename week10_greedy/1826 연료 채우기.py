import heapq

n = int(input())
heap = []
for _ in range(n):
    heapq.heappush(heap, list(map(int, input().split())))
end, fuel = map(int, input().split())

cases=[]
cnt=0
while fuel < end:
    while heap and heap[0][0] <= fuel:
        place, f = heapq.heappop(heap)
        heapq.heappush(cases, [-1*f, place])
    
    if not cases:
        cnt = -1
        break
    
    f, place = heapq.heappop(cases)
    fuel += -1*f
    cnt += 1

print(cnt)
    