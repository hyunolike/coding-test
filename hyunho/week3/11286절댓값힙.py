# 1차 풀이
import heapq
import sys

input = lambda : sys.stdin.readline()

n = int(input())
arr_plus = []
arr_minus = []

for _ in range(n):

    x = int(input())

    if x > 0:
        heapq.heappush(arr_plus, x)
    elif x < 0:
        heapq.heappush(arr_minus, -x)
    elif x == 0:
        if not arr_plus and not arr_minus:
            print(0)
        else:
            if arr_minus and not arr_plus:
                print(-heapq.heappop(arr_minus))
            elif arr_minus and arr_plus and arr_minus[0] <= arr_plus[0]:
                print(-heapq.heappop(arr_minus))
            else:
                print(heapq.heappop(arr_plus))

# 개선된 풀이
import sys
import heapq
numbers = int(input())
heap = []
for _ in range(numbers):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, (abs(num), num))
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)        