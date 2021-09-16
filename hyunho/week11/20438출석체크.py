import sys
input = sys.stdin.readline

n, k, q, m = map(int, input().split())

students = [0]*(n+3)
sleep = set(map(int, input().split()))
attend = list(map(int, input().split()))
attendPossible = set()

for code in attend:
    if code in sleep:
        continue
    for ncode in range(code, n+3, code):
        if ncode not in sleep:
            attendPossible.add(ncode)
            
for i in range(3, n+3):
    students[i] += students[i-1]
    if i in attendPossible:
        students[i] += 1

for _ in range(m):
    s, e = map(int, input().split())
    print((e-s+1)-(students[e]-students[s-1]))