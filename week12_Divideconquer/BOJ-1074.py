import sys
sys.setrecursionlimit(100000000)


def input():
    return sys.stdin.readline()
    

N, r, c = map(int, input().split())
result = 0
while N >= 1:
    if r < 2 ** (N-1) and c < 2 ** (N-1):
        N -= 1
    elif r < 2 ** (N-1) <= c:
        result += 4**(N-1)
        c -= 2**(N-1)
        N -= 1
    elif r >= 2 ** (N - 1) > c:
        result += 4**(N-1)*2
        r -= 2**(N-1)
        N -= 1
    else:
        result += 4**(N-1)*3
        r -= 2 ** (N - 1)
        c -= 2 ** (N - 1)
        N -= 1
print(result)
