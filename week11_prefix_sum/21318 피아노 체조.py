import sys
input = sys.stdin.readline

n = int(input())
play = list(map(int, input().split()))
play = [0]+play
fail = [0]*(n+1) # 실수한 개수 누적합

for i in range(n):
    if play[i] > play[i+1]:
        fail[i] += 1

for i in range(1, len(fail)):
    fail[i] += fail[i-1]

test = int(input())
for _ in range(test):
    x, y = map(int, input().split())
    answer = fail[y]-fail[x-1]
    if fail[y] != fail[y-1]:
        answer -= 1
    print(answer)