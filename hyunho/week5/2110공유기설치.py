import sys

input = lambda : sys.stdin.readline()

N, C = map(int, input().split())

house = [int(input().rstrip()) for _ in range(N)]
house.sort()

def binary_search(array, start, end):
    while start <= end:
        mid = start + (end - start) // 2
        current = array[0]
        count = 1

        for i in range(1, len(array)):
            if array[i] >= current + mid:
                count += 1
                current = array[i]

        if count >= C:
            global result
            start = mid + 1
            result = mid
        else:
            end = mid - 1

start = 1
end = house[-1] - house[0]
result = 0

binary_search(house, start, end)
print(result)