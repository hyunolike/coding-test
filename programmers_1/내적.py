def solution(a, b):
    answer = 0
    for n1, n2 in zip(a,b):
        answer+=n1*n2
    return answer