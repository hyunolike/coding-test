import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = list(map(int, input().split()))

arr = dict()
answer = 0
start, end = 0, 0
while end < n:
    if data[end] not in arr:
        arr[data[end]] = 1
    else:
        arr[data[end]] += 1
        if arr[data[end]] > k:
            answer = max(answer, end-start)
            while arr[data[end]] > k:
                arr[data[start]] -= 1
                start += 1
    end += 1

answer = max(answer, end-start)
print(answer)
