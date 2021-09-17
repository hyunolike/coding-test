import sys

input = sys.stdin.readline

n, h = map(int, input().split())  # 길이, 높이

# 길이 별 장애물 저장
high = [0] * h  # 종유석
low = [0] * h  # 석순

# 종유석, 석순 입력 받기
for j in range(n // 2):
    i = int(input())
    high[i - 1] += 1
    i = int(input())
    low[h - i] += 1
if n % 2 == 1:
    i = int(input())
    low[h - i] += 1

# 종유석은 역순으로 누적 합, 석순은 정방향 누적 합 계산
for i in range(1, h):
    high[h - i - 1] += high[h - i]
    low[i] += low[i - 1]

# 두 배열을 합치면 경로 별 장애물 개수가 나옴
answer = [high[i] + low[i] for i in range(h)]

# 최솟값 및 개수 구하기
min = 200001
count = -1
for idx in range(len(answer)):
    if answer[idx] < min:
        min = answer[idx]
        count = 1
    elif answer[idx] == min:
        count += 1

print(min, count)