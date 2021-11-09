def solution(n):
    answer = 0
    three=''
    while n!=0:
        three+=str(n%3)
        n=n//3
    for i in range(len(three)):
        answer+=int(three[i])*(3**(len(three)-i-1))
    return answer


# 문자열 뒤집기
def reversed(three):
    three=three[::-1]
    three=reversed(three)
    return three

# another solution
def solution(n):
    tmp=''
    while n:
        tmp+=str(n%3)
        n=n//3
    # int()함수에 스트링 to 진법 변환 기능 있다.
    answer=int(tmp, 3)
    return answer

