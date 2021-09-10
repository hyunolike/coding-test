n = int(input())
rooms = [list(map(int,input().split())) for _ in range(n)]
rooms = sorted(rooms, key=lambda x: (x[1], x[0]))
answer = 0
end = 0

for s, e in rooms:
    if end <= s:
        answer+=1
        end = e

print(answer)