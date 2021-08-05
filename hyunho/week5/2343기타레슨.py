import sys

input = lambda : sys.stdin.readline()

def add_lesson():
    cnt = 0
    sum_lesson = 0
    for i in range(N):
        if sum_lesson + lesson[i] > mid:
            cnt += 1
            sum_lesson = 0
        sum_lesson += lesson[i]
    else:
        if sum_lesson:
            cnt += 1
    return cnt

N, M = map(int, input().split())
lesson = list(map(int, input().split()))

right = sum(lesson)
left = max(lesson)


while left <= right:
    mid = left + (right - left) // 2
    cnt = add_lesson()
    if cnt <= M:
        right = mid - 1
    elif cnt > M:
        left = mid + 1


print(left)