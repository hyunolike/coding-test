def get_bound_end(idx):
    num = arr[idx]
    prev_power, power = 1, 1
    bound = idx
    while True: # 이중 while문으로 잡음
        left, right = bound+1, N-1 # 범위를 바운더리 +1부터 끝까지로 잡음
        while left <= right:
            middle = (left+right)//2 # 중간값
            t_bound = arr[middle] # 볏짚 위치
            if t_bound > num+power: # 멀어서 안닿으면
                right = middle-1
            else: # 닿으면?
                bound = middle
                left = middle+1
                power += 1
        num = arr[bound]
        if power == prev_power:
            break
        prev_power = power
    return bound

def get_bound_start(idx):
    num = arr[idx]
    prev_power, power = 1, 1
    bound = idx
    while True: # 이중 while문으로 잡음
        left, right = 0, bound-1 # 범위를 바운더리 +1부터 끝까지로 잡음
        while left <= right:
            middle = (left+right)//2 # 중간값
            t_bound = arr[middle] # 볏짚 위치
            if t_bound < num-power: # 멀어서 안닿으면
                left = middle+1
            else: # 닿으면?
                bound = middle
                right = middle-1
                power += 1
        num = arr[bound]
        if power == prev_power:
            break
        prev_power = power
    return bound


N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()
# 각 숫자의 범위는 0~10억
# 폭발은 범위 1부터 시작한다.
# 최대 폭발할 수 있는 개수를 출력한다.
result = 0
# print(arr)
for i in range(N):
    start = get_bound_start(i)
    end = get_bound_end(i)
    if (end - start + 1) > result:
        result = end - start + 1
print(result)