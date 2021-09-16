import heapq

n = int(input())
heap = []
for _ in range(n):
    heapq.heappush(heap, list(map(int, input().split())))
end, fuel = map(int, input().split())

cases=[]
cnt=0
while fuel < end:
    while heap and heap[0][0] <= fuel: # 연료로 도달할 수 있는 곳 체크
        place, f = heapq.heappop(heap)
        heapq.heappush(cases, [-1*f, place])
    
    if not cases:
        cnt = -1
        break
    
    f, place = heapq.heappop(cases) # 가장 멀리갈 수 있는 곳 체크
    fuel += -1*f
    cnt += 1

print(cnt)
    