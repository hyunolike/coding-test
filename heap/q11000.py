import sys
import heapq as heap

input = sys.stdin.readline
n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]
times.sort()  # 시작시간이 빠른 것 부터 정렬

in_use = []  # 끝 시간을 적을 힙
heap.heapify(in_use)

heap.heappush(in_use, times[0][1])  # 첫 강의
for i in range(1, len(times)):
    if in_use[0] <= times[i][0]:  # 사용ㅇ: 기존의 가장 빨리 끝나는 시간 <= 현재강의 시작시간
        heap.heappop(in_use)
        heap.heappush(in_use, times[i][1])
    else:  # 사용x: push
        heap.heappush(in_use, times[i][1])

print(len(in_use))
