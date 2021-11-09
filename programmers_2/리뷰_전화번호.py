from collections import defaultdict

def solution(phone_book):
    hash_map = defaultdict(int)
    
    for p in phone_book:
        hash_map[p] += 1
    
    for phone_number in phone_book:
        tmp = ''
        for t in phone_number:
            tmp += t
            if tmp in hash_map and tmp != phone_number:
                return False
    
    return True

# str.startswith() 사용하기
def solution(phoneBook):
    phoneBook=sorted(phoneBook)
    
    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True