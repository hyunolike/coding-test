from math import inf
import sys
input = lambda : sys.stdin.readline()

N = int(input())
numbers = sorted(list(map(int, input().split())))


def binary_search(numbers):
    start, end = 0, N - 1
    max_value = float(inf)

    while start < end:

        tmp = numbers[start] + numbers[end]
        print(tmp)
        if tmp == 0:
            return numbers[start], numbers[end]
        if abs(tmp) < max_value:
            result = (numbers[start], numbers[end])
            # print(result)
            max_value = abs(tmp)
        if tmp > 0:
            end -= 1
        else:
            start += 1
    return result

result = binary_search(numbers)
print(result[0], result[1])