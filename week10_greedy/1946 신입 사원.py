import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    apply = [list(map(int,input().split())) for _ in range(n)]
    apply = sorted(apply)
    answer = 1
    end = apply[0][1]

    for i in range(1, n):
        if end > apply[i][1]:
            end = apply[i][1]
            answer += 1

    print(answer)