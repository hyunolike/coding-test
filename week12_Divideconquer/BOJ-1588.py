import sys
input = sys.stdin.readline

def get_count(N):
    count = [[(1, 0, 0)],
             [(0, 1, 0)],
             [(0, 0, 1)]]
    for _ in range(N):
        for i in range(3):
            a, b, c = count[i][-1]
            count[i].append((a + b * 2,
                          b + a + c * 2,
                          c + a))
    return count

def solve(x, N, L, R):
    all = 3 ** N
    if R - L + 1 == all:
        return pre_count[x][N]
    t = all // 3
    ret = []
    for next_x in [(0, 2, 1), (1, 0, 0), (1, 2, 1)][x]:
        if L <= t and 0 <= R:
            ret.append(solve(next_x, N - 1, max(0, L), min(t - 1, R)))
        L -= t
        R -= t
    return sum(ret[i][0] for i in range(len(ret))),\
           sum(ret[i][1] for i in range(len(ret))),\
           sum(ret[i][2] for i in range(len(ret)))


x = int(input()) - 1
L = int(input())
R = int(input())
N = int(input())
pre_count = get_count(N)
print(*solve(x, N, L, R))