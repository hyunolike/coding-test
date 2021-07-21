import sys
from collections import deque

input = sys.stdin.readline

itself = deque()
itself.append((0, 0))
trans = list()
apples = list()

sec, snakeLength, idx = 0, 1, -1
pos = [0, 0]
head = 'D'
x, y = (1, 0, -1, 0), (0, 1, 0, -1)  # 우하좌상

n = int(input())
k = int(input())

for _ in range(k):
    tmp = list(map(int, input().split()))
    tmp[0], tmp[1] = tmp[1]-1, tmp[0]-1
    apples.append(tmp)

k = int(input())
for _ in range(k):
    a, b = input().split()
    trans.append(int(a))
    trans.append(b)

while True:
    # move
    if head == 'D':
        idx = (idx + 1) % 4
    elif head == 'L':
        idx = (idx - 1) % 4
    else:
        idx = idx

    pos[0] = pos[0] + x[idx]  # x
    pos[1] = pos[1] + y[idx]  # y

    # crash
    if tuple(pos) in itself:  # 자기자신
        sec += 1
        break
    if pos[0] < 0 or pos[1] < 0:  # 벽
        sec += 1
        break
    if pos[0] == n or pos[1] == n:  # 벽
        sec += 1
        break

    # apple
    if apples and pos in apples:
        apples.remove(pos)
        snakeLength += 1

    itself.append(tuple(pos))
    if snakeLength < len(itself):
        itself.popleft()

    # head
    if trans and sec + 1 == trans[0]:
        head = trans[trans.index(sec + 1) + 1]
        del trans[0]
        del trans[0]
    else:
        head = ''

    sec += 1
print(sec)
