def _1105():
    A, B = map(str, input().split(' '))

    ret = 0

    if len(A) != len(B):
        print(0)
        return

    for i in range(len(A)):
        if A[i] == B[i]:
            if A[i] == '8':
                ret += 1
        else:
            break
    print(ret)
_1105()