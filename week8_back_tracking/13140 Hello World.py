from itertools import permutations

def solution(n):
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    for s in permutations(num, 7):
        h, e, l, o, w, r, d = s
        word_hello = 10000 * h + 1000 * e + 100 * l + 10 * l + o
        word_world = 10000 * w + 1000 * o + 100 * r + 10 * l + d
        if word_hello + word_world == n and h != 0 and w != 0:
            print(f"  {word_hello}")
            print(f"+ {word_world}")
            print("-------")
            if n>=100000:
                print(f" {n}")
            else:
                print(f"  {n}")
            return
    print("No Answer")

n = int(input())
solution(n)