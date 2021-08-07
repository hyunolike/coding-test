import sys
input = lambda : sys.stdin.readline()

N, M = map(int, input().split())
tree = list(map(int, input().split()))

start = 1
end = max(tree)

while start <= end:
    mid = start + (end-start) // 2
    result = 0

    # 합산 계산하는 부분에서 python3 시간 초과 발생 
    # sum() 함수로 개선
    result = sum(t - mid if t - mid > 0 else 0 for t in tree) 

    # print(result)
    if result >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)