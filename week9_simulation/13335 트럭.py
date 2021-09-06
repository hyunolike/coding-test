from collections import deque

n, w, l = map(int, input().split())
trucks = deque(list(map(int, input().split())))
bridge = deque()
sec = 0
while trucks:
    sec += 1
    total = sum([weight for weight, _ in bridge])
    
    if total+trucks[0] <= l and len(bridge) < w:
        go = trucks.popleft()
        bridge.append([go, 1])
    for i in range(len(bridge)):
        bridge[i][1] += 1
    if bridge[0][1] == w+1:
        bridge.popleft()

while bridge:
    sec += 1
    for i in range(len(bridge)):
        bridge[i][1] += 1
    if bridge[0][1] == w+1:
        bridge.popleft()
# 1초를 추가하는 이유
# 맨 앞 트럭이 다음 트럭이 들어 올 수 있도록 미리 빠져나가므로, 1초 일찍 종료됨
print(sec+1)