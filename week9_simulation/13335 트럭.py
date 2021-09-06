from collections import deque

n, w, l = map(int, input().split())
trucks = deque(list(map(int, input().split())))
sec = 0
bridge = deque()
while trucks:
    sec += 1
    total = 0
    for weight, _ in bridge:
        total += weight
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
print(sec+1)