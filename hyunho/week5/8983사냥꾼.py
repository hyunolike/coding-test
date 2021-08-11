import sys

input = sys.stdin.readline


def cal_dist(x, a, b):
    return abs(x - a) + b

def binary_search(start, end, i, L):
    global answer
    while start <= end:
        mid = start + (end - start) // 2
        if cal_dist(sand_bags[mid], animals[i][0], animals[i][1]) <= L:
            answer += 1
            break
        else:
            if sand_bags[mid] <= animals[i][0]:
                start = mid + 1
            else:
                end = mid - 1


M, N, L = map(int, input().split())
# 사대 위치
sand_bags = list(map(int, input().split()))
sand_bags.sort()

# 동물 좌표
animals = []

for i in range(N):
    tmp = tuple(map(int, input().split()))
    animals.append(tmp)

animals.sort()

answer = 0

for i in range(N):
    binary_search(0, M - 1, i, L)

print(answer)