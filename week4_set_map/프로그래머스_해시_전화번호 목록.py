def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book, key=len)
    
    for n1 in phone_book:
        for n2 in phone_book:
            if n1 == n2[:len(n1)] and n1 != n2:
                answer = False
                return answer
    
    return answer