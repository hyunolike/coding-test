from collections import deque

def first(m, data):
    data = deque(data)
    cnt=0

    while data:
        max_n = max(data)
        if max_n[0] == data[0][0]:
            if m == data[0][1]:
                data.popleft()
                cnt += 1
                print(cnt)
                return 0
            else:
                cnt += 1
                data.popleft()
        else:
            data.append(data.popleft())


test = int(input())
for i in range(test):
    data = []
    n, m = map(int, input().split())
    tmp = list(map(int, input().split()))
    for i, num in enumerate(tmp):
        data.append((num, i))
    first(m,data)
