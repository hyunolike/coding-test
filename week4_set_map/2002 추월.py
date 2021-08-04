import sys

start = dict()
end = dict()
answer = 0
order = []

n = int(input())
for i in range(n):
    car = sys.stdin.readline().strip()
    start[car] = i

for i in range(n):
    car = sys.stdin.readline().strip()
    end[car] = i
    order.append(car)

for i in range(len(order)):
    for j in range(i+1, len(order)):
        if start[order[i]] > start[order[j]]:
            answer += 1
            break

print(answer)