import sys
import heapq

def sol(n,stations,l,p):
    stations.sort(reverse=True)
    heap = []

    count = 0

    while p<l:
        while stations and stations[-1][0] <= p:
            dist, fuel = stations.pop()
            heapq.heappush(heap, -fuel)
        if not heap:
            break
        p -=heapq.heappop(heap)
        count+=1
    if l<=p:
        return count
    return -1

n = int(sys.stdin.readline())

stations = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

goal, gas = map(int,sys.stdin.readline().split())

print(sol(n,stations,goal,gas))