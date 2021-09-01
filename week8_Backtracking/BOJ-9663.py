#9663 N-Queen

"""
문제풀이 1: 프로미싱함수를 통해 가지치기 구현

"""
import sys
input = sys.stdin.readline

def promising(i):  #재귀 조건 적합 여부 판단
    for j in range(0,i):
        if row[j] == row[i] or abs(row[j]-row[i]) ==(i-j):
            return False

    return True

def N_queen(i):
    global ans
    if i ==N:
        ans += 1
    else:
        for j in range(N):
            row[i] = j
            if promising(i):
                N_queen(i+1)

ans = 0
N = int(input().rstrip())
row = [0]*15
N_queen(0)
print(ans)