import sys
import heapq as heap

input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))

heap.heapify(cards)  # list to heap

for _ in range(m):
    sum_value = heap.heappop(cards) + heap.heappop(cards)
    heap.heappush(cards, sum_value)
    heap.heappush(cards, sum_value)

print(sum(cards))

'''
heap으로 만들어서
가장 작은 수 두 개를 뽑고 합을 다시 2번 넣어줌(카드 수 유지)
heap을 더함
'''
